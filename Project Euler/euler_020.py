# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:29:20 2016

@author: srowe
"""
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
        

digits = str(factorial(100))
t = 0
for c in digits:
    t += int(c)

print t
