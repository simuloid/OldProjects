# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:26:15 2016

@author: srowe

Square root convergents
Problem 57
It is possible to show that the square root of two can be 
expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, 
but the eighth expansion, 1393/985, is the first example where 
the number of digits in the numerator exceeds the number of 
digits in the denominator.

In the first one-thousand expansions, how many fractions contain 
a numerator with more digits than denominator?
"""
from math import sqrt

primes = [2]

def generate_primes(upto):
    for n in range(2, upto):
        s = sqrt(n)
        prime = True
        for p in primes:
            if p > s:
                break
            if n % p == 0:
                prime = False
                break
        if prime:
            primes.append(n)
            
def prime_factors(n):
    f = []
    for p in primes:
        while n % p == 0:
            f.append(p)
            n = n / p
        if n == 1:
            break
    return f
            
def lcm(a, b):
    pfa = prime_factors(a)
    pfb = prime_factors(b)
    pf = []
    for f in pfa:
        if f in pf:
            continue
        c = max(pfa.count(f), pfb.count(f))
        pf.extend([f] * c)
        
    for f in pfb:
        if f in pf:
            continue
        c = max(pfa.count(f), pfb.count(f))
        pf.extend([f] * c)
        
#    print pfa, pfb, pf
    t = 1
    for f in pf:
        t = t * f
        
    return t
    
def add_frac(f1, f2):
    lcd = lcm(f1[1], f2[1])
    num = f1[0]*lcd/f1[1]
    num += f2[0]*lcd/f2[1]
    return (num, lcd)
    
# return the numerator and denominator of the
# repeating fraction after n iterations.
def root_denom(n):
    if n == 0:
        return 1.0/1+2
    return 2+1.0/root_denom(n-1)

if __name__ == '__main__':
    generate_primes(100000)
    n = 3
    d = 2
    t = 0
    for i in range(2, 1000):
        n, d = 2*d+n, d+n
        if len(str(n)) > len(str(d)):
            t = t + 1
            
    print "Answer:", t
    
    
