# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:07:28 2016

@author: Steve
"""

# Generate s digits of Champernowne's constant
def champernowne(n):
    s = ''
    i = 1
    while len(s) < n:
        s = s + str(i)
        i += 1
    return s

if __name__ == '__main__':
    C = champernowne(1000000)
    ans = 1
    for e in range(7):
        p = int(10**e)
        d = int(C[p-1])
        print 'd',p,'is',d
        ans *= d
        
    print 'ans:', ans