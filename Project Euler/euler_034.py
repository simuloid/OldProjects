# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 01:06:14 2016

@author: Steve
"""

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
def fact(n):
    if n < 2:
        return 1
    return n*fact(n-1)
    
def sum_of_fact(n):
    t = 0
    for c in str(n):
        d = int(c)
        t += fact(d)
    return t
    
def is_sum_of_fact(n):
    return sum_of_fact(n) == n
    
if __name__ == '__main__':
    # It would be interesting to know how to choose the
    # upper bound here.
    for i in range(3, 100000):
        if is_sum_of_fact(i):
            print i