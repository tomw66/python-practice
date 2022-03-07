# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:21:23 2022

@author: Tom

Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen.
"""

with open('nameslist.txt', 'r') as open_file:
    all_text = open_file.read()
    all_list = all_text.split()
    darth_count = 0
    lea_count = 0
    luke_count = 0
    for i in all_list:
        if i == 'Darth':
            darth_count +=1
        elif i == 'Lea':
            lea_count +=1
        elif i == 'Luke':
            luke_count +=1
    print("darth:", darth_count, "lea:", lea_count, "luke:", luke_count)
    