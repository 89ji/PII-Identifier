import re
import spacy

nlp = spacy.load("en_core_web_sm")

def removeName(text):
    
    name = r"[A-Z][a-z]+ [A-Z][a-z]+"
    #with open("ehr JMS.txt", "r") as file:
    
        redacted = []     # Empty list to store modified lines
        #for line in text:   #changed file to text
            result = re.findall(name, text) # Find potenial first and last names
            for match in result:
                doc = nlp(match) # Process possible names through spaCy
                if any(ent.label_ == "PERSON" for ent in doc.ents):
                   #print(match)
                   line = line.replace(match, "*name*")  # Replace name
return redacted.append(text)    # Add modified line to list for writing back to file

# Test with file output
#with open("ehr_JMS_redacted.txt", "w") as output_file:
#    output_file.writelines(redacted)

#print("Redacted file saved as 'ehr_JMS_redacted.txt'")
     
