# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:17:22 2022

@author: Tom

list numbers elements if conditional
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def filt(list, b):
    new = []
    for i in list:
        if i < b:
            new.append(i)
    print(new)
            
filt(a, 9)
