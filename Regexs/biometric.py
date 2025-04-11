import re

def bio_identifiers(fullText):
    biometric_tag = "*biometric*"

    biometric_finder = re.compile(r"[bB]iometric(?: [nN]umbers?)?[:-]\s?(.*)", re.IGNORECASE)
    match = biometric_finder.findall(fullText)

    if len(match) > 0:
        for phone in match:
            phone_num = phone.strip()
            fullText = fullText.replace(phone_num, biometric_tag)

    return fullText