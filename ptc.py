import math
import os
import random
import re
import sys
import itertools

# Complete the 'formingMagicSquare' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.

s = []
for i in range(3):
    s.extend(list(map(int, input().split(" "))))
min_cost = 1000
best = None
def is_magic(s):
    for i in range(3):
        if sum(s[i*3:i*3+3]) != 15:
            return False
        if sum(s[i::3]) != 15:
            return False
    if s[0] + s[4] + s[8] != 15:
        return False
    if s[2] + s[4] + s[6] != 15:
        return False
    return True
for p in itertools.permutations(range(1,10)):
    cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
    if cost < min_cost and is_magic(p):
        min_cost = cost
        best = p       
print(min_cost)