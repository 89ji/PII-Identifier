import re

def FindAddresses(fullText :str) -> str:
    tag = "*address*"
    street_suffixes = "Street St Avenue Ave Boulevard Blvd Road Rd Drive Dr Court Ct Lane Ln Place Pl Way Terrace Ter Circle Cir Trail Trl Cove Cv Ridge Rdg View Vw Loop Row Path Glen Gln Hollow Holw Manor Mnr Village Vlg Estates Ests"
    street_suffixes = street_suffixes.split(" ")
    streets = ""
    for street in street_suffixes:
        streets = streets + "|" + street
    streets = f"({streets[1::]})"

    pattern = "\d{1,6}.{1,20}" + streets + "(,? ((Apt|Unit).{1,20} [A-Z][A-Z] )?\d{5})?"
    return re.sub(pattern, tag, fullText)