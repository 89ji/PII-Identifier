import re
import json
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
from Regexs.account import *
from Regexs.labels import LabelwiseRemove

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createDB import Base, PII, Files

def stringify(value):
    if isinstance(value, list):
        return ', '.join(str(v) for v in value)
    if isinstance(value, dict):
        return json.dumps(value)
    return value


def Contains(original :list[str], target :str) -> bool:
    return target in original

def RemovePII(fullText :str, phiToRemove :list[str], allergies :str) -> str:

    # starting connection to database

    engine = create_engine('sqlite:///PII.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # initialize these to keep

    account                = None
    address                = None
    allergies              = None
    biometric              = None
    certificate            = None
    deviceidentifiers      = None
    dob                    = None
    emailre                = None
    fax                    = None
    hospital               = None
    ipaddress              = None
    labresults             = None
    labels                 = None
    medicaid               = None
    medicalrecordnumbers   = None
    removed_names          = None
    removed_providers      = None
    removed_social_workers = None
    phone                  = None
    planBeneficiaryNumber  = None
    serial                 = None
    ssn                    = None
    uniqueid               = None
    url                    = None

    if Contains(phiToRemove, "Fax numbers"):
        fullText, fax = LabelwiseRemove("*fax number*", fullText, r"(fax number|fax no\.?)")
        print("Faxes removed")

    if Contains(phiToRemove, "Street Addresses"):
        fullText, address = FindAddresses(fullText)
        print("Address removed")

    if Contains(phiToRemove, "Dates of Birth"):
        fullText, dob = removeDOB(fullText)
        print("DOB removed")

    if Contains(phiToRemove, "Social Security Numbers"):
        fullText, ssn = removeSSN(fullText)
        print("SSN removed")

    if Contains(phiToRemove, "Phone numbers"):
        fullText, phone = remove_phone_numbers(fullText)
        print("Phone removed")

    if Contains(phiToRemove, "Email addresses"):
        fullText, emailre = remove_email_addresses(fullText)
        print("Email removed")

    if Contains(phiToRemove, "Medicaid IDs"):
        fullText, medicaid = LabelwiseRemove(
            "*medicaid id*",
            fullText,
            r"medicaid",
            r"(\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4})",
        )
        print("Medicaid removed")

    if Contains(phiToRemove, "Lab Results"):
        fullText, labresults = removeLabResults(fullText)
        print("Lab results removed")

    if Contains(phiToRemove, "Allergies"):
        fullText, allergies = RemoveAllergies(fullText, allergies)
        print("Allergies removed")

    if Contains(phiToRemove, "Hospital Names"):
        fullText, hostpial = LabelwiseRemove("*hospital*", fullText, r"hospital")
        print("Hospital name removed")

    if Contains(phiToRemove, "Account Numbers"):
        fullText, account = removeAccount(fullText)
        print("Account removed")

    if Contains(phiToRemove, "Certificate/License Numbers"):
        fullText, certificate = removeCertificate(fullText)
        print("Certificate removed")

    if Contains(phiToRemove, "Serial Numbers"):
        fullText, serial = LabelwiseRemove("*serial number*", fullText, r"serial")
        print("Serial number removed")

    if Contains(phiToRemove, "Medical record numbers"):
        fullText, medicalrecordnumbers = LabelwiseRemove(
            "*medical record number*", fullText, r"medical record number"
        )
        print("Medical record numbers removed")

    if Contains(phiToRemove, "Health Plan Beneficiary Numbers"):
        fullText, planBeneficiaryNumber = LabelwiseRemove(
            "*health plan beneficiary number*",
            fullText,
            r"health plan beneficiary number",
        )
        print("Beneficiary numbers removed")

    if Contains(phiToRemove, "Unique identifying numbers/characteristics/codes"):
        fullText, uniqueid = removeUniqueID(fullText)
        print("Unique IDs removed")

    if Contains(phiToRemove, "Device Identifiers"):
        fullText, deviceidentifiers = remove_device_identifiers(fullText)
        print("Device identifiers removed")

    if Contains(phiToRemove, "URLs"):
        fullText, url = remove_urls(fullText)
        print("Urls removed")

    if Contains(phiToRemove, "IP Addresses"):
        fullText, ipaddress = remove_ipaddress(fullText)
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
        fullText, biometric = removeBioidentifiers(fullText)
        print("Biometric removed")

    # Additional PII types can be added in the same manner

    # final edits to vars
    account                = stringify(account               )
    address                = stringify(address               )
    allergies              = stringify(allergies             )
    biometric              = stringify(biometric             )
    certificate            = stringify(certificate           )
    deviceidentifiers      = stringify(deviceidentifiers     )
    dob                    = stringify(dob                   )
    emailre                = stringify(emailre               )
    fax                    = stringify(fax                   )
    hospital               = stringify(hospital              )
    ipaddress              = stringify(ipaddress             )
    labresults             = stringify(labresults            )
    labels                 = stringify(labels                )
    medicaid               = stringify(medicaid              )
    medicalrecordnumbers   = stringify(medicalrecordnumbers  )
    removed_names          = stringify(removed_names         )
    removed_providers      = stringify(removed_providers     )
    removed_social_workers = stringify(removed_social_workers)
    phone                  = stringify(phone                 )
    planBeneficiaryNumber  = stringify(planBeneficiaryNumber )
    serial                 = stringify(serial                )
    ssn                    = stringify(ssn                   )
    uniqueid               = stringify(uniqueid              )
    url                    = stringify(url                   )

    new_pii = PII(
        account = account,
        address = address,
        allergies = allergies,
        biometric = biometric,
        certificate = certificate,
        deviceidentifiers = deviceidentifiers,
        dob = dob,
        emailre = emailre,
        fax = fax,
        hospital = hospital,
        ipaddress = ipaddress,
        labresults = labresults,
        labels = labels,
        medicaid = medicaid,
        medicalrecordnumbers = medicalrecordnumbers,
        name = removed_names,
        socialworkername = removed_providers,
        providername = removed_social_workers,
        phone = phone,
        planBeneficiaryNumber = planBeneficiaryNumber,
        serial = serial,
        ssn = ssn,
        uniqueid = uniqueid,
        url = url
    )

    session.add(new_pii)
    session.flush()

    new_file = Files(
        author      ="None",
        no_pii_text = fullText,
        pii_id= new_pii.id
    )

    session.add(new_file)
    session.commit()


    return fullText
