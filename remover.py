import re
from Regexs.address import *
from Regexs.email_re import *
from Regexs.phone import *
from Regexs.dob import *
from Regexs.ssn import *
from Regexs.nlpless_name import *
from Regexs.nlp_name import *
from Regexs.lab_results import *
from Regexs.allergies import allergies as RemoveAllergies
from Regexs.account import *
from Regexs.certificate import *
from Regexs.uniqueID import *
from Regexs.biometric import *
from Regexs.deviceidentifiers import *
from Regexs.url import *
from Regexs.ip_address import *
from dbstorage import *
from storer import Storer
from Regexs.labels import LabelwiseRemove

def Contains(original :list[str], target :str) -> bool:
    return target.lower() in original


db = instance

def RemovePII(fullText :str, phiToRemove :list[str], allergies :str) -> str:
    storer = Storer(db)

    phiToRemove = [item.lower() for item in phiToRemove]
    allergies = allergies.lower()

    if Contains(phiToRemove, "Fax numbers"):
        fullText, removed = LabelwiseRemove("*fax number*", fullText, r"(fax number|fax no\.?)")
        storer.StoreFax(removed)
        print(f"Faxes: {removed}")

    if Contains(phiToRemove, "Street Addresses"):
        fullText, removed = FindAddresses(fullText)
        storer.StoreAddresses(removed)
        print(f"Addresses: {removed}")

    if Contains(phiToRemove, "Dates of Birth"):
        fullText, removed = removeDOB(fullText)
        storer.StoreDOB(removed)
        print(f"DOBs: {removed}")

    if Contains(phiToRemove, "Social Security Numbers"):
        fullText, removed = removeSSN(fullText)
        storer.StoreSSN(removed)
        print(f"SSNs: {removed}")


    if Contains(phiToRemove, "Phone numbers"):
        fullText, removed = remove_phone_numbers(fullText)
        storer.StorePhone(removed)
        print(f"Phone numbers: {removed}")

    if Contains(phiToRemove, "Email addresses"):
        fullText, removed = remove_email_addresses(fullText)
        storer.StoreEmail(removed)
        print(f"Emails: {removed}")

    if Contains(phiToRemove, "Medicaid IDs"):
        fullText, removed = LabelwiseRemove(
            "*medicaid id*",
            fullText,
            r"medicaid",
            r"(\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4})",
        )
        storer.StoreMedicareID(removed)
        print(f"Medicaid IDs: {removed}")

    if Contains(phiToRemove, "Lab Results"):
        fullText, removed = removeLabResults(fullText)
        storer.StoreLabResults(removed)
        print(f"Lab results: {removed}")

    if Contains(phiToRemove, "Allergies"):
        fullText, removed = RemoveAllergies(fullText, allergies)
        storer.StoreAllergies(removed)
        print(f"Allergies: {removed}")

    if Contains(phiToRemove, "Hospital Names"):
        fullText, removed = LabelwiseRemove("*hospital*", fullText, r"hospital")
        storer.StoreHospitals(removed)
        print(f"Hospital names: {removed}")

    if Contains(phiToRemove, "Account Numbers"):
        fullText, removed = account(fullText)
        storer.StoreAccountNum(removed)
        print(f"Account numbers: {removed}")

    if Contains(phiToRemove, "Certificate/License Numbers"):
        fullText, removed_certifications, removed_licenses = certificate(fullText)
        storer.StoreCertNum(removed_certifications)
        storer.StoreLicenseNum(removed_licenses)
        print(f"Certificate numbers: {removed_certifications}")
        print(f"License numbers: {removed_licenses}")

    if Contains(phiToRemove, "Serial Numbers"):
        fullText, removed = LabelwiseRemove("*serial number*", fullText, r"serial")
        storer.StoreSerial(removed)
        print(f"Serial numbers: {removed}")

    if Contains(phiToRemove, "Medical record numbers"):
        fullText, removed = LabelwiseRemove(
            "*medical record number*", fullText, r"medical record number"
        )
        storer.StoreMedicalRecNum(removed)
        print(f"Medical record numbers: {removed}")

    if Contains(phiToRemove, "Health Plan Beneficiary Numbers"):
        fullText, removed = LabelwiseRemove(
            "*health plan beneficiary number*",
            fullText,
            r"health plan beneficiary number",
        )
        storer.StoreHealthPlanBeneficiaryNum(removed)
        print(f"Beneficiary numbers: {removed}")

    if Contains(phiToRemove, "Unique identifying numbers/characteristics/codes"):
        fullText, removed = removeUniqueID(fullText)
        storer.StoreUniqueIdNums(removed)
        print(f"Unique IDs: {removed}")

    if Contains(phiToRemove, "Device Identifiers"):
        fullText, removed = remove_device_identifiers(fullText)
        storer.StoreDeviceID(removed)
        print(f"Device identifiers: {removed}")

    if Contains(phiToRemove, "URLs"):
        fullText, removed = remove_urls(fullText)
        storer.StoreURL(removed)
        print(f"Urls: {removed}")

    if Contains(phiToRemove, "IP Addresses"):
        fullText, removed = remove_ipaddress(fullText)
        storer.StoreIPs(removed)
        print(f"IP addresses: {removed}")

    re_name = Contains(phiToRemove, "Names")
    re_provider = Contains(phiToRemove, "Provider Names")
    re_social_worker = Contains(phiToRemove, "Social Worker Names")
    if re_name or re_provider or re_social_worker:
        fullText, removed_names, removed_providers, removed_social_workers = remove_names(fullText, re_name, re_provider, re_social_worker)
        storer.StoreNames(removed_names)
        storer.StoreProviders(removed_providers)
        storer.StoreSW(removed_social_workers)
        print(f"Names removed: {removed_names}")
        print(f"Social Workers removed: {removed_social_workers}")
        print(f"Providers removed: {removed_providers}")

    if Contains(phiToRemove, "Biometric Identifiers"):
        fullText, removed = bio_identifiers(fullText)
        storer.StoreBiomentricIDs(removed)
        print(f"Biometric IDs: {removed}")

    storer.Save(fullText)

    return fullText
