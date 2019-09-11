#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:44:29 2019

@author: kevinhowlett
"""

#program takes in a character(char) and a string(aStr) in alphabetical order and 
#returns a boolean for whether the character is in the string or not

def isIn(char, aStr):

    if aStr=='':
        return False
    if char==aStr:
        return True
    low=0
    high=len(aStr)
    test=aStr[int((low+high)/2)]
    if test==char:
        return True
    elif test>char:
        return isIn(char,aStr[:aStr.find(test)-1])
    else:
        return isIn(char,aStr[aStr.find(test)+1:])