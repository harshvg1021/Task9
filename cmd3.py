#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

# print("hi lw !!!")
#time.sleep(10)

cmd = cgi.FieldStorage()
name = cmd.getvalue("x")
number = cmd.getvalue("y")
#print(cmd)
o = subprocess.getoutput("sudo kubectl scale deployment " +name+ " --replicas=" +number+ " --kubeconfig admin.conf")
print(o)
