# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:19:19 2024

@author: Ken
"""

import time

def pause():
    for i in range(10, 0, -1):
        print(f"The program will end in {i}...")
        time.sleep(1)
        
#pause()

def current_time():
    t = time.strftime("%I:%M %p")
    return t

def current_date():
    d = time.strftime("%b %d %Y")
    return d

print(current_time())
print(current_date())

