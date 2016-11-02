# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 02:17:05 2016

@author: Steve
"""

def is_palindrome(s):
    return s == s[::-1]
    
if __name__ == '__main__':
    t = 0
    for n in range(1, 1000000):
        d = str(n)
        b = '{0:b}'.format(n)
        if is_palindrome(d) and is_palindrome(b):
            t += n
            
    print t