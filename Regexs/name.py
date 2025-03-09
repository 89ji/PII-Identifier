import re
import spacy

nlp = spacy.load("en_core_web_sm")

name = r"[A-Z][a-z]+ [A-Z][a-z]+"
with open("ehr JMS.txt", "r") as file:
    
    redacted = []
    for line in file:   
        result = re.findall(name, line) # Find potenial first and last names
        for match in result:
            doc = nlp(match) # Process possible names through spaCy
            if any(ent.label_ == "PERSON" for ent in doc.ents):
               #print(match)
               line = line.replace(match, "*name*")  # Replace name
        redacted.append(line)

# Test with file output
#with open("ehr_JMS_redacted.txt", "w") as output_file:
#    output_file.writelines(redacted)

#print("Redacted file saved as 'ehr_JMS_redacted.txt'")
     
