# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:56:01 2022

@author: Tom

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""
print('Enter a number: ')
x = int(input())

testList = range(2, x)

for i in testList:
    if x % i == 0:
        print(i)