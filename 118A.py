# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 00:11:22 2021

@author: Aspire
"""

string = input()

vowels = 'AOYEUIaoyeui'
for char in vowels:
    string = string.replace(char,"")

string = string.lower()
string='.' + '.'.join(string)
print(string)