#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:17:11 2019

@author: kevinhowlett
"""

#program calculates minimum fixed monthly payment required to pay
#off credit card balance in a year using bisection search

def minFixed(balance,annualInterestRate):

    initBalance = balance
    monthlyInterestRate = annualInterestRate/12.0
    lower=balance/12
    upper=(balance*(1+monthlyInterestRate)**12)/12.0
    minimumPayment = (lower+upper)/2


    while abs(balance)>=0.01:
        for i in range(12):
            unpaidBalance = balance - minimumPayment
            balance = unpaidBalance+monthlyInterestRate*unpaidBalance
        if balance>0.01:
            balance = initBalance
            lower = minimumPayment
            
        elif balance<(-0.01):
            balance = initBalance
            upper = minimumPayment
            
        minimumPayment = (lower+upper)/2.0
        
    print(str(round((minimumPayment),2)))
