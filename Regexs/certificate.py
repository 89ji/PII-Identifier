import re

def certificate(fullText: str) -> str:
    certificate_tag = "*certificate_num*"

    certificate_finder = re.compile(r"[cC]ertificate(?: [nN]umber)?:\s?([A-Z]{2}\d{3}[a-z]-?\d{4})")
    match = certificate_finder.findall(fullText)

    if len(match) > 0:
        print(f"Certificate match: {match}")
        for certificate in match:
            certificate_num = certificate.strip()
            fullText = fullText.replace(certificate_num, certificate_tag)
    
    license_tag = "*license_num*"

    license_finder = re.compile(r"[lL]icense(?: [nN]umber)?:\s?([A-Z]{2}\d{2}-?\d{6})")
    match = license_finder.findall(fullText)
    
    if len(match) > 0:
        print(f"License match: {match}")
        for license_num in match:
            license_num = license_num.strip()
            fullText = fullText.replace(license_num, license_tag)

    return fullText