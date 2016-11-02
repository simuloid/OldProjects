# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:06:30 2016

@author: srowe
"""

primes = [2,3]

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
            
    return True
    
def more_primes(n):
    c = primes[-1]+1
    while len(primes) < n:
        if is_prime(c):
            primes.append(c)
            
        c += 1
        
    print primes[n-1]
    
if __name__ == '__main__':
    more_primes(10001)
    print(primes)
    