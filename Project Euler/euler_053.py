# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:37:02 2016

@author: Steve

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
   n!
--------
r!(n−r)!

,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 
23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, 
for 1 ≤ n ≤ 100, are greater than one-million?
"""

fact_cache = dict()

def factorial(n):
    if n in fact_cache:
        return fact_cache[n]
    if n < 2:
        fact_cache[n] = 1
        return 1

    f = n * factorial(n-1)
    fact_cache[n] = f
    return f
       
def n_choose_r(n, r):
    nf = factorial(n)
    rf = factorial(r)
    df = factorial(n-r)
    return nf / (rf*df)

if __name__ == '__main__':
    t = 0
    for n in range(1, 101):
        for r in range(1, n):
            ncr = n_choose_r(n, r)
            if ncr > 1000000:
                t += 1
                
    print t