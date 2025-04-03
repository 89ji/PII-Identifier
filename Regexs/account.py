import re

def account(fullText :str) -> str:
    tag = "*account_num*"
    
    account_finder = re.compile(r"Account(?: number)?:\s?((\d|\*){4}(\s|-)?(\d|\*){4}(\s|-)?(\d|\*){4}(\s|-)?(\d|\*){4})", re.IGNORECASE)
    match = account_finder.findall(fullText)
    
    if len(match) > 0:
        print(f"Account match: {match}")
        for account in match:
            account_num = account[0].strip()
            fullText = fullText.replace(account_num, tag)

    return fullText