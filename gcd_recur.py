#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:38:18 2019

@author: kevinhowlett
"""
#program finds the greatest common divisor of
#variables a and b using recursion

def gcdRecur(a, b):

    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)
