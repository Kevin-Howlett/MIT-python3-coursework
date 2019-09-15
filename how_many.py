#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:07:34 2019

@author: kevinhowlett
"""

#program takes a dictionary with lists as values
#and returns an integer number of values in the dictionary

def how_many(aDict):

    num_values=0
    for v in aDict.values():
        for i in v:
            num_values+=1
    return num_values