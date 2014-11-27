#coding:utf-8
import ftplib
import codecs
import re
ftp=ftplib.FTP()
ftp.connect('ftp地址')
ftp.login('用户名','密码')
stack=['/']
for heu in ftp.nlst():
    heu="/%s" % heu
    stack.append(heu)
f=file('ftp.txt','w')
#print stack
##############################################
#遍历搜索
#pattern用于指定文件名/文件夹名
#pattern="sr-sgadv"
#pattern=pattern.decode('utf-8').encode('gbk')
###############################################
while stack:
    test=stack.pop()
    #test=unicode(test,"utf-8")
    f.write(test+'\n')
    if test=='/':
        break
    print test
    try:
        ftp.cwd(test)
    except:
        continue
    for i in ftp.nlst():
        i=("%s/%s") % (test,i)
        stack.append(i)
    #print stack
f.close()
#再生成一个utf-8编码的文本
f1 = codecs.open('ftp.txt', 'rb', 'mbcs')
f2 = open('ftp_utf8.txt', 'wb')
for x in f1:
    x=x.encode('utf-8')
    f2.write(x)
f1.close
f2.close()