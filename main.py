import sys

from numpy import full
from Regexs.address import *
from Regexs.email import *
from Regexs.phone import *
from Regexs.dob import *
from Regexs.ssn import *

import re

def main():
    if len(sys.argv) < 2:
        print("Usage:\t1st argument: Input file path\n\t2nd argument: PII to search for. Will default to all without input [optional]\n\t3rd argument: Output file path [optional]")
        exit(-1)

    # Reading the input filename
    targetFile = sys.argv[1]

    # Reading the PII types filename
    piiFile = ""
    if len(sys.argv) > 2:
        piiFile = sys.argv[2]

    destFile = ""
    if len(sys.argv) > 3:
        destFile = sys.argv[3]
    else:
        destFile = "".join(targetFile.split(".")[:-1]) + " sans PII.txt"
    
    # Reading from the input file
    try:
        with open(targetFile) as target:
            fullText = target.read()
    except:
        print("Unable to read target file")
        exit(-1)

    # Reading from the PII types file
    if piiFile == "":
        Pii = "all"
    else:
        try:
            with open(piiFile) as target:
                Pii = target.read()
        except:
            print("Unable to read PII file")
            exit(-1)


    # Going through the PII types
    if re.search("name", Pii, re.IGNORECASE) is not None or Pii == "all":
        pass

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


    # Writing the target file
    with open(destFile, "w") as dest:
        dest.write(fullText)


# Standard pythonic boilerplate
if __name__ == "__main__":
    main()