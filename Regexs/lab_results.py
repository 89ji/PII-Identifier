import re

def removeLabResults(text):
    lines = text.split("\n")
    new_text = []
    inside_lab_section = False  # tracks if we are in the section
    labPhrases = [r"\bresults?\b", r"\blab results?\b", r"\btest results?\b"]

    for line in lines:

        # ignore bulleted sections please
        if inside_lab_section and not re.match(r"(^\s*$|^\s*[-•])", line):
            inside_lab_section = False  # Stop ignoring text

        # Detect lab results section
        for y in labPhrases:
            if re.search(y, line, re.IGNORECASE):
                inside_lab_section = True  
                new_text.append("*lab results*\n")  # redact added
                break # skip the line
                
        # append only lines not inside the lab results section
        if not inside_lab_section:
            new_text.append(line)

    return "\n".join(new_text)