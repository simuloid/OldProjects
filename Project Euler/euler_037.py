# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 02:27:12 2016

@author: Steve
"""

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
            

def left_truncate(n):
    s = str(n)
    return int(s[1:])

def right_truncate(n):
    s = str(n)
    return int(s[:-1])
    
def all_truncations(n):
    d = len(str(n))
    rc = []
    ln = n
    rn = n
    for i in range(d-1):
        if ln > 10:
            ln = left_truncate(ln)
            rc.append(ln)
        if rn > 10:
            rn = right_truncate(rn)
            rc.append(rn)
        
    return rc        
    
if __name__ == '__main__':
    print 'Generating primes...'
    generate_primes(1000000)
    print len(primes),'primes generated.'
    truncatable = []
    for p in primes:
        if p < 10:
            continue
        print p
        r = all_truncations(p)
        is_truncatable = True
        for q in r:
            if q not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable.append(p)
            
    print len(truncatable),'truncatable primes.'