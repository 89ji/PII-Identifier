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
from storage import Database
from Regexs.labels import LabelwiseRemove

def Contains(original :list[str], target :str) -> bool:
    return target in original

def RemovePII(fullText :str, phiToRemove :list[str], allergies :str) -> str:
    if Contains(phiToRemove, "Fax numbers"):
        fullText, removed = LabelwiseRemove("*fax number*", fullText, r"(fax number|fax no\.?)")
        print("Faxes removed")

    if Contains(phiToRemove, "Street Addresses"):
        fullText = FindAddresses(fullText)
        print("Address removed")

    if Contains(phiToRemove, "Dates of Birth"):
        fullText = removeDOB(fullText)
        print("DOB removed")

    if Contains(phiToRemove, "Social Security Numbers"):
        fullText = removeSSN(fullText)
        print("SSN removed")

    if Contains(phiToRemove, "Phone numbers"):
        fullText, matches = remove_phone_numbers(fullText)
        print("Phone removed")

    if Contains(phiToRemove, "Email addresses"):
        fullText, matches = remove_email_addresses(fullText)
        print("Email removed")

    if Contains(phiToRemove, "Medicaid IDs"):
        fullText, removed = LabelwiseRemove(
            "*medicaid id*",
            fullText,
            r"medicaid",
            r"(\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4})",
        )
        print("Medicaid removed")

    if Contains(phiToRemove, "Lab Results"):
        fullText = removeLabResults(fullText)
        print("Lab results removed")

    if Contains(phiToRemove, "Allergies"):
        fullText = RemoveAllergies(fullText, allergies)
        print("Allergies removed")

    if Contains(phiToRemove, "Hospital Names"):
        fullText, removed = LabelwiseRemove("*hospital*", fullText, r"hospital")
        print("Hospital name removed")

    if Contains(phiToRemove, "Account Numbers"):
        fullText = account(fullText)
        print("Account removed")

    if Contains(phiToRemove, "Certificate/License Numbers"):
        fullText = certificate(fullText)
        print("Certificate removed")

    if Contains(phiToRemove, "Serial Numbers"):
        fullText, removed = LabelwiseRemove("*serial number*", fullText, r"serial")
        print("Serial number removed")

    if Contains(phiToRemove, "Medical record numbers"):
        fullText, removed = LabelwiseRemove(
            "*medical record number*", fullText, r"medical record number"
        )
        print("Medical record numbers removed")

    if Contains(phiToRemove, "Health Plan Beneficiary Numbers"):
        fullText, removed = LabelwiseRemove(
            "*health plan beneficiary number*",
            fullText,
            r"health plan beneficiary number",
        )
        print("Beneficiary numbers removed")

    if Contains(phiToRemove, "Unique identifying numbers/characteristics/codes"):
        fullText = removeUniqueID(fullText)
        print("Unique IDs removed")

    if Contains(phiToRemove, "Device Identifiers"):
        fullText = remove_device_identifiers(fullText)
        print("Device identifiers removed")

    if Contains(phiToRemove, "URLs"):
        fullText = remove_urls(fullText)
        print("Urls removed")

    if Contains(phiToRemove, "IP Addresses"):
        fullText = remove_ipaddress(fullText)
        print("IP addresses removed")

    re_name = Contains(phiToRemove, "Names")
    re_provider = Contains(phiToRemove, "Provider Names")
    re_social_worker = Contains(phiToRemove, "Social Worker Names")
    if re_name or re_provider or re_social_worker:
        fullText, removed_names, removed_providers, removed_social_workers = remove_names(fullText, re_name, re_provider, re_social_worker)
        print(f"Names removed: {removed_names}")
        print(f"Social Workers removed: {removed_social_workers}")
        print(f"Providers removed: {removed_providers}")
        print("Name removed")

    if Contains(phiToRemove, "Biometric Identifiers"):
        fullText = bio_identifiers(fullText)
        print("Biometric removed")

    # Additional PII types can be added in the same manner

    return fullText
