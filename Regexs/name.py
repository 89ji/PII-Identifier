import re
import spacy

nlp = spacy.load("en_core_web_sm")

name = r"[A-Z][a-z]+ [A-Z][a-z]+"
with open("ehr JMS.txt", "r") as file:

    for line in file:   
        result = re.findall(name, line) # Find potenial first and last names
        for match in result:
            doc = nlp(match) # Process possible names through spaCy
            if any(ent.label_ == "PERSON" for ent in doc.ents):
                print(match)
