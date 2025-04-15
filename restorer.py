from typing import List, Dict
from storage import *
import hashlib

def RestorePII(fullText :str, toRestore :str) -> str:
    db = instance


    # Processing the text to make it ignore whitespace changes
    strippedText = fullText.replace("\n", "").replace(" ", "")

    # Hashing the text and saving it
    hasher = hashlib.sha256()
    hasher.update(strippedText.encode())
    identifier = hasher.hexdigest()

    dict: Dict[str, List[bytes]] = db.retrieve_phi(identifier)

    for tag in dict:
        phiList = dict[tag]
        for phi in phiList:
            fullText = fullText.replace(tag, phi.decode(), 1)
        
    return fullText
