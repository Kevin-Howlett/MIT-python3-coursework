#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:03:06 2019

@author: kevinhowlett
"""

#program has user think of a number between 0-100 and guesses number using 
#bisection search

low = 0
high = 100
guess = int((low + high)/2.0)
print('Please think of a number between 1 and 100!')



while True:

    print('Is your secret number ' + str(guess) + '?')
    i = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if i == 'c':
        print('Game over. Your secret number was:'+str(guess))
        break
    elif i == 'l':
        low = guess
    elif i == 'h':
        high = guess 
    else:
        print('Please enter a valid character.')

    guess = int((low + high)/2.0)
