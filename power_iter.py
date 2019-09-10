#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:12:02 2019

@author: kevinhowlett
"""

#program takes two floats or ints, base and exp, and raises the base to
#the power of the exp

def iterPower(base, exp):

    num=base
    for i in range(exp-1):
        num=num*base
    if exp==0:
        return 1
    else:
        return num
    