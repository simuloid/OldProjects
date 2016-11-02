# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:02:33 2016

@author: srowe
"""
import re
from math import sqrt

def nth_triangle_number(n):
    return n*(n+1)/2
    
def is_triangle_number(t):
    # Find n such that t == n*(n+1)/2
    # 2t = n*(n+1)
    # 2t = (n+0.5)**2 - 0.25
    # 2t + 0.25 = (n + 0.5)**2
    # sqrt(2t + 0.25) = n + 0.5
    # sqrt(2t + 0.25) - 0.5 = n
    n = sqrt(2*t + 0.25) - 0.5
    return n == int(n)
    
def word_value(s):
    t = 0
    for c in s:
        t += ord(c)-ord('A')+1
    return t

def read_words(fname):
    f = open(fname)
    s = f.read()
    s = re.sub('["]', '', s)
    return s.split(',')
    
if __name__ == '__main__':
    print word_value('SKY')
    words = read_words('p042_words.txt')
    triangle_words = []
    for w in words:
        v = word_value(w)
        if is_triangle_number(v):
            print v, w
            triangle_words.append(w)
            
    print len(triangle_words), 'triangle words found.'