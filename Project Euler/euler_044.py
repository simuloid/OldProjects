# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:29:54 2016

@author: srowe
"""

from math import sqrt

pentagonal_cache = set([])

def nth_pentagonal_number(n):
    p = n*(3*n-1)/2
    pentagonal_cache.add(p)
    return p
    
def is_pentagonal(t):
    return t in pentagonal_cache
    
def do_eet():
    N = 10000
    for i in range(1, N):
        d = nth_pentagonal_number(i)
        for j in range(i+1, N):
            s = nth_pentagonal_number(j)
            # now make pj, pk (> pj) such that
            # pk-pj == d
            # s = pj+pk
            pj = (s - d)/2
            if not is_pentagonal(pj):
                continue
            pk = d + pj
            if not is_pentagonal(pk):
                continue
            print pj, pk, d, s
            return
    
if __name__ == '__main__':
    print 'generating pentagonals.'
    for j in range(1, 1000000):
        nth_pentagonal_number(j)
    print 'done generating.'
    
    do_eet()