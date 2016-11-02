# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:32:37 2016

@author: srowe
"""

def is_pythagorean_triplet(a,b,c):
    return a*a + b*b == c*c
    
def sum_to_1000(a,b,c):
    return a+b+c == 1000
    
def do_eet():
    for a in range(1,1001):
        for b in range(1,1001):
            for c in range(1,1001):
                if is_pythagorean_triplet(a,b,c):
                    print "pythagorean: ", a, b, c
                    if sum_to_1000(a,b,c):
                        print "sum to 1000: ", a,b,c
                        return
                    
do_eet()
