import re

def account(fullText :str) -> str:
    tag = "*account_num*"
    
    account_finder = re.compile(r"Account(?: number)?:\s?((\d|\*){4}(\s|-)?(\d|\*){4}(\s|-)?(\d|\*){4}(\s|-)?(\d|\*){4})", re.IGNORECASE)
    matches = []
    
    for match in account_finder.finditer(fullText):
        matches.append(match.group(1))
        fullText = fullText.replace(match.group(1), tag, 1)

    return fullText, matches