# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 01:21:31 2016

@author: Steve
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

    primes = set(sorted(primes))
            

def rotate(n):
    s = str(n)
    return int(s[-1]+s[:-1])

def all_rotations(n):
    d = len(str(n))
    rc = []
    for i in range(d):
        n = rotate(n)
        rc.append(n)
    return rc        
    
if __name__ == '__main__':
    print 'Generating primes...'
    generate_primes(1000000)
    print len(primes),'primes generated.'
    circular = []
    for p in primes:
        r = all_rotations(p)
        is_circular = True
        for q in r:
            if q not in primes:
                is_circular = False
                break
        if is_circular:
            circular.append(q)
            
    print len(circular),'circular primes.'