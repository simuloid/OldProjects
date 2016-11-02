# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:20:21 2016

@author: srowe
"""

names = ['1p', '2p', '5p', '10p', '20p', '50p', 'L1', 'L2']
multipliers = [1, 2, 5, 10, 20, 50, 100, 200]

def sop(counts, values):
    t = 0
    for i in range(len(counts)):
        t += counts[i] * values[i]
    return t
    
def next_tuple(t, m):
    i = 0
    d = [j for j in t]
    while i < len(t):
        d[i] += 1
        if d[i] * multipliers[i] > m:
            d[i] = 0
            i = i + 1
        else:
            break
        
    if i == len(t):
        return None
        
    return tuple(d)
    
make_cache = {}

def ways_to_make_k(k, mi):
    if k in make_cache:
        return make_cache[k]
        
    t = 0
    c = tuple([0]*(mi+1))
    while c != None:
        if sop(c, multipliers) == k:
            print c, k
            t += 1
        c = next_tuple(c, k)
        
    make_cache[k] = t
    return t
    
def recursive_ways(k, mi):
    if k == 0:
        return 1 # One way to pay: no coins
    if k < 0:
        return 0 # No way to pay negative values
    if mi < 0:
        return 0 # we are out of coins
        
    vmi = multipliers[mi]
    # C(N,mi) = C(N,mi-1) + C(N-vmi, mi)
    return recursive_ways(k, mi-1) + recursive_ways(k-vmi, mi)
    
if __name__ == '__main__':
    for i in range(1, 10):
        print ways_to_make_k(i, 3)
        print recursive_ways(i, 3)