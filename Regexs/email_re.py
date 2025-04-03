import re

EMAIL_ADDRESS_TOKEN = '*email*'

def remove_email_addresses(text):
    standard_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return standard_pattern.sub(EMAIL_ADDRESS_TOKEN, text)