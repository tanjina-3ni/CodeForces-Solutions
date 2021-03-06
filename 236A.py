# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:36:06 2021

@author: Aspire
"""

username = input()
liist = []

for i in range(0,len(username)):
    if username[i] not in liist:
          liist.append(username[i])  
if len(liist)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
