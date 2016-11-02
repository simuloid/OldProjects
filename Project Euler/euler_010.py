# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:06:30 2016

@author: srowe
"""
from math import sqrt

primes = [2,3]

def is_prime(n):
    root = sqrt(n)
    for p in primes:
        if n % p == 0:
            return False
        if p > root:
            return True
            
    return True
    
def more_primes(n):
    c = primes[-1]+1
    while c < n:
        if is_prime(c):
            primes.append(c)
            
        c += 1
    pass        
    
if __name__ == '__main__':
    more_primes(2000000)
    print(sum(primes))
    