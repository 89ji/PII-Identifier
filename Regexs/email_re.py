import re

EMAIL_ADDRESS_TOKEN = '*email*'

def remove_email_addresses(text):
    standard_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return standard_pattern.sub(EMAIL_ADDRESS_TOKEN, text)

if __name__ == '__main__':
    test_text = "Contact us at testemail@gmail.com that is our email address. This is not an email: testemail@com."
    print(remove_email_addresses(test_text))