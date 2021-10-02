#!/usr/local/bin/python3
from os import popen
from re import split
fWho=popen('who','r')
for eachLine in fWho.readlines():
    print(split('\s\s+|\t',eachLine.strip()))

fWho.close()
