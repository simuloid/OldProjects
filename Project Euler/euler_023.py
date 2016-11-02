# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:15:05 2016

@author: srowe
"""

# So-called "proper" divisors are numbers less than n that
# divide n evenly.
factor_cache = dict()

def proper_divisors(n):
    if factor_cache.has_key(n):
        return factor_cache.get(n)
        
    rc = set([1])
    for d in range(2, int(sqrt(n)+1)):
        if n % d == 0:
            rc.add(d)
            rc.add(n/d)
            
    factor_cache[n] = rc
    return rc
    
def sum_of_divisors(n):
    d = proper_divisors(n)
    s = sum(d)
    return s
    
def is_perfect(n):
    return sum_of_divisors(n) == n
    
def is_deficient(n):
    return sum_of_divisors(n) < n
    
def is_abundant(n):
    return sum_of_divisors(n) > n

def sum_of_abundant(n):
    for a in abundant:
        b = n - a
        if b > 0 and is_abundant(b):
            return True
    return False
    
# Find all abundant numbers less than 28124/2 = 14062

if __name__ == '__main__':
    answer = 0
    abundant = [i for i in range(12,14062) if is_abundant(i)]
    for i in range(1, 28124):
        if not sum_of_abundant(i):
            print i
            answer += i
            
    print 'answer: ', answer