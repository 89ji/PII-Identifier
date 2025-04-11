import re

def remove_phone_numbers(text):
    phone_tag = "*phone*"
    phone_finder = re.compile(r"([pP]hone)(?: [nN]umbers?)?:\s?((?:\+\d{1,2}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})", re.IGNORECASE)
    
    matches = []
    substituted_text = text

    for match in phone_finder.finditer(text):
        phone_num = match.group(2).strip()
        matches.append(phone_num)
        substituted_text = substituted_text.replace(phone_num, phone_tag, 1)

    return substituted_text, matches