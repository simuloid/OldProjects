# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:45:19 2016

@author: Steve
"""
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
    
previous_cache = {}

def previous(n):
    if n in previous_cache:
        return previous_cache[n]
    t = 0
    for i in range(n):
        t = t + square(i)[1]
        
    previous_cache[n] = t
    return t
    
def square(n):
    side = 1+n*2
    return side, max(1,side*2+(side-2)*2)
    
def cornersx(r):
    side, num = square(r)
    start = previous(r)+1
    c = start + side - 2
    return [ c, c + side - 1, c + 2 * (side - 1), c + 3 * (side - 1)]
    
def corners(r):
    # The odd square (r*2+1) ** 2 is the biggest number.
    # The start value ((r-1)*2+1) ** 2 + 1
    side, num = square(r)
#    start = previous(r)+1
    start = ((r-1)*2+1) ** 2 + 1
    c = start + side - 2
    return [ c, c + side - 1, c + 2 * (side - 1), c + 3 * (side - 1)]
    
if __name__ == '__main__':
    L = 100000000
#    generate_primes(L)
    p = 0
    np = 1
    r = 20000
    t = 0
    for i in range(1,r+1):
        side = 1+i*2
        c = corners(i)
        for x in c:
            if is_prime(x):
                p += 1
            else:
                np += 1
#        print c
        f = float(p)/(float(p+np))
        print side, p, np, int(f*100+0.5),'%', c
        if f < 0.1:
            break
 #   print t + 1
        