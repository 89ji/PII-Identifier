Usage:
  Run via main.py from the command line. Use the -w argument to start the web interface. Otherwise supply the input filename, PII list filename, and output filename. The last two arguments are optional.

Installation:
  1. Create a python virtual environment and activate it. Make sure it doesn't get included in your git commits. Or else...
  2. Install the items in requirements.txt
  3. Download /ML_Approach/name_classifier.pth from the repo. The file gets munted when downloaded via git for some reason.
  4. Run python3 -m spacy download en_core_web_trf