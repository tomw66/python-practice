# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:31:10 2021

@author: Tom

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
"""
def ex1():
    num = int(input("Give me a number: "))
    
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")
        
def ex2():
    num = int(input("Give me a number to check: "))
    check = int(input("Give me a number to divide by: "))
    
    if num % check == 0:
        print(str(check) + " divides evenly into " + str(num))
    else:
        print(str(check) + " does not divide evenly into " + str(num))
        
ex2()
