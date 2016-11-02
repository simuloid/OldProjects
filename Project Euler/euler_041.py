# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:17:23 2016

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

#    primes = set(sorted(primes))
           
def is_prime(n):
    for p in primes:
        if p > sqrt(n):
            break
        if n % p == 0:
            return False
    return True
           
def is_pandigital(s):
    if len(s) != 9:
        return False
        
    counts = [0]*9

    for c in s:
        d = int(c)
        counts[d-1] += 1
        
    for i in range(1,len(s)+1):
        if counts[i-1] != 1:
            return False
            
    return True


def next_permutation(p):
    # Find the largest index k such that p[k] < p[k+1]
    k = -1
    for i in reversed(range(len(p)-1)):
        if p[i] < p[i+1]:
            k = i
            break
    if k == -1:
        return None
        
    # Find the largest index l > k such that a[k] < a[l]
    l = -1
    for i in reversed(range(k+1, len(p))):
        if p[k] < p[i]:
            l = i
            break
    # Swap a[k] and a[l]
    x = [n for n in p]
    x[k], x[l] = x[l], x[k]
    
    # Reverse sequence from a[k+1] onward
    x[k+1:] = reversed(x[k+1:])
    return tuple(x)

def tuple_to_number(t):
    s = ''
    for d in t:
        s = s + str(d)
    return int(s)
    
if __name__ == '__main__':
    print 'generating primes'
    generate_primes(int(sqrt(987654321))+1)
    print 'generated', len(primes), 'primes'
    for N in range(2,10):
        t = tuple([i for i in range(1,N+1)])
        while t:
            p = tuple_to_number(t)
            if is_prime(p):
                print p
            t = next_permutation(t)
            