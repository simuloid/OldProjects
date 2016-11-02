# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 20:27:17 2016

@author: Steve

Passcode derivation
Problem 79
A common security method used for online banking is to ask 
the user for three random characters from a passcode. For 
example, if the passcode was 531278, they may ask for the 
2nd, 3rd, and 5th characters; the expected reply would be: 
317.

The text file, keylog.txt, contains fifty successful login 
attempts.

Given that the three characters are always asked for in 
order, analyse the file so as to determine the shortest 
possible secret passcode of unknown length.
"""

possible_passcodes = set([])
before = dict()
after = dict()

def add_ordered(b, a):
    if b not in after:
        after[b] = set([])
    if a not in before:
        before[a] = set([])
    before[a].add(b)
    after[b].add(a)
    
if __name__ == '__main__':
    inp = open('p079_keylog.txt')
    for line in inp:
        add_ordered(line[0], line[1])
        add_ordered(line[1], line[2])
        add_ordered(line[0], line[2])
    inp.close()
    ob = [s for s in before.values()]
    ob.sort(key=len)
    rc = []
    for s in ob:
        print s
        t = set(rc)
        s = s.difference(t)
        assert len(s) == 1
        rc.append(s.pop())
    print rc
    
    