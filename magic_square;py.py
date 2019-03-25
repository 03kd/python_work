# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:59:53 2019

@author: keshav singh
"""

def magic_Square(n):
    
    magicSquare = []
    
    for i in range(n):
        l =[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i = n//2
    j = n-1
    count = 1
    num =n*n
    
    while(count<=num):
        if(i==-1 and j == n):
            j = n-2
            i = 0
        else:
            if(j == n):
                j=0
            if(i<0):
                i=n-1
                
        if(magicSquare[i][j]!=0):
            i=i+1
            j=j-2
            continue
        else:
            magicSquare[i][j]=count
            count=count+1
            
        i=i-1
        j=j+1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print( )
    print("Th sum of row/column/diagonal  "+str((n*(n**2+1)/2)))
k=input("enter no. do you want")
p =int(k)
magic_Square(p)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        