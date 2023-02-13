import json
import os
import time

# print(os.getcwd())
# b = os.popen('cat 1.txt', 'r') # open file r or w
# print(b.read())

# # os.system - run command
# # os.environ - переменные командной оболочки
# a = [os.name, os.system('ls | grep 1'), ]

# c = os.path.split(os.getcwd())


# print(c)

def decor(fn):
    def wrapp(*args, **kwargs):
        x = str(fn(*args, **kwargs)) + str(f' {fn.__name__}')
        return x
    return wrapp


# @decor
def subject(a : int):
    """test function"""
    x = 0
    return x + a

@decor
def folk(i = 'my name'):
    return i


print(folk())

# print(subject(1))

# subject = decor(subject)

# print(subject(1))
