import re

def remove_phone_numbers(text):
    phone_tag = "*phone*"

    phone_finder = re.compile(r"([pP]hone|[fF]ax)(?: [nN]umbers?)?:\s?((?:\+\d{1,2}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})", re.IGNORECASE)
    match = phone_finder.findall(text)

    if len(match) > 0:
        for phone in match:
            phone_num = phone[1].strip()
            text = text.replace(phone_num, phone_tag)

    return text