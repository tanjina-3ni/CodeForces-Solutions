# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:15:56 2021

@author: Aspire
"""

n = list(map(int, input().split()))
a = max(n)
n = [a - i for i in n]
n.remove(0)
print(' '.join(map(str, n)))