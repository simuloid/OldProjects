# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 13:23:57 2016

@author: srowe
"""

from math import sqrt

# n^2 + an + b where |a| < 1000 and |b| < 1000
# Find a,b that produces the most consecutive primes
# starting with n=0.

prime_cache = set()

def is_prime(n):
    if n in prime_cache:
        return True
        
    if n < 2:
        return False
    s = int(sqrt(n))
    for d in range(2, s+1):
        if n % d == 0:
            # n is evenly divisible by d => Not Prime.
            return False
            
    prime_cache.add(n)
    return True

def consecutive_primes(a, b):
    rc = []
    for n in range(1000):
        v = n*n + a*n + b
        if is_prime(v):
           rc.append(v)
        else:
            break
    return rc
    
if __name__ == '__main__':
    max_primes = 0
    mp_a = -1000
    mp_b = -1000
    for a in range(-1999,2000):
        for b in range(-1999,2000):
            cp = len(consecutive_primes(a,b))
            if cp > max_primes:
                max_primes = max(max_primes, cp)
                mp_a = a
                mp_b = b
                
    print max_primes, mp_a, mp_b, mp_a * mp_b
    