#! /usr/bin/python
#coding:utf-8

import re
import urllib2

url = "https://www.vpnbook.com/freevpn"

response = urllib2.urlopen(url)

html = response.read()

# print html

m = re.search('<ul\sclass=\"disc\">.*?</ul>',html,re.S)
if m:
    result = m.group()
    # print(result)
    print "Server:"
    s = re.findall(r"(?<=<strong>).*?\.vpnbook\.com(?=</strong>)",result)
    for sItem in s:
    	print "\t",sItem

    u = re.findall(r"(?<=<li>Username:<strong>).*?(?=</strong>)",result.replace(" ",""))
    # user = re.findall(r"(?<=<strong>).*?(?=</strong>)",u[0])
    print "Username:"
    print "\t",u[0]

    p = re.findall(r"(?<=<li>Password:<strong>).*?(?=</strong>)",result.replace(" ",""))
    # passwd = re.findall(r"(?<=<strong>).*?(?=</strong>)",p[0])
    print "Password:"
    print "\t",p[0]
else:
    print "No matched"

if __name__ == "__main__":
    raw_input()
else:
    pass
