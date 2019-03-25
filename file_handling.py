# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:24:50 2019

@author: keshav singh
"""

with open("file.txt","r+") as myfile:
    print(myfile.read())
myfile.close()