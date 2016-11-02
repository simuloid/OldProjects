# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:07:33 2016

@author: srowe
"""

def terms(ma, mb):
    rc = set([])
    for a in range(2, ma+1):
        for b in range(2, mb+1):
            v = a ** b
            rc.add(v)
    return sorted(rc)
    
if __name__ == '__main__':
    t = terms(100, 100)
    print len(t), t
