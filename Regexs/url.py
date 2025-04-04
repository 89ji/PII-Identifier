# Web Universal Resource Locators (URLs)
import re

URL_TOKEN = '*url*'

def remove_urls(text):
    url_finder = re.compile(r"\b(www.)([a-z0-9]+)(.com|.org|.net|.edu|.gov|.mil|.io)\b")
    return url_finder.sub(URL_TOKEN, text)
    
