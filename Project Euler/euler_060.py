# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 12:30:48 2016

@author: srowe

Prime pair sets
Problem 60
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any 
order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. The sum 
of these four primes, 792, represents the lowest sum for 
a set of four primes with this property.

Find the lowest sum for a set of five primes for which 
any two primes concatenate to produce another prime.
"""

from itertools import *
from math import sqrt

primes = [2]

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
            
def is_prime_using_list(n):
    if n in primes:
        return True
    s = int(sqrt(n))
    for p in primes:
        if n % p == 0:
            return False
        if p > s:
            primes.append(n)
            return True
    raise "Need more primes"
    
def is_prime(n):
    s = int(sqrt(n))
    for p in range(2, s+1):
        if n % p == 0:
            return False
#    primes.append(n)
    return True
    

def test(pset):
    for t in combinations(pset, 2):
        x = int(str(t[0])+str(t[1]))
        if not is_prime(x):
            return False
        x = int(str(t[1])+str(t[0]))
        if not is_prime(x):
            return False
    return True

compatible = dict()
   
if __name__ == '__main__':
    generate_primes(1000)
    for p in primes:
        compatible[p] = set()
        for q in primes:
            if q <= p:
                continue
            if is_prime(int(str(p)+str(q))) and \
               is_prime(int(str(q)+str(p))):
                   compatible[p].add(q)

    count_compatible = dict()                  
    for p in primes:
        count_compatible[p] = 0
        for k in compatible:
            s = compatible[k]
            if p in s:
                count_compatible[p] += 1
                
    for k in count_compatible:
        if count_compatible[k] >= 5:
            print k,count_compatible[k]