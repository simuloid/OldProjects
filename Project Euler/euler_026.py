# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:09:27 2016

@author: srowe
"""
from math import log10

def extended_fraction(denominator):
    ans = ''
    remainder = 10
    past_remainders = set([])
    ans_by_remainder = {}
    
    while True:
        if remainder in past_remainders:
            break
        past_remainders.add(remainder)
        ans_by_remainder[remainder] = ans
        if denominator > remainder:
            ans = ans + '0'
            remainder = remainder * 10
        else:
            q = int(remainder / denominator)
            ans = ans + str(q)
            remainder = 10 * (remainder % denominator)
            
    repeating_part = ''
    
    if remainder > 0:
        # zp is where the repeating pattern starts
        # since the remainder is the same as it was
        # when the repeating pattern started, we can
        # deduce how many digits preceed the pattern.
        zp = len(ans_by_remainder[remainder])
        repeating_part = ans[zp:]
        if zp > 0:
            ans = '0.' + ans[:zp] + '(' + repeating_part + ')'
        else:
            ans = '0.' + '(' + ans + ')'
    else:
        ans = '0.' + ans[:-1]
        
        
    return ans, remainder, repeating_part    

if __name__ == '__main__':
    biggest_r = ''
    biggest_i = 0
    for i in range(2,10000):
        a,x,r = extended_fraction(i)
#        print i,a,x,len(r)
        if x > 0 and r and len(r) > len(biggest_r):
            biggest_r = r
            biggest_i = i
    print biggest_i, 'gives', biggest_r