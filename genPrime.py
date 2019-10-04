#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 21:28:15 2019

@author: kevinhowlett
"""

#Program generates prime numbers in successive calls

def genPrimes():
    primes=[]
    x=1
    while True:
        x+=1
        for p in primes:
            if (x%p) == 0:
                break
        else:
            primes.append(x)
            yield x