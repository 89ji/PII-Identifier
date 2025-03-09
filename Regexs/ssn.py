import re

def removeSSN(text):
    returnPhrase = ""
    lines = text.split("\n")

    for x in lines:
        # the find regex patterns 
        ssnPhrases = [r"\d{3}[\s\-_]?\d{2}[\s\-_]?\d{4}"]
        
        # SSN section
        for y in ssnPhrases:
            x = re.sub(y, "*ssn*", x, flags=re.IGNORECASE)

        # store line, also any modifications
        returnPhrase += x + "\n"

    return returnPhrase