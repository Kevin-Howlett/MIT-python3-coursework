#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 12:24:34 2019

@author: kevinhowlett
"""
#program finds the greatest common divisor of 
#the variables a and b using iteration

def gcdIter(a, b):

    if a==b:
        return a
    elif a<b:
        test=a
    elif b<a:
        test=b
    while True:
        if test==1:
            break
        if a%test==0 and b%test==0:
            break
        test-=1
    return test