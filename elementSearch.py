# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 15:39:50 2022

@author: Tom

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
"""
a = [1, 3, 5, 30, 42, 43, 500]

def search(list, subject):
    for i in list:
        if i == subject:
            return True
    return False


def binaryLoop(list, subject):
    midIndex = int(len(list)/2)
    midValue = list[midIndex]
    if subject < midValue:
        reduced = list[:midIndex]
    elif subject > midValue:
        reduced = list[midIndex + 1:]
    elif subject == midValue:
        reduced = [midValue]
    return reduced

def binarySearch(list, subject):
    while len(list) > 2:
        list = binaryLoop(list, subject)
    print(search(list, subject))
    
binarySearch(a, 9)