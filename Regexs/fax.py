import re

def FindFax(fullText :str) -> str:
    tag = "*fax number*"
    regex = re.compile(r"(Fax number|Fax no\.?): ?(.*)", re.I)
    matches = regex.findall(fullText)


    for match in matches:
        fullText = fullText.replace(match[1], tag)
    return fullText
