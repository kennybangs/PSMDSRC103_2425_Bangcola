#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:12:38 2024

@author: kbangcola
"""

#initialize badWords
badWordsList = []
    
def notEmptyCheck(a):
    return len(str(a)) > 0

def inputLoopString(prompt):
    
    validInput = False #set flag to retry input if input is invalid
    
    #begin input looop

    while validInput == False: 
        try:
            userInput = str(input(prompt))
            if notEmptyCheck(userInput): 
                return userInput
                validInput = True
            else:
                print("ERROR: Values must not be not empty.")
        except ValueError:
            print ("ERROR: Input must be a valid string!") #restrat loop if empty 
                                
    #end input loop
    
def censor(sentence=''):        
    sentence = inputLoopString("Input the sentence you want to censor: ").lower()
        
    if len(badWordsList) <= 0: #check if badwords list is empty
        print("\nError: Bad words blacklist empty! Please input some bad words first.")
        print("Returning to main menu...")
        mainMenu()
    else: #if blacklist is not empty, proceed
        tempSentenceCensored = sentence #initialize temp variable for censor loop
        
        #begin censorship loop
        
        print("\nCensoring against blacklist...")
        for x in badWordsList: #loop through each word in the blacklist
            #debug
            #print("Now censoring " + x)
            if tempSentenceCensored.find(x) == -1: #if bad word not found in setence, skip it
                #debug
                print(x + "not found. Skipping.")
                pass 
            else:
                #debug
                #print(x + " found. Censoring...")
                #print("Sentence to censor: " + tempSentenceCensored)
                
                beginBadWord = sentence.find(x) #return start of bad word in sentence
                endBadWord = beginBadWord+len(x) #ending of bad word in sentence
                
                #debug 
                #print("Beginning of bad word: " + str(beginBadWord))
                #print("Ending of bad word: " + str(endBadWord))
                
                for y in range(len(x)): #loop through each char of the word to replace with *
                    #print("Substituting character #" + str(y) + " at position " + str(beginBadWord + y)) 
                    tempSentenceCensored = tempSentenceCensored[:beginBadWord + y] + '*' + sentence[endBadWord:]                    
                    #print(tempSentenceCensored)
                
                sentence = tempSentenceCensored #sasve the temp sentence as the final sentence
                
        #end censorship loop        
        
        print("\nYour censored sentence is: ")
        print(sentence)
                            
            #debug stuff
            #print(beginBadWord) #need to add case when word not found
            #print(endBadWord)
            #print(sentence[:beginBadWord])
            #sentenceCensored = sentence[beginBadWord:(beginBadWord+len(x))]
            #print(sentenceCensored)
                                
def mainMenu():
    print("\nWhat would you like to do today? Input the number of your choice:")
    print("\n1 to censor a sentence, \n2 to add words to the blacklist, \n3 to view the blacklist, \n4 to quit the program.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        censor()
    elif menuInput == 2:
        inputWords()
    elif menuInput == 3:
        displayWords() 
    elif menuInput == 4:
        raise SystemExit #quit the program
    else:
        print("\nSorry, invalid input. Please try again!")
        mainMenu()

def inputWords():
    print("\n-- Bad word input module --")
    print("Current list of bad words to censor: ")
    
    displayWords()
    
    print("\nNow inputting bad words to blacklist. Input your word and press Enter. To quit input, type 'done' and press enter.")
           
    #begin input looop
    
    validInput = False #set flag to continue input loop
    
    while validInput == False: 
        userInput = str(input("\nPlease input bad word [input 'done' to finish inputting.']: "))
        if notEmptyCheck(userInput): #check first if input is not empty
            if userInput.lower() != 'done': #check if user wants to quit input
                badWordsList.append(userInput)
                print("Added word " + userInput +" to blacklist.")
            else: #exit loop if input is string and not empty
                validInput = True
        else: #restart loop if input is empty
            print("ERROR: Input must not be not empty.")
    
    #return to main menu
    print("\nReturning to main menu.")
    
def displayWords():
    print("\n--START OF BAD WORDS BLACKLIST--")
    
    for x in badWordsList: 
        print("\n" + x)
        
    print("\n--END OF BAD WORDS BLACKLIST--")
