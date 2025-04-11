# Web Universal Resource Locators (URLs)
import re

URL_TOKEN = '*url*'

def remove_urls(text):
    url_finder = re.compile(r"\b(www\.[a-z0-9-]+\.(?:com|org|net|edu|gov|mil|io))\b", re.IGNORECASE)
    
    found_url = url_finder.findall(text)
    replaced_text = url_finder.sub(URL_TOKEN, text)
    return (replaced_text, found_url)
    
    
