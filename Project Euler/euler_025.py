# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:52:11 2016

@author: srowe
"""
fib_cache = [0]*100000

def fib(n):
    if n <= 2:
        return 1
    return ffib(n-1) + ffib(n-2)
    
def ffib(n):
    if fib_cache[n] == 0:
        fib_cache[n] = fib(n)
        
    return fib_cache[n]

def digits(n):
    return len(str(n))
    
if __name__ == '__main__':
    n = 100
    while digits(ffib(n)) < 1000:
        n += 1

    print n, ffib(n)                