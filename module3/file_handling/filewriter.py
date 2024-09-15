# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:27:46 2024

@author: Ken
"""

name = "Ken Bangcola"  # Modify by writing your name here.
file = open("newfile1.txt", 'w')
file.write(f"Hello, {name}!\n")
file.write("Isn't this amazing?\n")
file.write("that we can create and write on text files\n")
file.write("using Python.")
file.close()

file = open("newfile2.txt", 'w')
file.write("This message was created using Python!\n")
file.close()
