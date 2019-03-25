# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:59:11 2019

@author: keshav singh
"""
a=[1,3,5,2,6]
count=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            count+=1
            tmp=a[i]
            
            for k in range(i,len(a)-1):
                a[i]=a[i+1]
                break
            a[len(a)-1]=tmp
            #break
print(a)
print(count)