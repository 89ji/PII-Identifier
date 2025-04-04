import re

def FindBeneficiary(fullText :str) -> str:
    tag = "*health plan beneficiary number*"
    regex = re.compile(r"(.*health plan beneficiary number.*): ?(.*)", re.I)
    matches = regex.findall(fullText)
    for match in matches:
        fullText = fullText.replace(match[1], tag)
    return fullText
