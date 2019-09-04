#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:01:50 2019

@author: kevinhowlett
"""

#problem set 1.1
#program that counts number of vowels contained in the string "s"

num_vowels = 0
for i in s:
    if i == 'a'or i=='e'or i=='i'or i=='u'or i=='o':
        num_vowels+=1
print('Number of vowels: '+str(num_vowels))