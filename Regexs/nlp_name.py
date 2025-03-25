import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import AlbertModel, AlbertTokenizer
import os
import re
import spacy

class NameClassifier(nn.Module):
    def __init__(self, bert_model_name="albert-base-v2"):
        super(NameClassifier, self).__init__()
        self.bert = AlbertModel.from_pretrained(bert_model_name)
        self.fc = nn.Linear(self.bert.config.hidden_size, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]
        logits = self.fc(cls_output)
        return self.sigmoid(logits)

class NameDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]["input_ids"], self.data[idx]["attention_mask"]

def create_context_window(words, i):
    start = max(0, i - WINDOW_SIZE)
    end = min(len(words), i + WINDOW_SIZE + 1)

    beginning_pad = ["[PAD]"] * (max(0, WINDOW_SIZE - i))
    ending_pad = ["[PAD]"] * (max(0, (i + WINDOW_SIZE + 1) - len(words)))

    context_window = ["[CLS]"] + beginning_pad + words[start:i] + ["<w>"] + [words[i]] + ["</w>"] + words[i+1:end] + ending_pad + ["[SEP]"]
    return context_window

def create_data(tokens):
    data = []

    for i in range(len(tokens)):
        context_window = create_context_window(tokens, i)

        encoding = tokenizer(context_window, padding="max_length", max_length=35, truncation=True, is_split_into_words=True, return_tensors="pt")

        data.append({
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_mask"].squeeze(0),
        })

    return data

def preprocess_text(text):
    processed_text = text.replace("\n", " ").split()

    return processed_text

def predict_name(model, text):
    data = create_data(text)
    dataset = NameDataset(data)
    loader = DataLoader(dataset, batch_size=32, shuffle=False)

    model.eval()
    prediction = []
    with torch.no_grad():
        for batch in loader:
            input_ids, attention_mask = batch
            input_ids, attention_mask = input_ids.to(device), attention_mask.to(device)

            outputs = model(input_ids, attention_mask)
            predictions = (outputs > 0.5).float()
            predictions = predictions.squeeze()

            predictions_list = predictions.tolist()
            predictions_list = predictions_list if isinstance(predictions_list, list) else [predictions_list]

            prediction.extend(predictions_list)
    
    return prediction

def remove_names(text, tag_names=True, tag_providers=True):
    text_copy = str(text)
    processed_text = preprocess_text(text_copy)
    no_punctuation_text = [re.sub(r"[,\.]", "", token) for token in processed_text]
    predictions = predict_name(model, processed_text)
    names = [name for name, pred in zip(processed_text, predictions) if pred == 1]

    checked_names = []
    for match in names:
        doc = nlp(match)
        if any(ent.label_ == "PERSON" for ent in doc.ents):
            checked_names.append(match)
    
    cleaned_text = [re.sub(r"[,\.]", "", token) for token in checked_names]
    for name in cleaned_text:
        name_index = no_punctuation_text.index(name)
        context_window = processed_text[max(0, name_index - WINDOW_SIZE):min(len(processed_text), name_index + WINDOW_SIZE + 1)]
        context_text = " ".join(context_window)
        
        provider_pattern = re.compile(r"\b(Dr|MD|PhD|DDS|DVM|DO|PA|NP|RN|LPN|CNA)\b")
        if tag_providers and provider_pattern.search(context_text):
            text = text.replace(name, "*provider_name*")
        elif tag_names and not provider_pattern.search(context_text):
            text = text.replace(name, "*name*")
    
    if tag_names:
        text = re.sub(r"(\*\bname\*) (\*name\b\*)", "*name*", text)
    if tag_providers:
        text = re.sub(r"(\*\bprovider_name\*) (\*provider_name\b\*)", "*provider_name*", text)
    
    if tag_providers:
        text = re.sub(r"\b(Dr|MD|PhD|DDS|DVM|DO|PA|NP|RN|LPN|CNA)\b.*?\b(Dr|MD|PhD|DDS|DVM|DO|PA|NP|RN|LPN|CNA)\b", "*provider_name*", text)
    
    if tag_names:
        text = re.sub(r"((Mr|Mrs|Miss|Ms)\.) (([A-Z][a-z]* ?)*)" , "", text)

    return text

WINDOW_SIZE = 5

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AlbertTokenizer.from_pretrained("albert-base-v2")
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ML_Approach", "name_classifier.pth")
model = NameClassifier()
model.load_state_dict(torch.load(model_path, weights_only=True, map_location=device))
model.to(device)
nlp = spacy.load("en_core_web_trf")