# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:33:21 2024

@author: Ken
"""

file = open("newfile2.txt", 'r')
data = file.read(12)
print(data)
file.close()