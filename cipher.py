# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:06:19 2019

@author: keshav singh
"""

import string
dict={}
data=""
file=open("out.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("ciphar.txt") as f:
    while(True):
        c=f.read(1)
        if not c:
            print("End of line")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        #print(data)
file.close()
k=open("out.txt","r")
print(k.read())