# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:52:48 2019

@author: keshav singh
"""
def r_p_s(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw")
    elif(player_one[p1]=='Rock' and player_two[p2]=='Paper'):
        print("Player_two wins !!!")
    elif(player_one[p1]=='Rock' and player_two[p2]=='Scissor'):
        print("Player_one wins !!!")
    elif(player_one[p1]=='Paper' and player_two[p2]=='Scissor'):
        print("Player_two wins !!!")
    elif(player_one[p1]=='Paper' and player_two[p2]=='Rock'):
        print("Player_one wins !!!")
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Paper'):
        print("Player_one wins !!!")
    elif(player_one[p1]=='Scissor' and player_two[p2]=='Rock'):
        print("Player_two wins !!!")

player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_two={0:'Paper',1:'Scissor',2:'Rock'}

while(1):
    num1=(input("Player One enter your number"))
    num2=(input("Player two enter your number"))
    bit1=int(input("Player one ,enter your secrect position"))
    bit2=int(input("Player two ,enter your secrect position"))
    r_p_s(num1,num2,bit1,bit2)
    
    ch=input("Do you want to continue ? y/n")
    if(ch=='n'):
        break
    