# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:23:43 2016

@author: srowe
"""

def previous(n):
    t = 0
    for i in range(n):
        t = t + square(i)[1]
        
    return t
    
def square(n):
    side = 1+n*2
    return side, max(1,side*2+(side-2)*2)
    
def corners(r):
    side, num = square(r)
    start = previous(r)+1
    c = start + side - 2
    return [ c, c + side - 1, c + 2 * (side - 1), c + 3 * (side - 1)]
    
if __name__ == '__main__':
    r = 500
    t = 0
    for i in range(r+1):
        c = corners(i)
        print c
        t = t + sum(c)
    print t + 1
        