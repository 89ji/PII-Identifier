import re
from Regexs.address import *
from Regexs.email_re import *
from Regexs.medicalRecordNumbers import *
from Regexs.phone import *
from Regexs.dob import *
from Regexs.planBeneficiaryNumber import *
from Regexs.ssn import *
from Regexs.nlpless_name import *
from Regexs.nlp_name import *
from Regexs.hospital import *
from Regexs.lab_results import *
from Regexs.medicaid import *
from Regexs.allergies import *
from Regexs.account import *
from Regexs.certificate import *
from Regexs.serial import *
from Regexs.fax import *
from Regexs.uniqueID import *
from Regexs.biometric import *
from Regexs.deviceidentifiers import * 
from Regexs.url import *
from Regexs.ipaddress import *

def RemovePII(
    fullText: str,
    re_name: bool = True,
    re_address: bool = True,
    re_dob: bool = True,
    re_ssn: bool = True,
    re_phone: bool = True,
    re_email: bool = True,
    re_provider: bool = True,
    re_social_worker: bool = True,
    re_medicaid: bool = True,
    re_lab_results: bool = True,
    re_allergies: bool = True,
    allergies_input: str = None,
    re_hospital: bool = True,
    re_account: bool = True,
    re_certificate: bool = True,
    re_serial: bool = True,
    re_fax: bool = True,
    re_med_rec_num: bool = True,
    re_beneficiary_num: bool = True,
    re_biometric: bool = True,
    re_uniqueID: bool = True,
    re_device_identifiers: bool = True,
    re_url: bool = True,
    re_ipaddress: bool = True,
) -> str:
    if re_fax:
        fullText = FindFax(fullText)
        print("Faxes removed")

    if re_address:
        fullText = FindAddresses(fullText)
        print("Address removed")

    if re_dob:
        fullText = removeDOB(fullText)
        print("DOB removed")

    if re_ssn:
        fullText = removeSSN(fullText)
        print("SSN removed")

    if re_phone:
        fullText = remove_phone_numbers(fullText)
        print("Phone removed")

    if re_email:
        fullText = remove_email_addresses(fullText)
        print("Email removed")

    if re_medicaid:
        fullText = FindMedicaid(fullText)
        print("Medicaid removed")

    if re_lab_results:
        fullText = removeLabResults(fullText)
        print("Lab results removed")

    if re_allergies:
        fullText = allergies(fullText, allergies_input)
        print("Allergies removed")

    if re_hospital:
        fullText = FindHospitals(fullText)
        print("Hospital name removed")

    if re_account:
        fullText = account(fullText)
        print("Account removed")

    if re_certificate:
        fullText = certificate(fullText)
        print("Certificate removed")

    if re_serial:
        fullText = serial(fullText)
        print("Serial number removed")

    if re_med_rec_num:
        fullText = FindRecordNumbers(fullText)
        print("Medical record numbers removed")

    if re_beneficiary_num:
        fullText = FindBeneficiary(fullText)
        print("Beneficiary numbers removed")

    if re_uniqueID:
        fullText = removeUniqueID(fullText)
        print("Unique IDs removed")

    if re_device_identifiers:
        fullText = remove_device_identifiers(fullText)
        print("Device identifiers removed")
        
    if re_url:
        fullText = remove_urls(fullText)
        print("Urls removed")

    if re_ipaddress:
        fullText = remove_ipaddress(fullText)
        print("IP addresses remove")
    

    # Going through the PII types
    if re_name or re_provider or re_social_worker:
        fullText = remove_names(fullText, re_name, re_provider, re_social_worker)
        print("Name removed")

    if re_biometric:
        fullText = bio_identifiers(fullText)
        print("Biometric removed")

    if re_ipaddress:
        fullText = remove_ipaddress(fullText)
        print("IP address removed")

    # Additional PII types can be added in the same manner

    return fullText
