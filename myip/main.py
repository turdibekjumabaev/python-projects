import os, requests

iprequest = requests.get("https://api.myip.com").json()
ip = iprequest["ip"] 
country = iprequest["country"] 
cc = iprequest["cc"] 

print(f"[MyIP] User: {os.getlogin()}")
print(f"[MyIP] IP: {ip}")
print(f"[MyIP] Country: {country}")
print(f"[MyIP] Country Code: {cc}")