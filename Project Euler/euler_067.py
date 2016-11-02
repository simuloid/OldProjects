# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:53:51 2016

@author: srowe
"""

# This will require dynamic programming

# For each row, assume it got there by taking the most profitable
# path that can get it there.
#
#       3
#     7   4
#   2   4   6
# 8   5   9   3
#
# becomes
#        3
#     10  7
#   12  14  13
# 20  17  23  16
#
#       75
#     170 139
#   187 217 221
#
lil_triangle=[
[3],
[7,4],
[2,4,6],
[8,5,9,3]
]

triangle = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20, 4,82,47,65],
[19, 1,23,75, 3,34],
[88, 2,77,73, 7,63,67],
[99,65, 4,28, 6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
[04,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]
]

def read_triangle():
    global triangle
    triangle = []
    f = open('p067_triangle.txt')
    for line in f:
        row = [int(s) for s in line.split(' ')]
        triangle.append(row)
    f.close()
        
# Return the list of parent values for the given r,c
def parents(r, c, t=triangle):
    # r is measured from the top and is 0 based
    # c is measured from the left and is 0 based
    rc = []
    # top has no parents
    if r == 0:
        return rc
    # edges have only 1 parent
    if c == 0:
        rc.append(t[r-1][0])
    elif c == len(t[r])-1:
        rc.append(t[r-1][-1])
    else:
        # Everything else has 2 parents
        rc.append(t[r-1][c-1])
        rc.append(t[r-1][c])
        
    return rc
    
def flow_down(t = triangle):
    for r, row in enumerate(t):
        for c, value in enumerate(row):
            p = parents(r, c, t)
            v = value
            if len(p) > 0:
                v = v + max(p)
            t[r][c] = v

if __name__ == '__main__':
    read_triangle()
    t = triangle
    print t[-1]
    flow_down(t)
    print max(t[-1])