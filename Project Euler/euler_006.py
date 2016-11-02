# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:57:43 2016

@author: srowe
"""

def sum(n):
    t = 0
    for i in range(1,n+1):
        t += i
    return t
    
def sum_of_squares(n):
    t = 0
    for i in range(1,n+1):
        t += i*i
    return t
    
if __name__ == '__main__':
    s = sum(100)
    s = s * s
    sq = sum_of_squares(100)
    print(s);
    print(sq);
    print(s-sq)
    