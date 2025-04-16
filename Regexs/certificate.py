import re

def certificate(fullText: str) -> str:
    certificate_tag = "*certificate_num*"

    certificate_finder = re.compile(r"[cC]ertificate(?: [nN]umber)?:\s?([A-Z]{2}\d{3}[a-z]-?\d{4})")
    cert_matches = []

    for match in certificate_finder.finditer(fullText):
        cert_matches.append(match.group(1))
        fullText = fullText.replace(match.group(1), certificate_tag, 1)
    
    license_tag = "*license_num*"

    license_finder = re.compile(r"[lL]icense(?: [nN]umber)?:\s?([A-Z]{2}\d{2}-?\d{6})")
    license_matches = []
    
    for match in license_finder.finditer(fullText):
        license_matches.append(match.group(1))
        fullText = fullText.replace(match.group(1), license_tag, 1)

    return fullText, cert_matches, license_matches