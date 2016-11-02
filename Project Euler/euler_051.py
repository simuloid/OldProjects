# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:32:00 2016

@author: Steve

By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 
13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the 
same digit, this 5-digit number is the first example 
having seven primes among the ten generated numbers, 
yielding the family: 
56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the 
number (not necessarily adjacent digits) with the same 
digit, is part of an eight prime value family.
"""

from math import sqrt

primes = [2]
fast_primes = set([])

def generate_primes(upto):
    global primes
    global fast_primes
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
            
    fast_primes = set(primes)

def nth_mask(length, n):
    fmt = '{0:0' + str(length) + 'b}'
    return fmt.format(n)

def family(n, mask):
    assert len(str(n)) == len(mask)
    rc = []
    for r in range(10):
        s = [c for c in str(n)]
        for i, c in enumerate(mask):
            if c == '1':
                s[i] = str(r)
        p = int(''.join(s))
        if len(str(p)) == len(mask) and p in fast_primes:
            rc.append(p)
    return rc

def find_family(size):
    for p in primes:
        L = len(str(p))
        if L < 5:
            continue
        for m in range(1,2**L-1):
            mask = nth_mask(L, m)
            f = family(p, mask)
            if len(f) >= size:
                print p, mask, f
                return f
    return None
    
if __name__ == '__main__':
    print "Generating..."
    generate_primes(1000000)
    f = find_family(8)
