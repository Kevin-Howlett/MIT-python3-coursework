#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:56:39 2019

@author: kevinhowlett
"""

#Program creates a class called Coordinate which represents x, y
#coordinates in plotting
#A few functions were created under Coordinate class

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        return (self.x==other.x and self.y==other.y)
        
    def __repr__(self):
        return 'Coordinate('+str(self.x)+','+str(self.y)+')'
        