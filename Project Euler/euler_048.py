# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:16:00 2016

@author: Steve
"""

if __name__ == '__main__':
    N = 1000
    t = 0
    for i in range(1, N+1):
        t += i**i
        
    print str(t)[-10:]
