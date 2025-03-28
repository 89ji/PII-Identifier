import re

def allergies(text):
    lines = text.split("\n")
    new_text = []
    inside_allergies_section = False  # tracks if we are in the section
    allergiesPhrases = [r"\ballergies?\b", r"\ballergy?\b"]

    for line in lines:

        # ignore bulleted sections please
        if inside_allergies_section and not re.match(r"^\s*[-•]", line):
            inside_allergies_section = False  # Stop ignoring text

        # Detect allergies section
        for y in allergiesPhrases:
            if re.search(y, line, re.IGNORECASE):
                inside_allergies_section = True  
                new_text.append("*allergies*")  # redact added
                break # skip the line
                
        # append only lines not inside the allergies section
        if not inside_allergies_section:
            new_text.append(line)

    return "\n".join(new_text)