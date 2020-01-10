#!/usr/bin/env python
# encoding: utf-8
from IPy import IP
import requests
 
#批量Get_Flag
 
 
# IP地址处理，调用方法IPs("192.168.10.0/24")或IPs("192.168.10.0.-20"),返回一个数组
def IPs(ip):
    IPS = []
    s1 = "/"
    s2 = "-"
    if ip.find(s1) > 0:
        ip1 = IP(ip)
        for i in ip1:
            IPS.append(i)
    elif (str(ip).find(s2)) > 0:
        for i in range(int(str(ip)[str(ip).rfind('.') + 1:str(ip).rfind('-')]),
                       int(str(ip)[str(ip).rfind('-') + 1:]) + 1):
            IPS.append(str(ip)[:str(ip).rfind('.') + 1] + str(i))
    return IPS
# for i in IPs("192.168.1.0-12"):
#     print(i)
headers = {
    'Accept': '*/*',
    'Referer': 'https://www.baidu.com',
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.1; ',
    'Cache-Control': 'no-cache'
}
 
 
def get_Requests(ip, payload):
    url = 'http://' + str(ip) + '/' + payload
    try:
        get_Flag = requests.get(url, headers=headers, timeout=3)
        return get_Flag.text
    except requests.exceptions.ConnectTimeout:
        print("Connect Timeout")
 
 
def post_Requests(ip, payload, post_data):
    url = 'http://' + ip + '/' + payload
    try:
        get_Flag = requests.post(url,
                                 headers=headers,
                                 data=post_data,
                                 timeout=3)
        return get_Flag.text
    except requests.exceptions.ConnectTimeout:
        print("Connect Timeout")
 
 
def main():
    print('#get_Flag V1.0')
    ip = input('Please enter the IP range >>>')
    num = int(input('Please select request method 1 = get 2 = post >>>'))
    payload = input('Please enter the payload')
    if num == 2:
        post_data = input('Please enter post_data')
        for i in IPs(ip):
            print(post_Requests(i, payload, post_data))
    else:
        for i in IPs(ip):
            print(get_Requests(i, payload))
 
 
if __name__ == '__main__':
    main()