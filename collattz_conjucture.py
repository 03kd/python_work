# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:19:51 2019

@author: keshav singh
"""

def checkcoll(num):
    count=1
    while(num!=1):
        if(num%2==0):
            num=num//2
            count+=1
        else:
            num=(num*3)+1
            count+=1
    print(num ,count)
    
checkcoll(70)