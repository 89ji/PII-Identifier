import re

def removeUniqueID(text):
    lines = text.split("\n")
    new_text = []
    removed_values = []
    devPhrases = [
    r"\bcode\b",                  # code
    r"\bID\b",                    # ID
    ]

    for line in lines:

        # Detect lab results section
        if any(re.search(phrase, line, re.IGNORECASE) for phrase in devPhrases): #sees tag and replaces after
            # Replace text after colon with "*device ID*"
            match = re.search(r":\s*(.+)", line)
            if match:
                removed_values.append(match.group(1).strip())
                new_line = re.sub(r"(:\s*)(.+)", r"\1*Unique Code*", line)
                new_text.append(new_line)
            else:
                new_text.append(line)
        else:
            new_text.append(line)
        
    return ("\n".join(new_text), removed_values)
