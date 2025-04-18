import re

def removeLabResults(text):
    lines = text.split("\n")
    new_text = []
    removed = []
    inside_lab_section = False
    labPhrases = [r"\bresults?\b", r"\blab results?\b", r"\btest results?\b"]

    for line in lines:
        # Check for end of lab section
        if inside_lab_section and re.match(r"^.*:\s*$", line):
            inside_lab_section = False

        # Check if we should start redacting
        if not inside_lab_section:
            for phrase in labPhrases:
                if re.search(phrase, line, re.IGNORECASE):
                    inside_lab_section = True
                    removed.append(line)
                    new_text.append("*lab results*")
                    break
            else:
                new_text.append(line)
        else:
            removed.append(line)

    return "\n".join(new_text), removed