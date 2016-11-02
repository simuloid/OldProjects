# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:52:19 2016

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

def n_digits_from(p, start, n):
    t = 0
    for i in range(start,start+n):
        t = t * 10
        t += p[i]

    return t
        
def is_interesting(p):
    t = n_digits_from(p, 1, 3) % 2 + \
    n_digits_from(p, 2, 3) % 3 + \
    n_digits_from(p, 3, 3) % 5 + \
    n_digits_from(p, 4, 3) % 7 + \
    n_digits_from(p, 5, 3) % 11 + \
    n_digits_from(p, 6, 3) % 13 + \
    n_digits_from(p, 7, 3) % 17
    return t == 0

if __name__ == '__main__':
    interesting = []
    p = (0,1,2,3,4,5,6,7,8,9)
    while p:
        if is_interesting(p):
            v = n_digits_from(p, 0, len(p))
            print p, v
            interesting.append(v)
        p = next_permutation(p)