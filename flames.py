# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:07:26 2019

@author: keshav singh
"""

import string

def remove_matching(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+['*']+l2
                return [l,True]
    l=l1+['*']+l2
    return [l,False]

p1=input("Enter he name: ")
p1=p1.lower()
p1.replace(" ","")

p2=input("Enter she name: ")
p2=p2.lower()
p2.replace(" ","")

l1=list(p1)
l2=list(p2)

flag=True
while flag==True:
    ret_list = remove_matching(l1,l2)
    con_list =ret_list[0]
    flag=con_list[1]
    star = con_list.index('*')
    l1 =con_list[:star]
    l2 =con_list[star+1:]
    
count=len(l1)+len(l2)
result =['Friend','Love','Affection','Marriage','Enemy','Siblings']

while len(result)>1:
    split_index =(count%len(result))-1
    if split_index>=0:
        right=result[split_index+1:]           
        left =result[:split_index]
        result=right+left
    else:
        result=result[:len(result)-1]
        
print(result[0])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            