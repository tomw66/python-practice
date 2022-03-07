# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 20:00:26 2022

@author: Tom
Ask the user for a number and determine whether the number is prime or not.
"""

def checkPrime(number):
    num = int(number)
    testList = range(2, num)
    isPrime = True
    for i in testList:
        if num % i == 0:
            print(str(num) + ' is not a prime number')
            isPrime = False
            break
    if isPrime:
        print(str(num) + ' is a prime number')
    
checkPrime(input('Enter a number: '))