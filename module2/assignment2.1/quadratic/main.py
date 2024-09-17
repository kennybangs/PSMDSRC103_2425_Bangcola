#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:06:53 2024

@author: kbangcola

Create a quadratic equation solver module that would write the inputs 
of the user and the corresponding output into text files.

"""

import math

def notEmptyCheck(a):
    return len(str(a)) > 0

def inputLoopFloat(prompt):
    
    validInput = False #set flag to retry input if input is invalid
    
    #begin input looop

    while validInput == False: 
        try:
            userInput = float(input(prompt))
            if notEmptyCheck(userInput): 
                return userInput
                validInput = True
            else:
                print("ERROR: Values must not be not empty.")
        except ValueError:
            print ("ERROR: Input must be a valid number!") #restrat loop if empty 

def quadratic_formula(a, b, c):
    if b**2 - (4*a*c) < 0:
        x1 = (complex(-b, math.floor(math.sqrt(abs(b**2-(4*a*c)))))) / (2*a)
        x2 = (complex(-b, -1*math.floor(math.sqrt(abs(b**2-(4*a*c)))))) / (2*a)
        return x1, x2
    else:
        x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
        x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
        return x1, x2

inputA = inputLoopFloat("Please enter the value for variable a: ")
inputB = inputLoopFloat("Please enter the value for variable b: ")
inputC = inputLoopFloat("Please enter the value for variable c: ")
result = quadratic_formula(inputA, inputB, inputC)
print("Now solving...")
print("The values of x are: ")
print(result)
print("\nNow saving results to file 'results.txt'...")

file = open("results.txt", 'w')

file.write("Quadratic Equation solved:")
file.write("\nValues of a, b, c:")
file.write("a = " + str(inputA))
file.write("b = " + str(inputB))
file.write("c = " + str(inputC))
file.write("\nValues of x:")
file.write(str(result))
file.close()

print("Done saving file!")