# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 16:10:31 2021

@author: Aspire
"""

n =  int(input())

for i in range(0,n):
    string =  input()
    length = len(string)
    if length>10:
        print(string[0]+str(length-2)+string[length-1])
    else:
        print(string)