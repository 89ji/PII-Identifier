import re
from Regexs.address import *
from Regexs.email import *
from Regexs.phone import *
from Regexs.dob import *
from Regexs.ssn import *
from Regexs.nlpless_name import *

def RemovePII(fullText :str, Pii :str = "all") -> str:
    # Going through the PII types
    if re.search("name", Pii, re.IGNORECASE) is not None or Pii == "all":
        fullText = FindNames(fullText)

    if re.search("address", Pii, re.IGNORECASE) is not None or Pii == "all":
        fullText = FindAddresses(fullText)

    if re.search("date of birth", Pii, re.IGNORECASE) is not None or Pii == "all":
        fullText = removeDOB(fullText)

    if re.search("(ssn|social security)", Pii, re.IGNORECASE) is not None or Pii == "all":
        fullText = removeSSN(fullText)

    if re.search("phone", Pii, re.IGNORECASE) is not None or Pii == "all":
        fullText = remove_phone_numbers(fullText)

    if re.search("e.mail", Pii, re.IGNORECASE) is not None or Pii == "all":
        fullText = remove_email_addresses(fullText)

    # Additional PII types can be added in the same manner

    return fullText
