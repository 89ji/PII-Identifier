import re

def removeSSN(text):
    ssn_tag = "*ssn*"

    ssn_finder = re.compile(r"(SSN|Social Security| Social Security Number):\s?((\d|\*){3}[\s\-_]?(\d|\*){2}[\s\-_]?(\d|\*){4})", re.IGNORECASE)
    match = ssn_finder.search(text)

    if match:
        ssn_num = match.group(2).strip()
        text = text.replace(ssn_num, ssn_tag)
    
    return text