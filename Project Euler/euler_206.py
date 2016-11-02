# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 23:07:22 2016

@author: Steve

Concealed Square
Problem 206
Find the unique positive integer whose square has the 
form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
import re

for guess in range(1010101010, 1389026624, 10):
    sq = guess*guess
    if re.match('1.2.3.4.5.6.7.8.9.0', str(sq)):
        print guess, sq
        