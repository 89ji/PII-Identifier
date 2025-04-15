from typing import List, Dict
from storage import *
import hashlib

def RestorePII(fullText :str, toRestore :str) -> str:
    if instance is not None:
        db = instance
    else:
        db = Database()

    # Processing the text to make it ignore whitespace changes
    fullText = fullText.replace("\n", "").replace(" ", "")

    # Hashing the text and saving it
    hasher = hashlib.sha256()
    hasher.update(fullText.encode())
    identifier = hasher.hexdigest()

    dict: Dict[str, List[str]] = db.retrieve_phi(identifier)

    for tag in dict:
        phiList = dict[tag]
        for phi in phiList:
            fullText = fullText.replace(tag, phi, 1)
        
    return fullText
