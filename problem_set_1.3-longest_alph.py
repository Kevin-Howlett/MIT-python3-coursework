#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:08:17 2019

@author: kevinhowlett
"""

#problem set 1.3
#program that prints longest substring, in string "s", that occurs in alphabetical order
#in case of tie, prints first substring in tie

longest_sub=s[0]
substring=s[0]
for i in s[1:]:
    if i>=substring[-1]:
        substring+=i
        if len(substring)>len(longest_sub):
            longest_sub = substring
    else:
        substring=i
print('Longest substring in alphabetical order is: '+str(longest_sub))