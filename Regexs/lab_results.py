import re

def removeLabResults(text):
    lines = text.split("\n")
    new_text = []
    inside_lab_section = False  # Tracks if we're inside a section to redact
    labPhrases = [r"\bresults?\b", r"\blab results?\b", r"\btest results?\b"]

    for line in lines:
        # stop if we find "Text:" (signaling end of section)
        if inside_lab_section and re.match(r"^.*:\s*$", line):
            inside_lab_section = False  # stop ignoring

        # Ignore lab results sections
        if not inside_lab_section:
            for phrase in labPhrases:
                if re.search(phrase, line, re.IGNORECASE):
                    inside_lab_section = True  # Start ignoring
                    new_text.append("*lab results*\n")  # Redact with placeholder
                    break  # Skip this line
        
        # Keep lines that are not part of the redacted section
        if not inside_lab_section:
            new_text.append(line)

    return "\n".join(new_text)

with open("test2.txt") as target:
    text = target.read()

with open("output.txt", "w") as new_file:
    new_file.write(removeLabResults(text))