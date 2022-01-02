# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:13:18 2021

@author: Tom

Simple program that asks for user input and returns a custom message
"""
import datetime
currentYear = datetime.datetime.now().year
name = input("Give me your name: ")
age = input("Give me your age: ")
age = int(age)
repeats = input("Give me another number: ")

def centenary(age, currentYear):
    ageDiff = 100 - age
    centYear = currentYear + ageDiff
    return str(centYear)
    
message = "Your name is " + name + ", you will be 100 in the year " + centenary(age, currentYear) + ".\n"
    
print(int(repeats) * message)

