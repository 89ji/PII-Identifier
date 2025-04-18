import re

def FindAddresses(fullText: str):
    tag = "*address*"
    street_suffixes = "Street St Avenue Ave Boulevard Blvd Road Rd Drive Dr Court Ct Lane Ln Place Pl Way Terrace Ter Circle Cir Trail Trl Cove Cv Ridge Rdg View Vw Loop Row Path Glen Gln Hollow Holw Manor Mnr Village Vlg Estates Ests"
    suffixList = street_suffixes.split(" ")
    streets = "(" + "|".join(suffixList) + ")"

    pattern = r"\d{1,6}.{1,20}" + streets + r"(,? ((Apt|Unit)?.{1,20} [A-Z]{2} )?\d{5})?"

    found = re.findall(pattern, fullText)
    addresses = [match[0] for match in found] if found else []

    redactedText = re.sub(pattern, tag, fullText)

    return redactedText, addresses  #