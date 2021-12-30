import QiwiMaster
#API FROM TO


from keyauth import api

import os
import sys
import os.path
import platform
from datetime import datetime


keyauthapp = api("QChain", "u6NQ037Tro", "7528c35cc917bd84489bb861bdcdabdc1287128614dc2aa2983f1b5fbe4d6515","1.0")

print("Initializing")
keyauthapp.init()


key = input('Enter your license: ')
keyauthapp.license(key)


print("\nUser data: ") 
print("Hardware-Id: " + keyauthapp.user_data.hwid)
print("Created at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Last login at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expires at: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))






f = open("config.txt", 'r')
p = open("proxy.txt", 'r')
n = int(f.readline() )- 1
otstup = "    "
proxyStatus = p.readline()
print(proxyStatus)
proxy = None
if int(proxyStatus) == 1:
    proxy = str(p.readline())

getFrom = list(map(str, f.readline().strip().split(' ')))
for i in range(0, n):
    putTo = list(map(str, f.readline().strip().split(' ')))
    print(putTo)
    j = open("config.json", 'w+')
    j.write('{')
    j.write("\n" + otstup + '"' + "main-token" + '"' + " : " + '"' + getFrom[0] + '"' + ',')
    j.write("\n" + otstup + '"' + "main-number" + '"' + " : " + '"' + getFrom[1] + '"' + ',')
    j.write("\n" + otstup + '"' + "number-client" + '"' + " : " + '"' + putTo[1] + '"' + ',')
    if int(proxyStatus) == 2:
        j.write("\n" + otstup + '"' + "number-client" + '"' + " : " + '"' + p.readline() + '"')
    elif int(proxyStatus) == 1:
        j.write("\n" + otstup + '"' + "number-client" + '"' + " : " + '"' + proxy + '"')
    elif proxyStatus == 0:
        j.write("\n" + otstup + '"' + "proxy" + '"' + " : " + '"' + "no" + '"')
    j.write("\n}")
    j.close
    getFrom = putTo
    QiwiMaster.summa()
