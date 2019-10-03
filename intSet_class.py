#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:49:38 2019

@author: kevinhowlett
"""
#Program creates a class, intSet, which can add integers to a set
#and has a few different functions, including the ability to
#find the intersection between sets


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """Returns intersection of two sets"""
        intersection=intSet()
        for item in self.vals:
            if other.member(item):
                intersection.insert(item)
        return intersection
        
    def __len__(self):
        """Returns length of set"""
        count=0
        for item in self.vals:
            count+=1
        return count