# IP address IPv4 and IPv6
import re

IP_TOKEN = '*ip address*'

def remove_ipaddress(text):
    ip_finder = re.compile(r"\b(?:(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)|(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4})\b", re.IGNORECASE)
    
    found_ip = ip_finder.findall(text)
    replaced_text = ip_finder.sub(IP_TOKEN, text)
    return (replaced_text, found_ip)
    
