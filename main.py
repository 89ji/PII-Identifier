#!/usr/bin/env python3
import sys
from remover import RemovePII
from web import StartWebserver

def main():
    if len(sys.argv) < 2:
        print('''
Usage:
    1st argument: Input file path
    2nd argument: PII to search for. Will default to all without input [optional]
    3rd argument: Output file path [optional]
              
    or use -w to start the web interface'''
              )
        
        exit(-1)

    if "-w" in sys.argv:
        StartWebserver()

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


    fullText = RemovePII(fullText, Pii)


    # Writing the target file
    with open(destFile, "w") as dest:
        dest.write(fullText)


# Standard pythonic boilerplate
if __name__ == "__main__":
    main()