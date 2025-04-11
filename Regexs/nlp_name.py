import spacy
import re

NAME_TAG = "*name*"
PROVIDER_TAG = "*provider*"
SOCIAL_WORKER_TAG = "*social_worker*"

nlp = spacy.load("en_core_web_trf")

def remove_names(text, tag_names=True, tag_providers=True, tag_social_workers=True):
    text_copy = text[:]
    doc = nlp(text_copy)

    names = []
    providers = []
    social_workers = []

    replacements = []

    provider_title_pattern = re.compile(r'\b(Dr|MD|PhD|DDS|DVM|DO|PA|NP|RN|LPN|CNA)\b', re.IGNORECASE)
    social_worker_pattern = re.compile(r'\b(Social Worker|SW|LCSW|MSW)\b', re.IGNORECASE)
    honorific_pattern = re.compile(r'\s?(,?\s?\b(Mr|Mrs|Miss|Ms|Dr|MD|PhD|DDS|DVM|DO|PA|NP|RN|LPN|CNA)\.?)\s?', re.IGNORECASE)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            person = ent.text
            start, end = ent.start_char, ent.end_char

            context_window = text_copy[max(0, start - 20):end + 10]
            tag = None
            target_list = None

            if tag_providers and provider_title_pattern.search(context_window):
                tag = PROVIDER_TAG
                target_list = providers
            elif tag_social_workers and social_worker_pattern.search(context_window):
                tag = SOCIAL_WORKER_TAG
                target_list = social_workers
            elif tag_names:
                tag = NAME_TAG
                target_list = names
            
            for match in honorific_pattern.finditer(text_copy):
                match_start, match_end = match.span(1)
                if abs(match_end - start) <= 1 or abs(match_start - end) <= 1:
                    start = min(start, match_start)
                    end = max(end, match_end)
                    person = text_copy[start:end]

            if tag:
                replacements.append((start, end, tag, person, target_list))

    replacements.sort(key=lambda x: x[0], reverse=True)

    for start, end, tag, original_text, target_list in replacements:
        text_copy = text_copy[:start] + tag + text_copy[end:]
        target_list.insert(0, original_text)

    return text_copy, names, providers, social_workers