# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:46:56 2016

@author: Steve
"""
#
# Generate all right triangles of perimeter p
# p = a + b + c
# c*c = a*a + b*b
def sides(p):
    rc = []
    for a in range(1, p-1):
        for b in range(a, p-1):
            c = p - b - a
            if c <= 0 or (a*a + b*b) != (c*c):
                continue
            rc.append((a,b,c))
            
    return rc
    
if __name__ == '__main__':
    m = 0
    mp = 0
    for p in range(3, 1001):
        s = sides(p)
        if len(s) > m:
            m = len(s)
            mp = p
            print p, m, s

    print 'rt triangle with perimeter',p,'has',m,'sets of integer sides.'