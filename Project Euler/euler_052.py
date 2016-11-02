# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:27:13 2016

@author: Steve

It can be seen that the number, 125874, and its double, 
251748, contain exactly the same digits, but in a different 
order.

Find the smallest positive integer, x, such that 
2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def same_digits(n, m):
    nd = set([int(d) for d in str(n)])
    md = set([int(d) for d in str(m)])
    return nd == md

def find_answer():
    for n in range(10000, 10000000):
        match = True
        for k in range(2,7):
            if not same_digits(n, n*k):
                match = False
                break
        if match:
            print 'Answer:', n
            return n
    return None
    
if __name__ == '__main__':
    find_answer()