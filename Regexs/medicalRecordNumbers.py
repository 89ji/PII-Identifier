import re

def FindRecordNumbers(fullText :str) -> str:
    tag = "*medical record number*"
    regex = re.compile(r"(.*medical record number.*): ?(.*)", re.I)
    matches = regex.findall(fullText)
    for match in matches:
        fullText = fullText.replace(match[1], tag)
    return fullText
