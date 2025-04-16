import re

def removeDOB(text):
    returnPhrase = ""
    lines = text.split("\n")
    matches = []

    for x in lines:
        # the find regex patterns
        dobPhrases = [r"\bdate[\s\-_]*of[\s\-_]*birth\b", r"D[\s\-_]?O[\s\-_]?B", r"birth[\s\-_]*date", r"birth[\s\-_]*day", r"born[\s:]"]
        datePhrases = [r"\b\d{4}[\s\-/]*\d{1,2}[\s\-/]*\d{1,2}\b", r"\b\d{1,2}[/\-]\d{1,2}[/\-]\d{4}\b"]

        # DOB section
        for y in dobPhrases:
            if re.search(y, x, re.IGNORECASE):
                for z in datePhrases:
                    # Find all matches before replacing
                    found_dates = re.findall(z, x, flags=re.IGNORECASE)
                    # Add each found date to matches list
                    for date in found_dates:
                        matches.append(date)
                    # Perform the replacement
                    x = re.sub(z, "*dob*", x, flags=re.IGNORECASE)

        # store line, also any modifications
        returnPhrase += x + "\n"

    return returnPhrase, matches