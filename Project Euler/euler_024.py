# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:14:24 2016

@author: srowe
"""

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


if __name__ == '__main__':
    p = (0,1,2,3,4,5,6,7,8,9)
    for i in range(1,1000000):
        p = next_permutation(p)
        
    print p
    