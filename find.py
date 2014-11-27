#coding:utf-8
import re
f=open('ftp.txt','r')
pattern='关键字'
pattern=pattern.decode('utf-8').encode('gbk')
for line in f:
	if re.search(pattern,line):
		print 'found!',line