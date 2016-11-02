# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:24:11 2016

@author: srowe
"""

pentagonal_cache = set([])

def nth_pentagonal_number(n):
    p = n*(3*n-1)/2
    pentagonal_cache.add(p)
    return p
    
def is_pentagonal(t):
    return t in pentagonal_cache
    
def nth_triangular_number(n):
    p = n*(n+1)/2
    return p
    
if __name__ == '__main__':
    for i in range(1, 100000):
        nth_pentagonal_number(i)
    # The TRICK is that every other triangular number is also
    # hexagonal.
    for i in range(1, 100000, 2):
        t = nth_triangular_number(i)
        if is_pentagonal(t):
            print t