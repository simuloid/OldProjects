# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:46:40 2016

@author: srowe
"""
import sys
import sympy
from math import sqrt

primes = [2]

def generate_primes(upto):
    global primes
    for n in range(3, upto):
        prime = True
        s = sqrt(n)
        for p in primes:
            if p > s:
                break
            if (n % p) == 0:
                prime = False
                break
        if prime:
            primes.append(n)

#    primes = set(sorted(primes))
           
def is_prime(n):
    for p in primes:
        if p > sqrt(n):
            break
        if n % p == 0:
            return False
    return True

def prime_factors(n):
    return sympy.factorint(n)
    
def my_prime_factors(n):
    rc = set([])
    while n > 1:
        for p in primes:
            if p > n:
                return rc
            while n % p == 0:
                rc.add(p)
                n = n / p
            break
    return rc
    
if __name__ == '__main__':
    print "Generating..."
    sys.stdout.flush()
    generate_primes(100000)
    print "Looking..."
    sys.stdout.flush()
    consecutive = 0
    target_consecutive = 4
    for n in range(3, 200000):
        pf = my_prime_factors(n)
        if len(pf) != target_consecutive:
            consecutive = 0
        else:
            consecutive += 1
            if consecutive >= target_consecutive:
                print "Answer:", n - target_consecutive + 1
                break
