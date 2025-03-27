import re
from Regexs.address import *
from Regexs.email_re import *
from Regexs.phone import *
from Regexs.dob import *
from Regexs.ssn import *
from Regexs.nlpless_name import *
from Regexs.nlp_name import *
from Regexs.hospital import *

def RemovePII(fullText :str, re_name :bool = True, re_address :bool = True, re_dob :bool = True, re_ssn :bool = True, 
              re_phone :bool = True, re_email :bool = True, re_provider :bool = True, re_social_worker :bool = True,
              re_hospital :bool = True) -> str:
    # Going through the PII types
    if re_name or re_provider or re_social_worker:
        fullText = remove_names(fullText, re_name, re_provider, re_social_worker)

    if re_address:
        fullText = FindAddresses(fullText)

    if re_dob:
        fullText = removeDOB(fullText)

    if re_ssn:
        fullText = removeSSN(fullText)

    if re_phone:
        fullText = remove_phone_numbers(fullText)

    if re_email:
        fullText = remove_email_addresses(fullText)

    if re_hospital:
        fullText = FindHospitals(fullText)

    # Additional PII types can be added in the same manner

    return fullText
