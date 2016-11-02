# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 23:40:24 2016

@author: Steve

Totient maximum
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi 
function], is used to determine the number of numbers less 
than n which are relatively prime to n. For example, as 
1, 2, 4, 5, 7, and 8, are all less than nine and relatively 
prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""
import sys
import math

factor_cache = dict()
primes = [2]

def generate_primes(upto):
    for n in range(2, upto):
        is_prime = True
        for p in primes:
            if p > math.sqrt(n):
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            factor_cache[n] = set([n])
            primes.append(n)

def factors(n):
    if n in factor_cache:
        return factor_cache[n]
    rc = [n]
    for f in xrange(2, n):
        if n % f == 0:
            rc.append(f)
            
    factor_cache[n] = set(rc)
    return factor_cache[n]

gcd_cache = dict()
    
def gcd(a, b):
    ais = []
    bis = []
            
    while b > 0:
        if a in gcd_cache:
            if b in gcd_cache[a]:
                return gcd_cache[a][b], True
        ais.append(a)
        bis.append(b)
        a, b = b, a % b

    for ai, bi in zip(ais, bis):
        if ai not in gcd_cache:
            gcd_cache[ai] = dict()
        if bi not in gcd_cache[ai]:
            gcd_cache[ai][bi] = a
        
    return a, False
    
cc = 0
nc = 0
def is_relatively_prime(a, b):
    global cc, nc
    
    g, cache_hit = gcd(a, b)
    if cache_hit:
        cc += 1
    else:
        nc += 1
        
    return g == 1
    
def phi(n):
    nrp = 0
    if n == 1:
        return 0
    if n in primes:
        nrp = n-1
    else:
        # rp = [1]
        for p in xrange(2, n):
            if is_relatively_prime(n, p):
                # rp.append(p)
                nrp += 1
        # nrp = len(rp)
#    print n, rp
        
    return float(n)/float(nrp)
    
if __name__ == '__main__':
    m = 0
    L = 10000
    generate_primes(L)
    for n in primes:
        p = phi(n-1)
        if p > m:
            m = p
            print n, p
        
    
        