import re

def removeRegName(text):
    returnPhrase = ""
    lines = text.split("\n")

    for x in lines:
        # the find regex patterns
        labelPhrases = [r"(patient[\s:]*name|name)[\s:]*", r"(patient|name)[\s:]*"]
        namePhrases = [r"[A-Z][a-z]+(?: [A-Z][a-z]+)*"]
        savedName = []

        # DOB section
        for y in labelPhrases:
            if re.search(y, x, re.IGNORECASE):
                # print(f"Match found on line {lineNum}: DOB phrase detected.")
                
                # replacement time
                for z in namePhrases:
                    match = re.search(z, x, flags=re.IGNORECASE)
                    if match:
                        if match.group(1):
                            first_name = match.group(1)
                        else:
                            False
                        if match.group(2):
                            last_name = match.group(2) 
                        else:
                            False  # last name

                    x = re.sub(z, "*name*", x, flags=re.IGNORECASE)
        
        if first_name: #if theres a first name found, replace it later on
            x = re.sub(rf"\b{re.escape(first_name)}\b", "*name*", x, flags=re.IGNORECASE)

        if last_name: #same for last name
            x = re.sub(rf"\b{re.escape(last_name)}\b", "*name*", x, flags=re.IGNORECASE)

        # store line, also any modifications
        returnPhrase += x + "\n"

    return returnPhrase