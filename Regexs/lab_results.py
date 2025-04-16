import re

def removeLabResults(text):
    lines = text.split("\n")
    new_text = []
    matches = []
    inside_lab_section = False  # Tracks if we're inside a section to redact
    labPhrases = [r"\bresults?\b", r"\blab results?\b", r"\btest results?\b"]
    current_section = []

    for line in lines:
        if inside_lab_section and re.match(r"^.*:\s*$", line):
            matches.append('\n'.join(current_section).strip())
            current_section = []
            inside_lab_section = False

        if inside_lab_section:
            current_section.append(line)

        if not inside_lab_section:
            for phrase in labPhrases:
                if re.search(phrase, line, re.IGNORECASE):
                    inside_lab_section = True
                    current_section = [line]
                    new_text.append("*lab results*\n")
                    break
        
        if not inside_lab_section:
            new_text.append(line)

    if inside_lab_section and current_section:
        matches.append('\n'.join(current_section))

    return "\n".join(new_text), matches