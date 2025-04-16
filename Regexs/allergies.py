import re

def allergies(text, allergies_input=None):
    allergies_tag = "*allergies*"
    if allergies_input is None:
        return text
    allergiesPhrases = [allergy.strip() for allergy in allergies_input.split(",")]
    allergiesPhrases = [phrase for phrase in allergiesPhrases if phrase]
    allergies_pattern = str()
    matches = []

    for phrase in allergiesPhrases:
        if allergies_pattern:
            allergies_pattern += "|"
        allergies_pattern += re.escape(phrase)

    for match in re.finditer(allergies_pattern, text, re.IGNORECASE):
        matches.append(match.group())
        text = text.replace(match.group(), allergies_tag, 1)

    return text, matches