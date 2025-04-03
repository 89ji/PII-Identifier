import re

def FindMedicaid(fullText: str) -> str:
    tag = "*medicaid id*"
    medicaidFinder = re.compile(r"Medicaid(?: account)?: (\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4})", re.IGNORECASE)
    match = medicaidFinder.search(fullText)
    if match:
        medicaid_num = match.group(1).strip()
        fullText = fullText.replace(medicaid_num, tag)
    
    return fullText