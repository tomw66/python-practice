# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:24:37 2022

@author: Tom
In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
"""
import random

with open('sowpods.txt', 'r') as f:
    all_text = f.read()
    all_list = all_text.split()
    i = random.randint(0, len(all_list))
    print(all_list[i])