# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:31:16 2016

@author: srowe
"""
from math import sqrt

# So-called "proper" divisors are numbers less than n that
# divide n evenly.
factor_cache = dict()

def proper_divisors(n):
    if factor_cache.has_key(n):
        return factor_cache.get(n)
        
    rc = set([1])
    for d in range(2, int(sqrt(n)+1)):
        if n % d == 0:
            rc.add(d)
            rc.add(n/d)
            
    factor_cache[n] = rc
    return rc
    

def d(n):
    return sum(proper_divisors(n))
    
def amicable(a, b):
    return a != b and d(a) == b and d(b) == a
    
if __name__ == '__main__':
    s = 0
    mx = 10000
    for a in range(mx):
        for b in range(a+1, mx):
            if amicable(a,b):
                print a, b
                s += a + b
                
    print 'sum is ', s