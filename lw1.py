#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

# print("hi lw !!!")
#time.sleep(10)

cmd = cgi.FieldStorage()
img = cmd.getvalue("x")
cont = cmd.getvalue("y")
#print(cmd)
o = subprocess.getoutput("sudo kubectl run " +cont+ " --image=" +img+ " --kubeconfig admin.conf")
print(o)
