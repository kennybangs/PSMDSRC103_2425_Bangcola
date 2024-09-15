# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:38:25 2024

@author: Ken
"""

"""
#version 1

def generate_truthtable(number_of_variables):
    total_combinations = 2 ** number_of_variables
    combinations_list = []

    for i in range(total_combinations):
        bin_equivalent = bin(i)[2:]

        while len(bin_equivalent) < number_of_variables:
            bin_equivalent = "0" + bin_equivalent
        combinations_list.append(tuple(int(val) for val in bin_equivalent))

    return combinations_list

print(generate_truthtable())

"""

def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0:
        return "You need to enter an integer"
    else:
        total_combinations = 2 ** number_of_variables
        combinations_list = []

        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:]
            while len(bin_equivalent) < number_of_variables:
                bin_equivalent = "0" + bin_equivalent
            combinations_list.append(tuple(int(val) for val in bin_equivalent))

        return combinations_list
    
#print(generate_truthtable(3))

def evaluate_propositional_logic(combinations_list):
    expression = input("Enter the propositional logic expression: ")

    if variables == 2:
        print("A B f")
        for A, B in combinations_list:
            evaluated_expression = eval(expression)
            print(A, B, evaluated_expression)
    elif variables == 3:
        print("A B C f")
        for A, B, C in combinations_list:
            evaluated_expression = eval(expression)
            print(A, B, C, evaluated_expression)
            
evaluate_propositional_logic(generate_truthtable(3))