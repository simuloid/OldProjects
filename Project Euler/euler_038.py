# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:07:16 2016

@author: Steve
"""

def is_pandigital(s):
    if len(s) != 9:
        return False
        
    counts = [0]*9

    for c in s:
        d = int(c)
        counts[d-1] += 1
        
    for i in range(1,len(s)+1):
        if counts[i-1] != 1:
            return False
            
    return True

def mult_by_tuple(n, t):
    s = ''
    for i in t:
        p = n * i
        s = s + str(p)
        
    return s

def make_tuple(k):
    return tuple([i for i in range(1, k+1)])
    
if __name__ == '__main__':
    biggest = 0
    for j in range(2, 10):
        t = make_tuple(j)
        print t
        for n in range(1, 10000):
            s = mult_by_tuple(n, t)
            if is_pandigital(s):
                print t, n, s
                p = int(s)
                if p > biggest:
                    biggest = p
                    
    print 'Ta-da:', biggest
            
        