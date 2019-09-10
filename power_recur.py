#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:56:18 2019

@author: kevinhowlett
"""
#program takes two floats or ints, base and exp, and raises the base to
#the power of the exp using recursion

def recurPower(base, exp):

    if exp==0:
        return 1
    else:
        return base*recurPower(base, exp-1)
