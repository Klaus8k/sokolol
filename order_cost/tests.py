import os
import json

print(os.getcwd())
b = os.popen('cat 1.txt', 'r') # open file r or w
print(b.read())

# os.system - run command
a = [os.name, os.system('ls | grep 1'), os.environ['PATH']]

print(a)