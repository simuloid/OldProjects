# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 15:55:23 2016

@author: srowe
"""

def alphabetical_value(s):
    t = 0
    for c in s:
        v = ord(c) - ord('A') + 1
        # print c, v
        t += v
        
    return t
    
def name_score(i, names):
    return (i+1) * alphabetical_value(names[i])
    
def load_names():
    f = open('p022_names.txt')
    s = f.read()
    s = s.replace('"', '')
    names = s.split(',')
    return sorted(names)
    
if __name__ == '__main__':
    names = load_names()
    print names
    total = 0
    for i in range(len(names)):
        total += name_score(i, names)
        
    print total