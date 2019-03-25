# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:39:00 2019

@author: keshav singh
"""

def upper(r,a):
    for i in range(r):
        for j in range(r):
            if i>0:
             for k in range(i):
                 a[i][k]=0
            #print(a[i][j],end=" ")
    print_m(r,a)  

r=int(input())

a = []
for i in range(r):
    temp =list(input().split())
    temp=[int(i) for i in temp]
       
    a.append(temp)
    
upper(r,a)

def print_m (x,a):
    for i in range(x):
        for j in range(x):
            print(a[i][j],end=" ")
        print()
        