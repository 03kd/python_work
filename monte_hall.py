# -*for- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:16:39 2019

@author: keshav singh
"""

import random

doors =[0]*3
goatdoors =[0]*2
swap =0
dont_swap =0
j=0

while(j<3):
    x=random.randint(0,2)
    doors[x]="W"
    for i in range(0,3):
        
        if(i==x):
            continue
        else:
            doors[i]="G"
            goatdoors.append(i)
    choice=int(input("Enters your choice "))
    door_open=random.choice(goatdoors)
    while(door_open==choice):
        door_open=random.choice(goatdoors)
    ch=input("Do you want to swap?y/n ")
    if(ch=='y'):
        if(doors[choice]=='G'):
            print("Player Wins")
            swap=swap+1
        else:
            print("Player lost")
    else:
        if(doors[choice]=='G'):
            print("player wins")
        else:
            print("Player lost")
            dont_swap =dont_swap +1
    j=j+1
print("with swaps win  ",swap)
print("Without swap wins  ",dont_swap)