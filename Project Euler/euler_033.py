# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 00:50:04 2016

@author: Steve
"""

if __name__ == '__main__':
    for n in range(10, 100):
        for d in range(n+1, 100):
            # skip any n,d that don't have a common digit
            n_digits = [n/10, n%10]
            d_digits = [d/10, d%10]
            common = None
            if d/10 in n_digits:
                common = d/10
            if d%10 in n_digits:
                common = d%10
            if common:
                # There's a common digit and it isn't 0
                # (0 would make this "trivial")
                n_digits.remove(common)
                d_digits.remove(common)
                cn = n_digits[0]
                cd = d_digits[0]
                if cd > 0:
                    f1 = float(n)/float(d)
                    f2 = float(cn)/float(cd)
                    if f1 == f2:
                        print n,d,cn,cd, f1
            