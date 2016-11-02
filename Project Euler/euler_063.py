# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 08:40:44 2016

@author: Steve

Powerful digit counts
Problem 63
The 5-digit number, 16807=75, is also a fifth power. Similarly, 
the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth 
power?
"""

if __name__ == '__main__':
    t = 0
    for n in range(1, 100):
        e = 1.0 / n
        print '==========================='
        low = 10**(n-1)
        high = 10**n
#        print low, high
        for p in range(1, 100):
            x = p ** n
            if len(str(x)) == n:
                t = t + 1
                print x, p, n
                
    print t
                
        