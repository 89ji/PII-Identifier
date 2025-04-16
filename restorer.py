from typing import List, Dict
from storage import *
import hashlib


tag2name = {
    "*name*": "Names",
    "*provider*": "Provider Names",
    "*social_worker*": "Social Worker Names",
    "*address*": "Street Addresses",
    "*dob*": "Dates of Birth",
    "*phone*": "Phone numbers",
    "*fax number*": "Fax numbers",
    "*email*": "Email addresses",
    "*ssn*": "Social Security Numbers",
    "*medical record number*": "Medical record numbers",
    "*health plan beneficiary number*": "Health Plan Beneficiary Numbers",
    "*medicaid id*": "Medicaid IDs",
    "*account_num*": "Account Numbers",
    "*certificate_num*": "Certificate/License Numbers",
    "*serial number*": "Serial Numbers",
    "*device identifiers*": "Device Identifiers",
    "*url*": "URLs",
    "*ip*": "IP Addresses",
    "*biometric*": "Biometric Identifiers",
    "*uniqueID*": "Unique identifying numbers/characteristics/codes",
    "*lab results*": "Lab Results",
    "*hospital*": "Hospital Names",
    "*license_num*": "Certificate/License Numbers"
}


ERROR_MSG = '''The provided text was not found in the database!
Make sure it was processed with the remover first.
Do not modify any non-whitespace characters in the text.
'''

def RestorePII(fullText :str, toRestore :str) -> str:
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
        phiName = tag2name[tag]
        if phiName in toRestore:
            phiList = dict[tag]
            for phi in phiList:
                fullText = fullText.replace(tag, phi.decode(), 1)
        
    return fullText
