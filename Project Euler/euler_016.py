# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:10:34 2016

@author: srowe
"""

digits = str(2 ** 1000)
t = 0
for c in digits:
    t += int(c)

print t
