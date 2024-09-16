#Group 4:
#Karim Bangcola Jr
#Raymond Enague
#Ivan Villena

#create empty dict to hold events
eventGuestDictionary = {} 

#define function to get factorial of number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#define function to get total guests of all events
def total_guests():
    sumOfGuests = sum(eventGuestDictionary.values())
    return sumOfGuests

#define function to get fibonacci number of n
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#get input from user of events
print("Hello! Please input the number of events you want to input: ") 

userEventNumberInput = int(input("Number of events: "))

#store events and guests in dict

for x in range(userEventNumberInput):
    userEventInput = input("Name of Event: ")
    userGuestInput = int(input("Number of guests for event " + userEventInput + ": "))
    eventGuestDictionary[userEventInput] = userGuestInput
    
#print(eventGuestDictionary) 

print("The total 1number of guests for all events is: " + str(total_guests()))

for x in eventGuestDictionary:
    #store dictionary keys as list so we can get index for fibonacci function
    eventGuestDictionaryKeys = list(eventGuestDictionary.keys())
    #calculate possible seating arrangements per event
    print("The total number of seating arragements for event " + x + " is " + str(factorial(eventGuestDictionary[x])))
    #calculate Fibonnaci number of each event based on order of input
    #note: added +1 to index since indices start 0 and f(0) is 0
    print("Based on the Fibonacci sequence, the priority of event " + x + " is " + str(fibonacci(eventGuestDictionaryKeys.index(x)+1)))