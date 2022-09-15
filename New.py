#coding:utf-8
from platform import uname
from os import path,system,chmod
from sys import argv
try:
	import random_user_agent
except ImportError:
	system('pip install random_user_agent')
try:
    if argv[1].lower()=="reset":
        system("rm -rf *")
        system('curl -L https://raw.githubusercontent.com/BALLAKING/New/main/New.py -o New.py')
        system('python New.py')
except:
    pass
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\n\033[1;32mCongratulations! Your Device Support This Tools\033[1;37m')
else:
    exit("\033[1;31mSystem Not Support This Tools\033[1;37m")
while True:
        if path.isfile("New.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/BALLAKING/Data/main/New.so -o New.so")
        if path.isfile("dz.so"):
            break
        else:
            system(f"curl -L https://raw.githubusercontent.com/BALLAKING/Data/main/dz.so -o dz.so")
import New
print(' \n something working was wrong\n  run again :  python New.py reset');exit()
