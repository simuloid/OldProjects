# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:28:53 2016

@author: srowe
"""

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
           
def is_composite(n):
    return not is_prime(n)

def matches_conjecture(c):
    # Find a prime
    for p in primes:
        if p > c:
            return False
        # Now find a square
        for s in range(1, int(1+sqrt(c-p))):
            t = p + 2 * s * s
            if t == c:
                return True
    raise "Ran out of primes."
    
if __name__ == '__main__':
    generate_primes(1000000)
    for c in range(3, 100000, 2):
        if is_prime(c):
            continue
        if not matches_conjecture(c):
            print "Fails conjecture: ", c
            break
