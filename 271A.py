# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:38:55 2021

@author: Aspire
"""

n = input()

i = int(n)+1

while(1):
    if len(str(i)) == len(set(str(i))):
        print(i)
        break
    else:
        i = i + 1

