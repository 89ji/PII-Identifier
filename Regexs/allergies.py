import re

def allergies(text, allergies_input=None):
    allergies_tag = "*allergies*"
    if allergies_input is None:
        return text
    lines = text.split("\n")
    new_text = []
    allergiesPhrases = [allergy.strip() for allergy in allergies_input.split(",")]
    allergiesPhrases = [phrase for phrase in allergiesPhrases if phrase]
    allergies_pattern = str()

    for phrase in allergiesPhrases:
        if allergies_pattern:
            allergies_pattern += "|"
        allergies_pattern += re.escape(phrase)

    for line in lines:
        if re.search(allergies_pattern, line, re.IGNORECASE):
            new_text.append(f"{allergies_tag}")
        else:
            new_text.append(line)

    return "\n".join(new_text)