# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:15:41 2016

@author: srowe
"""
import re

def written_out(n):
    n = int(n)
    ones = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = [ 'none', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if (n < 20):
        return ones[n]
        
    if (n < 100):
        if n % 10 == 0:
            return tens[n/10]
        else:
            return tens[n/10] + '-' + written_out(n%10)
            
    if (n < 1000):
        if n % 100 == 0:
            return written_out(n/100) + ' hundred'
        else:
            return written_out(n/100) + ' hundred and ' + written_out(n%100)
    
    if (n == 1000):
        return 'one thousand'
        
def my_length(s):
    s = re.sub('[- ,]', '', s)
    return len(s)

if __name__ == '__main__':
    t = 0
    n = 1000
    for  i in range(1, n+1):
        t += my_length(written_out(i))
        
    print t
