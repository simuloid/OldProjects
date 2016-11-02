# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:23:37 2016

@author: srowe
"""

products = set([])

def pandigital(s):
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

#
# Given a tuple containing a permutation of the digits 1-9,
# Find all the partitions of the tuple into 3 parts.
# (multiplicand, multiplier, product).  Check for:
# correctness - does multiplicand * multiplier == product?
# Does the list of products contain the new product? If so, skip.
# Add the product to the list.
def check_products(t):
    for s1 in range(1,len(t)-1):
        for s2 in range(s1+1, len(t)):
            m1 = int(''.join([str(d) for d in t[:s1]]))
            m2 = int(''.join([str(d) for d in t[s1:s2]]))
            p = int(''.join([str(d) for d in t[s2:]]))
            q = m1 * m2
            if p != q or p in products:
                pass
            else:
                products.add(p)
                print m1, m2, p

if __name__ == '__main__':
    digits = tuple([1,2,3,4,5,6,7,8,9])
    while digits != None:
        check_products(digits)        
        digits = next_permutation(digits)
    
    
    