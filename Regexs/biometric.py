import re

def bio_identifiers(fullText):
    biometric_tag = "*biometric*"

    biometric_finder = re.compile(r"[bB]iometric(?: [nN]umbers?)?[:-]\s?(.*)", re.IGNORECASE)
    matches = []

    for match in biometric_finder.finditer(fullText):
        matches.append(match.group(1))
        fullText = fullText.replace(match.group(1), biometric_tag, 1)

    return fullText, matches