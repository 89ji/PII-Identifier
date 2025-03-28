import re

# detect "Allergies:"
# check each line after for leading "-" and replace with *allergy*
# if no leading "-" then return

def allergies(lines):
    sleeperAgent = False
    allergiesLines = []
    
    for line in lines:
        if re.search(r"\bAllergies:\b", line):
            sleeperAgent = True
        elif sleeperAgent and line.startswith("-"):
            line = "*allergy*"
        else:
            sleepAgent = False
            
        allergiesLines.append(line)
        
    return allergiesLines
    
