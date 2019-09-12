#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:46:41 2019

@author: kevinhowlett
"""

#program calculates minimum fixed monthly payment needed to pay
#off credit card balance in a year

def minFixed(balance,annualInterestRate):
    minimumPayment=0
    initBalance = balance
    monthlyInterestRate = annualInterestRate/12.0

    while balance>0:
        for i in range(12):
            unpaidBalance = balance - minimumPayment
            balance = unpaidBalance+monthlyInterestRate*unpaidBalance
        if balance>0:
            minimumPayment+=10
            balance = initBalance
        elif balance<=0:
            break
        print('Lowest payment: '+str(minimumPayment))