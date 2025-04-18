import re

def certificate(fullText: str) -> str:
    certificate_tag = "*certificate_num*"
    license_tag = "*license_num*"

    removed = {
        "certificates": [],
        "licenses": []
    }

    # Certificate pattern
    certificate_finder = re.compile(
        r"[cC]ertificate(?: [nN]umber)?:\s?([A-Z]{2}\d{3}[a-z]-?\d{4})"
    )
    certificate_matches = certificate_finder.findall(fullText)

    for cert_num in certificate_matches:
        cert_num_clean = cert_num.strip()
        removed["certificates"].append(cert_num_clean)
        fullText = fullText.replace(cert_num_clean, certificate_tag)

    # License pattern
    license_finder = re.compile(
        r"[lL]icense(?: [nN]umber)?:\s?([A-Z]{2}\d{2}-?\d{6})"
    )
    license_matches = license_finder.findall(fullText)

    for lic_num in license_matches:
        lic_num_clean = lic_num.strip()
        removed["licenses"].append(lic_num_clean)
        fullText = fullText.replace(lic_num_clean, license_tag)

    return fullText, removed