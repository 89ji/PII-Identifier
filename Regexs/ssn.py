import re

def removeSSN(text):
    ssn_tag = "*ssn*"

    ssn_finder = re.compile(r"(SSN|Social Security| Social Security Number):\s?((\d|\*){3}[\s\-_]?(\d|\*){2}[\s\-_]?(\d|\*){4})", re.IGNORECASE)
    matches = []

    for match in ssn_finder.finditer(text):
        matches.append(match.group(2))
        text = text.replace(match.group(2), ssn_tag, 1)
    
    return text, matches