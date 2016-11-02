# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 22:09:48 2016

@author: Steve

Square digit chains
Problem 92
A number chain is created by continuously adding the square of the digits in 
a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
loop. What is most amazing is that EVERY starting number will eventually 
arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

s89 = set([89,145,42,20,4,16,37,58])
s01 = set([1])

def make_chain(n):
    global s89 
    global s01 
    rc = []
    seen = set()
    while n not in seen:
        rc.append(n)
        seen.add(n)
        temp = [int(d)*int(d) for d in str(n)]
        n = sum(temp)
        if n in s01:
            for e in rc:
                s01.add(e)
            return False
        if n in s89:
            for e in rc:
                s89.add(e)
            return True

    rc.append(n)
    return False

c89 = 0    
for i in range(10000000):
    if make_chain(i):
        c89 += 1
        
print c89