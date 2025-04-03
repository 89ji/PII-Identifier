import re

def FindHospitals(fullText :str) -> str:
    tag = "*hospital*"
    
    hospital_finder = re.compile(r"Hospital(?: name)?: (([A-Z][a-z]* ?)*)", re.IGNORECASE)
    match = hospital_finder.search(fullText)
    
    if match:
        hospital_name = match.group(1).strip()
        fullText = fullText.replace(hospital_name, tag)

    return fullText