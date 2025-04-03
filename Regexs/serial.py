import re

def serial(fullText: str) -> str:
    tag = "*serial_num*"

    serial_finder = re.compile(r"[sS]erial(?: [nN]umbers?)?:\s?([A-Z]\d{4}-?\d{7})")
    match = serial_finder.findall(fullText)

    if len(match) > 0:
        for serial in match:
            serial_num = serial.strip()
            fullText = fullText.replace(serial_num, tag)

    return fullText