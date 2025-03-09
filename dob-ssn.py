import re

def removePII():
    returnPhrase = ""
    
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        lineNum = 0

        for x in lines:
            # the find regex patterns 
            dobPhrases = [r"\bdate[\s\-_]*of[\s\-_]*birth\b", r"D[\s\-_]O[\s\-_]B"]
            datePhrases = [r"\b\d{4}[\s\-/]*\d{1,2}[\s\-/]*\d{1,2}\b", r"\b\d{1,2}[/\-]\d{1,2}[/\-]\d{4}\b"]
            ssnPhrases = [r"\d{3}[\s\-_]?\d{2}[\s\-_]?\d{4}"]

            # DOB section
            for y in dobPhrases:
                if re.search(y, x, re.IGNORECASE):
                    print(f"Match found on line {lineNum}: DOB phrase detected.")
                    
                    # replacement time
                    for z in datePhrases:
                        x = re.sub(z, "*dob*", x, flags=re.IGNORECASE)
            
            # SSN section
            for y in ssnPhrases:
                x = re.sub(y, "*ssn*", x, flags=re.IGNORECASE)

            # store line, also any modifications
            returnPhrase += x
            lineNum += 1  # counting lines

    return returnPhrase

# call function, the print/return is the new file
print(removePII())
