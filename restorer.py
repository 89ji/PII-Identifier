from typing import List, Dict
from storage import *
import hashlib

ERROR_MSG = '''The provided text was not found in the database!
Make sure it was processed with the remover first.
Do not modify any non-whitespace characters in the text.
'''

def RestorePII(fullText :str) -> str:
    db = instance


    # Processing the text to make it ignore whitespace changes
    strippedText = fullText.replace("\n", "").replace(" ", "")

    # Hashing the text and saving it
    hasher = hashlib.sha256()
    hasher.update(strippedText.encode())
    identifier = hasher.hexdigest()

    try:
        dict: Dict[str, List[bytes]] = db.retrieve_phi(identifier)
    except:
        return ERROR_MSG

    for tag in dict:
        phiList = dict[tag]
        for phi in phiList:
            fullText = fullText.replace(tag, phi.decode(), 1)
        
    return fullText
