# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:44:51 2019

@author: Oliver

This is a binary tree node
"""

class node:
    def __init__(self, value):
        self.data = value
        self.count = 1
        self.left = None
        self.right = None
        
        
    def add(self, value):
        if value == self.data:
            self.count += 1
        elif value < self.data:
            if self.left is None:
                self.left = node(value)
            else:
                self.left.add(value)
        else:
            if self.right is None:
                self.right = node(value)
            else:
                self.right.add(value)