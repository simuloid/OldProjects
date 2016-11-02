# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 10:33:47 2016

@author: srowe

XOR decryption
Problem 59
Each character on a computer is assigned a unique code and the 
preferred standard is ASCII (American Standard Code for Information 
Interchange). For example, uppercase A = 65, asterisk (*) = 42, and 
lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes 
to ASCII, then XOR each byte with a given value, taken from a secret 
key. The advantage with the XOR function is that using the same 
encryption key on the cipher text, restores the plain text; for 
example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain 
text message, and the key is made up of random bytes. The user would 
keep the encrypted message and the encryption key in different 
locations, and without both "halves", it is impossible to decrypt 
the message.

Unfortunately, this method is impractical for most users, so the 
modified method is to use a password as a key. If the password is 
shorter than the message, which is likely, the key is repeated 
cyclically throughout the message. The balance for this method is 
using a sufficiently long password key for security, but short 
enough to be memorable.

Your task has been made easy, as the encryption key consists of 
three lower case characters. Using cipher.txt (right click and 
'Save Link/Target As...'), a file containing the encrypted ASCII 
codes, and the knowledge that the plain text must contain common 
English words, decrypt the message and find the sum of the ASCII 
values in the original text.
"""

import re
from itertools import *
  
def decode(msg, key):
    rc = []
    for c, k in zip(msg, key):
        x = c ^ k
#        print c, k, x, chr(x)
        rc.append(x)

    return ''.join(chr(i) for i in rc), sum(rc)
    
if __name__ == '__main__':
    lc_letters = [ord(c) for c in 'abcdefghijklmnopqrstuvwxyz']
    f = open('p059_cipher.txt')
    ct = f.read()
    f.close()
    f = open('p042_words.txt')
    s = f.read()
    f.close()
    out = open('out.txt', 'w')
    s = re.sub('"','', s)
    words = s.split(',')
    ascii = [int(d) for d in ct.split(',')]

    counter = 0
    for key in permutations(lc_letters, 3):
#        print key
        s, t = decode(ascii, key*int(len(ct)/3+1))
        real_words = []
        for w in set(s.split(' ')):
            if len(w) > 2 and w.upper() in words:
                real_words.append(w)
                
        if len(real_words) > 3:
            print ''.join(chr(c) for c in key)
            print real_words
            print s
            print 'Sum of chars: ', t
#        out.write(str(key)+"\n")
#        out.write(s+"\n")
        
    out.close()
