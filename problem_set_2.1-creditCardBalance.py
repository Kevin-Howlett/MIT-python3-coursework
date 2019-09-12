#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:55:58 2019

@author: kevinhowlett
"""

#program defines a function which takes three variables (balance, annualInterestRate,
#and monthlyPaymentRate) for a credit card account, and returns credit card balance
#if only the minimum payment is met for a year

def findBalance(balance,annualInterestRate,monthlyPaymentRate):
        
    for i in range(12):
        monthlyInterestRate = annualInterestRate/12.0
        minimumPayment = monthlyPaymentRate*balance
        unpaidBalance = balance - minimumPayment
        balance = unpaidBalance+monthlyInterestRate*unpaidBalance
    print('Remaining balance: '+str(round(balance,2)))
