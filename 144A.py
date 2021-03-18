# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:59:30 2021

@author: Aspire
"""

n = input()

line = list(map(int, input().split()))

min_swap = len(line) - (line[::-1].index(min(line)))

max_swap = line.index(max(line)) + 1

if min_swap < max_swap:
    res = len(line) - min_swap + max_swap - 2
else:
    res = len(line) - min_swap + max_swap - 1

print(res)