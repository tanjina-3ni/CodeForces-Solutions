# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:30:29 2021

@author: Aspire
"""
small = 'abcdefghijklmnopqrstuvwxyz'

string = input()
char = string[0]
new_str = "" 
  
for i in range(len(string)): 
    if i != 0: 
        new_str = new_str + string[i]
       
if char in small:
    char = char.upper()
string = char + new_str
print(string)