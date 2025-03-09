import re

def removePII():
    returnPhrase = ""
    
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        lineNum = 0

        for x in lines:
            found = False
            # Patterns
            dobPhrases = [r"\bdate[\s\-_]*of[\s\-_]*birth\b", r"D[\s\-_]O[\s\-_]B"]
            datePhrases = [r"\b\d{4}[\s\-/]*\d{1,2}[\s\-/]*\d{1,2}\b", r"\b\d{1,2}[/\-]\d{1,2}[/\-]\d{4}\b"]
            ssnPhrases = [r"\d{3}[\s\-_]?\d{2}[\s\-_]?\d{4}"]

            # Search and replace DOB indicators
            for y in dobPhrases:
                if re.search(y, x, re.IGNORECASE):
                    print(f"Match found on line {lineNum}: DOB phrase detected.")
                    
                    # Replace date mentions in the same line
                    for z in datePhrases:
                        x = re.sub(z, "*dob*", x, flags=re.IGNORECASE)
            
            # Search and replace SSNs
            for y in ssnPhrases:
                x = re.sub(y, "*ssn*", x, flags=re.IGNORECASE)

            # Store modified line
            returnPhrase += x
            lineNum += 1  # Move to next line

    return returnPhrase

# Call function and print cleaned text
print(removePII())
