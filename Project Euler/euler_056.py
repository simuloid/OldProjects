# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:20:27 2016

@author: srowe

Powerful digit sum
Problem 56
A googol (10100) is a massive number: one followed by one-hundred 
zeros; 100100 is almost unimaginably large: one followed by two-
hundred zeros. Despite their size, the sum of the digits in each 
number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, 
what is the maximum digital sum?
"""

def sum_of_digits(n):
    s = 0
    for d in str(n):
        s += int(d)
    return s
 
if __name__ == '__main__':
    for a in range(1,100):
        m = 0
        for b in range(1,100):
            n = a**b
            s = sum_of_digits(n)
            if s > m:
                m = s
                
    print m
    