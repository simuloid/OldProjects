# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:35:20 2016

@author: srowe
"""
#from itertools import max

def collatz(n):
    iterations = 1
    while n > 1:
        iterations += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3 * n + 1
        
    return iterations

def argmax(keys, f):
    return max(keys, key = f)
    