# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:49:35 2016

@author: srowe
"""

# Need the number of 40 digit binary numbers
# that contain an equal number of 0s and 1s

# 2n choose n, (2n)!/(n!)^2
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
        
def combinations(grid_size):
    n = factorial(2*grid_size)
    d = factorial(grid_size)
    d = d * d
    return n/d
    
if __name__ == '__main__':
    print combinations(20)    