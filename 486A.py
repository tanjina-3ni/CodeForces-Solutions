# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:13:44 2021

@author: Aspire
"""

import math
n = int(input())

f = 0

if n%2 == 0:
    f = int(n/2)
else:
    f = -math.ceil(n/2)
        
print(f)