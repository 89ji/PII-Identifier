# Device identifiers PM4437-BTX33457 & MAC indentifiers
import re

def remove_device_identifiers(text):
    DI_TOKEN = "*device identifiers*"

    di_finder = re.compile(r"\b([A-Z0-9]{6}-[A-Z0-9]{8}|\b(?:[A-Z0-9]{2}-){5}[A-Z0-9]{2})\b", re.IGNORECASE)
    
    found_di = di_finder.findall(text)
    replaced_text = di_finder.sub(DI_TOKEN,text)
    return (replaced_text, found_di)


 
