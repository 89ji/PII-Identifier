import re

def removeUniqueID(text):
    matches = []
    devPhrases = [
    r"\bcode\b",                  # code
    r"\bID\b",                    # ID
    r"group no."                  # group no.            
    ]
    devPhrase = "("

    for phrase in devPhrases:
        devPhrase += phrase + "|"
    devPhrase = devPhrase[:-1] + r"):?\s?(\d+)"

    for match in re.finditer(devPhrase, text, re.IGNORECASE):
        matches.append(match.group(2))
        text = text.replace(match.group(2), "*uniqueID*", 1)

    return text, matches
