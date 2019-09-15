#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:11:20 2019

@author: kevinhowlett
"""

#program takes a dictionary with lists as values and returns
#the key that has the largest number of associated values

def biggest(aDict):

    biggest=0
    biggest_key=''
    for k in aDict.keys():
        if len(aDict[k])>biggest:
            biggest_key=k
            biggest=len(aDict[k])
    return biggest_key