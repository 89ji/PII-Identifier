import re

def removeAccount(fullText: str):
    tag = "*account_num*"
    removed = []

    account_finder = re.compile(
        r"Account(?: number)?:\s?((\d|\*){4}(\s|-)?(\d|\*){4}(\s|-)?(\d|\*){4}(\s|-)?(\d|\*){4})",
        re.IGNORECASE
    )
    
    matches = account_finder.findall(fullText)
    
    if matches:
        for match in matches:
            account_num = match[0].strip()
            removed.append(account_num)
            fullText = fullText.replace(account_num, tag)

    return fullText, removed