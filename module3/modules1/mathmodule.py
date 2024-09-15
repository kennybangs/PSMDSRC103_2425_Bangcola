# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:07:43 2024

@author: Ken
"""

import math

def quadratic_formula(a, b, c):
    if b**2 - (4*a*c) < 0:
        x1 = (complex(-b, math.floor(math.sqrt(abs(b**2-(4*a*c)))))) / (2*a)
        x2 = (complex(-b, -1*math.floor(math.sqrt(abs(b**2-(4*a*c)))))) / (2*a)
        return x1, x2
    else:
        x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
        x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
        return x1, x2

print(quadratic_formula(1,2,3))