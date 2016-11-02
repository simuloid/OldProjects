# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:14:09 2016

@author: srowe
"""

def is_sum_of_pod(n, p):
    t = 0
    for c in str(n):
        d = int(c)
        t += d ** p
        
    return t == n
    
if __name__ == '__main__':
    t = 0
    for i in range(2, 1000000):
        if is_sum_of_pod(i, 5):
            print i
            t += i
            
    print 'sum is', t