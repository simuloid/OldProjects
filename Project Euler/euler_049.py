# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:26:46 2016

@author: Steve

The arithmetic sequence, 1487, 4817, 8147, in which each of the 
terms increases by 3330, is unusual in two ways: (i) each of 
the three terms are prime, and, (ii) each of the 4-digit 
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, 
or 3-digit primes, exhibiting this property, but there is 
one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three 
terms in this sequence?
"""

from math import sqrt

primes = [2]
big_primes = []

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
            if n > 999 and n < 10000:
                big_primes.append(n)

#    primes = set(sorted(primes))
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
    
def make_permutations(n):
    digits = sorted([int(c) for c in str(n)])
    t = tuple(digits)
    rc = []
    while t:
        rc.append(tuple_to_number(t))
        t = next_permutation(t)
    return rc
    
def find_answer():
    for p in big_primes:
        tups = make_permutations(p)
        for s in range(2, 3334):
#            print
#            print 'trying s=',s
            q = p
            out = str(p)
            success = True
            for i in range(2):
                q += s
#                print i, q,
                out = out + str(q)
                if q not in big_primes:
#                    print q, 'not prime'
                    success = False
                    break
                if q not in tups:
#                    print q, 'not in', tups
                    success = False
                    break
            if success:
                print 'Answer!', s, p, out
                break

    return None
    
if __name__ == '__main__':
    print "Generating..."
    generate_primes(100000)
    ans = find_answer()