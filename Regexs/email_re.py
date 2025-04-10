import re

EMAIL_ADDRESS_TOKEN = '*email*'

def remove_email_addresses(text):
    standard_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    matches = []
    substituted_text = text

    for match in standard_pattern.finditer(text):
        matches.append(match.group())
        substituted_text = substituted_text.replace(match.group(), EMAIL_ADDRESS_TOKEN, 1)

    return substituted_text, matches