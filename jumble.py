# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:52:10 2019

@author: keshav singh
"""

import random

def choose():
    words =['keshav','singh','science','master','analysis']
    pick =random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    printf(p1name,'Your point',pp1)
    printf(p1name,'Your point',pp1)


def play():
    p1name=input("Player 1 name")
    p2name=input("Player 2 name")
    pp1 =0
    pp2 =0
    turn =0
    while(1):
        #Computer Task
        picked_word = choose()
        #Create question
        qn = jumble(picked_word)
        print(qn)
        if(turn%2==0):
            print(p1name,"Your Turn")
            ans=input("what's your answer")
            if(ans==picked_word):
                pp1=pp1+1
                print("Your score is ",pp1)
            else:
                print("Better luck next time",picked_word)
            c=input("Press 1 for continue or 0 for exit")
            if(c==0):
                print("Thank",p1name,pp1,p2name,pp2)
                break
        #player 2
        else:
            print(p2name,"Your Turn")
            ans=input("what's your answer")
            if(ans==picked_word):
                pp2=pp2+1
                print("Your score is ",pp2)
            else:
                print("Better luck next time",picked_word)
            c=input("Press 1 for continue or 0 for exit")
            if(c==0):
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()
