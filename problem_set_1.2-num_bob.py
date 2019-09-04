#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:04:59 2019

@author: kevinhowlett
"""

#problem set 1.2
#program that prints the number of times the string 'bob' occurs in "s"

num_bob=0
for i in range(len(s)+1):
    if s[i-3:i]=='bob':
        num_bob+=1
print('Number of times bob occurs is: '+str(num_bob))