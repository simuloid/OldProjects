# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 10:48:27 2016

@author: srowe
"""
from math import sqrt

sum_up_to = [0]

def triangle(n):
    return sum(range(1,n+1))
    
def dp_triangle(n):
    if len(sum_up_to) <= n:
        # Fill in more elements
        k = len(sum_up_to)
        for i in range(k, n+1):
            sum_up_to.append(sum_up_to[-1]+i)
            
    return sum_up_to[n]
    
def next_triangle():
    return dp_triangle(len(sum_up_to))
    
def factors(n):
    rc = set([])
    for d in range(1, int(sqrt(n)+1)):
        if n % d == 0:
            rc.add(d)
            rc.add(n/d)
    return rc
    
if __name__ == '__main__':
    while True:
        t = next_triangle()
        f = factors(t)
        if len(f) > 500:
            break
        
    print t, f