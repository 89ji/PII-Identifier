import re

def bio_identifiers(fullText):
    biometric_tag = "*biometric*"
    removed = []

    biometric_finder = re.compile(
        r"[bB]iometric(?: [nN]umbers?)?[:\-]\s?(.*)", re.IGNORECASE
    )
    matches = biometric_finder.findall(fullText)

    for biometric in matches:
        biometric_clean = biometric.strip()
        removed.append(biometric_clean)
        fullText = fullText.replace(biometric_clean, biometric_tag)

    return fullText, removed