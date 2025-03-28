import re

def FindNames(fullText: str) -> str:
    tag = "*name*"
    foundNames = []

    # Finding names via "Patient: "
    patientFinder = re.compile(r"Patient: (([A-Z][a-z]* ?)*)")
    results = re.findall(patientFinder, fullText)
    for result in results:
        if len(result) > 1:
            foundNames.append(result[0])

    # Finding names via Mr/Mrs
    titleFinder = re.compile(r"((Mr|Mrs|Miss|Dr)\.) (([A-Z][a-z]* ?)*)")
    results = re.findall(titleFinder, fullText)
    for result in results:
        if result[0] != "Dr.":
            if len(result) > 2:
                foundNames.append(f"{result[0]} {result[2][:-1]}")

    for name in foundNames:
        fullText = fullText.replace(name, tag)

    return fullText
