import re

PHONE_NUMBER_TOKEN = '*phone*'

def remove_phone_numbers(text):
    standard_pattern = re.compile(r'(?:\+\d{1,2}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    return standard_pattern.sub(PHONE_NUMBER_TOKEN, text)

if __name__ == '__main__':
    test_text = "Call me at +1 (123) 456-7890 or 987-654-3210. This is not a phone number: 123-45-6789."
    print(remove_phone_numbers(test_text))