# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:08:30 2021

@author: Aspire
"""

s = input()

low = 'abcdefghijklmnopqrstuvwxyz'
high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = 0
h = 0
for i in range(0,len(s)):
    if s[i] in low:
        l = l + 1
    else:
        h = h + 1
if l>=h:
    s = s.lower()
else:
    s = s.upper()
print(s)