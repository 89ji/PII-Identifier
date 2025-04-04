import re

def removeUniqueID(text):
    lines = text.split("\n")
    new_text = []
    devPhrases = [
    r"\bcode\b",                  # code
    r"\bID\b",                    # ID
    ]

    for line in lines:

        # Detect lab results section
        if any(re.search(phrase, line, re.IGNORECASE) for phrase in devPhrases): #sees tag and replaces after
            # Replace text after colon with "*device ID*"
            new_line = re.sub(r"(:\s*)(.+)", r"\1*Unique Code*", line)
            new_text.append(new_line)
        else:
            new_text.append(line)
        

    return "\n".join(new_text)


with open("test2.txt") as target:
    text = target.read()
with open("output.txt", "w") as new_file:
    new_file.write(removeUniqueID(text))