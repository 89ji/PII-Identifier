import re

def removeSSN(text):
    ssn_tag = "*ssn*"
    removed = []

    ssn_finder = re.compile(
        r"(SSN|Social[\s\-_]Security|Social[\s\-_]Security[\s\-_]Number):\s?((\d|\*){3}[\s\-_]?(\d|\*){2}[\s\-_]?(\d|\*){4})",
        re.IGNORECASE
    )

    def replacer(match):
        ssn = match.group(2).strip()
        removed.append(ssn)
        return match.group(1) + ": " + ssn_tag

    text = ssn_finder.sub(replacer, text)
    return text, removed