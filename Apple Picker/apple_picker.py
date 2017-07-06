# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:57:49 2017

@author: Pranav Yadav

Apple Picking Game
"""

import time
global gold
global apple
gold = 0
apple = 0

def start():
    print("Hello and Welcome!")
    name = input("What is your name? ")
    print("\nWelcome, " + name + "!\n")
    print(name + " the objective of this game is to collect apples and then trade them in for gold.")
    print("The more apples you collect, the more gold you will accumalate!")
    choice = input(name + " would you like to start collecting apples? (Yes/No) ")
    
    if choice == "Yes":
        begin()
    elif choice == "No":
        print("\nSorry " + name + ", you couldn't pick any apples today! :( ")
    
def begin():
    global apple
    global gold
    print("\nLet's start picking apples!")
    pickappl = input("Do you want to pick an apple? (Yes/No) ")
    
    while(pickappl == "Yes"):
        time.sleep(1)
        print("\nYou picked an apple!")
        apple +=1
        print("You have ",apple, "apples!")
        pickappl = input("Do you want to pick another apple? (Yes/No) ")
        
    if pickappl == "No":
        sellappl = input("Do you want to sell your apples? (Yes/No) ")
        
        if sellappl == "Yes":
            gold = (apple * 10) + gold
            apple = 0
            print("\nYou have sold all your apples...")
            print("You have ",gold, "gold!")
            pickappl = input("Do you want to pick more apples? (Yes/No) ")
            if pickappl == "Yes":
                begin()
            elif pickappl == "No":
                print("\nYou have ",gold, "gold! Hope you had fun picking apples, goodbye!")  
                
        elif sellappl == "No":
            pickappl = input("Do you want to pick more apples? (Yes/No) ")
            if pickappl == "Yes":
                begin()
            elif pickappl == "No":
                print("\nYou have ",gold, "gold! Hope you had fun picking apples, goodbye!")                
                

start()