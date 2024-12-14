# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:22:06 2024

@author: Ken
"""
from sqlFunctions import viewClasses

def mainMenu():
    print("\n---MAIN MENU---")
    print("\nWhat would you like to do today? Input the number of your choice:")
    print("\n1 to View Records, \n2 to Create Records, \n3 to Update Records, \n4 to Drop Records, \n9 to quit the program.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        viewRecords()
    elif menuInput == 2:
        createRecords()
    elif menuInput == 3:
        updateRecords() 
    elif menuInput == 4:
        dropRecords() 
    elif menuInput == 9:
        raise SystemExit #quit the program
    else:
        print("\nSorry, invalid input. Please try again!")
        mainMenu()
        
def viewRecords():
    print("\n -- VIEW RECORDS MODULE --")
    print("\nPlease select an option:")
    print("\n1 to View Classes, \n2 for students, \n3 for enrolled classes, \n4 for professors, \n5 for deparments, \n9 to return to main menu.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        viewClasses()
        pass
    elif menuInput == 2:
        #viewStudents()
        pass
    elif menuInput == 3:
        #viewEnrollments()
        pass
    elif menuInput == 4:
        #viewProfessors()
        pass
    elif menuInput == 9:
        #viewDepartments()
        pass
    else:
        print("\nSorry, invalid input. Please try again!")
      
def createRecords():
    pass

def updateRecords():
    pass

def dropRecords():
    pass