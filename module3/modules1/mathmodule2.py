# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:17:09 2024

@author: Ken
"""

import math

def angle_demo():
    angle = math.sin(math.pi/2)

    # the default input is in radius
    # angle sin(90)-1 in degree == sin(pi/2)=1 in radians
    print(angle)

    # to make it convenient, convert it to radians
    angle = math.sin(math.radians(90))
    print(angle)

    # this is also similar for cosine and other trigonometric and hyperbolic function.
    
print(angle_demo())