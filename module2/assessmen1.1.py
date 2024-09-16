#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:56:10 2024

@author: kbangcola

1. Create a dictionary to contain a pair of values, an ID number and a list containing user details, such as name, height, weight and BMI.

2. Create functions that can perform the following tasks:

2a) Add an element to the dictionary with its new ID# and aforementioned details,

2b) Print a specific user ID, and

2c) Print all details contained.

3. Consider the following edge cases and show how you're able to solve them in your code:

3a) What if the new values to add to the dictionary has duplicate values?

3b) How are you handling empty values that the user inputs? - while loop

3c) Are you able to handle cases wherein height or weight have non-numeric values?

3d) How do you handle the situation where the ID# for the print user function is not passed a valid ID?
    
"""

#initialize empty dict
userDict = {}

#initialize last generated userID
lastUserID = 1

#initialize list of user properties to use
userDetailsList = ["Name","Height","Weight","BMI"]
#user details that must be numeric. used for input checking later on
userDetailsListNumeric = ["Height","Weight","BMI"]

#helper function to check if input is not empty

def notEmptyCheck(a):
    return len(str(a)) > 0

#helper function to cycle through userDict

def displayUserDictValues(userID):
    y = 0
    for x in userDetailsList:
        print(x + ": " + userDict[userID][y])
        y = y+1    

#menu function
def mainMenu():
    print("\nGood day! In tis program, you may add users to a database, read user details, or edit them.")
    print("What would you like to do today? Input the number of your choice: 1 for add user, 2 for read user.")
    print("To quit the program, type 4.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        inputUsers()
    elif menuInput == 2:
        readUsers()
    #elif menuInput == 3:
    #    editUsers() 
    elif menuInput == 4:
        raise SystemExit #quit the program
    else:
        print("\nSorry, invalid input. Please try again!")
        mainMenu()
        
#input function to add entries to dict
def inputUsers():
    tempUserList = [] #blank list to hold user details temporarily
    #print("\nCurrently inputting a user with autogenerated ID of " + str(lastUserID) + ".") 
    
    idInput = int(input("Please input an integer ID number: "))
    print ("\nUser details to collect: " + " for ID number: " + str(idInput))
    
    for x in userDetailsList: #display details to collect from userDetailsList
        print(x)
    
    for x in userDetailsList: #cycle through userDetailsList and collect info for each
    
        #begin input looop
        
        validInput = False #set flag to retry input if input is invalid
        
        while validInput == False: 
            userInput = input("\nPlease input value for " + x + ": ")
            if notEmptyCheck(userInput): #check first if input is not empty
                #if input is not empty, check if input is numeric. if not, skip to exit while loop
                if x in userDetailsListNumeric:
                    try:
                        int(userInput) #check if input is numeric, if not do ValueError
                        if int(userInput) > 0: #check if input is > 0
                            validInput = True
                        else: #restart input loop if <= 0
                           print("ERROR: " + x + " must be greater than zero. Try again." )
                    except ValueError: #restrat input loop if not numeric
                        print("ERROR: " + x + " must be numeric. Try again." )
                else: #exit loop if input is string and not empty
                    validInput = True
            else: #restart loop if input is empty
                print("ERROR: Values must not be not empty.")
                
        #end input loop
                
        tempUserList.append(userInput) #add ID and details to dict if inputs are valid
        
    #print(tempUserList) #debug
    
    #append userId and detailsList to userDict:
    
    userDict[idInput] = tempUserList
    
    #send success message and summarize input
    print("\nSuccesfully added user ID " + str(idInput) + " to database with following details:" )
    
    #cycle through inputted details
    displayUserDictValues(idInput)
    
    #return to main menu
    print("\nReturning to main menu.")
    
    mainMenu()

#function to display entries from dict 
def readUsers():
    print("\nUSER DATA RETRIEVAL:")
    
    #print("\nIn this module, you may 1) display all user IDs in the database, 2) search for a specific ID, 3) display ALL IDs and associated details, or 4) return to main menu.")
    print("\nInput the number of your choice: 1 to display all user IDs, 2 to search for a specific ID, 3 to display all users and details, 4 to return to main menu.")
    menuInput = int(input(("\nPlease select an option: " ))) 
    
    if menuInput == 1: #display all user IDs
        print("\nAvailable user IDs: ")
        for x in userDict:
            print("\n" + str(x))
        print("--END OF USER IDs--")
        
    elif menuInput == 2: #display specific user ID
        menuInput = int(input("Please enter user ID to search against: "))
        
        if menuInput in userDict:
            print("User ID: " + str(menuInput))
            displayUserDictValues(menuInput)
        else:
            print("Error! User ID " + str(menuInput) + " not found in database. Please try again.")
            readUsers() #retun to menu
        
    elif menuInput == 3: #display all users and details
        print("\nAvailable user IDs and details: ")
        
        for a in userDict: #cycle through each key of userDict
            print("\nUser ID: " + str(a)) #print keys
            displayUserDictValues(a) #print values

    elif menuInput == 4: #return to main menu
        mainMenu()
    
    #return to data retrieval menu
    readUsers()

#function to display entries from dict 
def editUsers():
    print("Feature not yet implemented!")
    mainMenu()
    pass

mainMenu()



