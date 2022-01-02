# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:28:46 2022

@author: Tom

Takes two list and finds elements that occur in both
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 
def overlap(a, b):
     c = []
     i = 0
     for i in a:
         if i in b and i not in c:
             c.append(i)
         i+=1
     print(c)

overlap(a, b)       