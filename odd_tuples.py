#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:31:54 2019

@author: kevinhowlett
"""

#program takes a tuple and returns a tuple
#of every odd item from the original tuple

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup=()
    counter=0
    for i in aTup:
        counter+=1
        if counter%2==1:
            newTup+=(i,)
    print(newTup)
