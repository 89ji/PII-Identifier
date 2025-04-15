import re
from typing import Tuple, List

def FindAddresses(fullText :str) -> Tuple[str, List[str]]:
    tag = "*address*"
    street_suffixes = "Street St Avenue Ave Boulevard Blvd Road Rd Drive Dr Court Ct Lane Ln Place Pl Way Terrace Ter Circle Cir Trail Trl Cove Cv Ridge Rdg View Vw Loop Row Path Glen Gln Hollow Holw Manor Mnr Village Vlg Estates Ests"
    suffixList = street_suffixes.split(" ")
    streets = ""
    for street in suffixList:
        streets = streets + "|" + street
    streets = f"({streets[1::]})"

    pattern = "\d{1,6}.{1,20}" + streets + "(,? ((Apt|Unit)?.{1,20} [A-Z][A-Z] )?\d{5})?"

    found = re.finditer(pattern, fullText)
    matches = []
    for find in found:
        matches.append(find.group())

    fullText = re.sub(pattern, tag, fullText)
    return (fullText, matches)