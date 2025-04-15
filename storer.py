from typing import List, Dict
from storage import Database
import hashlib

def EncodeAll(inp :List[str]) -> List[bytes]: 
    out: List[bytes] = []
    for item in inp:
        out.append(item.encode())
    return out

class Storer:
    __db = None
    __dict: Dict[str, List[bytes]] = {}
    __identifier = None

    def __init__(self, db :Database):
        self.__db = db

    def StoreNames(self, items :List[str]):
        self.__dict["*fax number*"] = EncodeAll(items)

    def StoreProviders(self, items :List[str]):
        self.__dict["*provider*"] = EncodeAll(items)

    def StoreSW(self, items :List[str]):
        self.__dict["*social_worker*"] = EncodeAll(items)

    def StoreAddresses(self, items :List[str]):
        self.__dict["*address*"] = EncodeAll(items)

    def StoreDOB(self, items :List[str]):
        self.__dict["*dob*"] = EncodeAll(items)

    def StorePhone(self, items :List[str]):
        self.__dict["*phone*"] = EncodeAll(items)

    def StoreFax(self, items :List[str]):
        self.__dict["*fax number*"] = EncodeAll(items)

    def StoreEmail(self, items :List[str]):
        self.__dict["*email*"] = EncodeAll(items)

    def StoreSSN(self, items :List[str]):
        self.__dict["*ssn*"] = EncodeAll(items)

    def StoreMedicalRecNum(self, items :List[str]):
        self.__dict["*medical record number*"] = EncodeAll(items)

    def StoreHealthPlanBeneficiaryNum(self, items :List[str]):
        self.__dict["*health plan beneficiary number*"] = EncodeAll(items)

    def StoreMedicareID(self, items :List[str]):
        self.__dict["*medicaid id*"] = EncodeAll(items)

    def StoreAccountNum(self, items :List[str]):
        self.__dict["*account_num*"] = EncodeAll(items)

    def StoreCertNum(self, items :List[str]):
        self.__dict["*certificate_num*"] = EncodeAll(items)

    def StoreSerial(self, items :List[str]):
        self.__dict["*serial number*"] = EncodeAll(items)

    def StoreDeviceID(self, items :List[str]):
        self.__dict["*device identifiers*"] = EncodeAll(items)

    def StoreURL(self, items :List[str]):
        self.__dict["*url*"] = EncodeAll(items)

    def StoreIPs(self, items :List[str]):
        self.__dict["*ip*"] = EncodeAll(items)

    def StoreBiomentricIDs(self, items :List[str]):
        self.__dict["*biometric* "] = EncodeAll(items)

    def StoreUniqueIdNums(self, items :List[str]):
        self.__dict["*Unique Code*"] = EncodeAll(items)

    def StoreLabResults(self, items :List[str]):
        self.__dict["*lab results*"] = EncodeAll(items)

    def StoreHospitals(self, items :List[str]):
        self.__dict["*hospital*"] = EncodeAll(items)

    def Save(self, fullText: str):
        # Processing the text to make it ignore whitespace changes
        fullText = fullText.replace("\n", "").replace(" ", "")

        # Hashing the text and saving it
        hasher = hashlib.sha256()
        hasher.update(fullText.encode())
        self.__identifier = hasher.hexdigest()

        # Sending the processed stuff to the storage module
        self.__db.store_phi(self.__identifier, self.__dict)
