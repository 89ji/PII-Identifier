import re

def FindMedicaid(fullText: str) -> str:
    tag = "*medicaid id*"
    medicaidFinder = re.compile(r"\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4}")
    return medicaidFinder.sub(tag, fullText)

    return fullText
