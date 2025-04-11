# IP address IPv4 and IPv6
import re

IP_TOKEN = '*ip address*'

def remove_ipaddress(text):
    ip_finder = re.compile(r"\b(((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])) | ([0-9a-z]{4}:){7}[0-9a-z]{4}\b")
    return ip_finder.sub(IP_TOKEN, text)
    
