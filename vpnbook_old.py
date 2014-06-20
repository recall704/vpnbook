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
    k = re.findall(r"<li><strong>.*\.vpnbook.com</strong>",result)
    for one in k:
        print "\t"+one[one.find("<strong>")+len("<strong>"):one.find("</strong>")]
    u = re.findall(r"<li>Username.*</li>",result)
    user = u[0]
    print "Username:"
    print "\t"+user[user.find("<strong>")+len("<strong>"):user.find("</strong>")]
    p = re.findall(r"<li>Password.*</strong>",result)
    password = p[0]
    print "Password:"
    print "\t"+password[password.find("<strong>")+len("<strong>"):password.find("</strong>")]
else:
    print "No matched"

if __name__ == "__main__":
    raw_input()
else:
    pass
