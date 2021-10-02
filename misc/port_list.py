#!/usr/local/bin/python3
#from os import popen
#from re import split
import os, sys
import functools
def compare(A,B):
    if A.startport < B.startport:
        return -1
    elif A.startport > B.startport:
        return 1
    else:
        return 0

class Record():
    def __init__(self, rawStr):
        self.rawStr=rawStr
        self.startport = 0
        self.endport = 0
        self.type="tcp"
    def parse(self):
        strlist = self.rawStr.split('/')
        self.type =strlist[1]
        if "-" in strlist[0]:
            #print(strlist[0])
            strlist2=strlist[0].split('-')
            self.startport=int(strlist2[0])
            self.endport = int(strlist2[1])
        else:
            self.startport = int(strlist[0])
            self.endport = int(strlist[0])
    def __str__(self):
        return ("Start Port: %5d\tEnd Port: %5d\tPort type: %s"%(self.startport, self.endport, self.type))
    def printinfo(self):
        print("startport:",self.startport)
        print("endport:", self.endport)
        print("rawStr:", self.rawStr)
        print("type:", self.type)

command = 'firewall-cmd --zone=public --list-ports'
file=os.popen(command,'r')
cmd_res = file.read()
file.close()
#print cmd_res
myList = []


cmd_re2 = cmd_res.split()  
for element in cmd_re2:
    #print(element)
    item=Record(element)
    item.parse()
    myList.append(item)
    #item.printinfo()
myList.sort(key=functools.cmp_to_key(compare))
for item in myList:
    print(item)