import re

def allergies(text, allergies_input=None):
    allergies_tag = "*allergies*"
    if allergies_input is None:
        return text, []

    lines = text.split("\n")
    new_text = []
    removed = []

    allergiesPhrases = [allergy.strip() for allergy in allergies_input.split(",") if allergy.strip()]
    if not allergiesPhrases:
        return text, []

    allergies_pattern = "|".join(re.escape(phrase) for phrase in allergiesPhrases)

    for line in lines:
        if re.search(allergies_pattern, line, re.IGNORECASE):
            removed.append(line)
            new_text.append(allergies_tag)
        else:
            new_text.append(line)

    return "\n".join(new_text), removed