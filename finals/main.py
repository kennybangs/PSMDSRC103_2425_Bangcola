# -*- coding: utf-8 -*-

# Module Imports
import mariadb
import sys
from tabulate import tabulate

#from menuFunctions import mainMenu
#import sqlFunctions 
useDatabase = 'finals_db'
# Get Cursor
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database=useDatabase

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

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
        conn.close()
        raise SystemExit #quit the program
    else:
        print("\nSorry, invalid input. Please try again!")
        mainMenu()
        
def viewRecords():
    print("\n -- VIEW RECORDS MODULE --")
    print("\nPlease select an option:")
    print("\n1 to View Classes, \n2 for Students, \n3 for enrolled classes, \n4 for professors, \n5 for deparments, \n9 to return to main menu.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        retrieveRecords("V_CLASSES","classes")
    elif menuInput == 2:
        retrieveRecords("V_STUDENTS","students")
    elif menuInput == 3:
        retrieveRecords("V_ENROLLMENTS","enrollments")
    elif menuInput == 4:
        retrieveRecords("V_PROFESSORS","professors")
    elif menuInput == 5:
        retrieveRecords("V_DEPARTMENTS","departments")  
    elif menuInput == 9:
        mainMenu()
        pass
    else:
        print("\nSorry, invalid input. Please try again!")
      
def createRecords():
    print("\n -- CREATE RECORDS MODULE --")
    print("\nPlease select an option:")
    print("\n1 to Create Student, \n2 to Create Class,\n3 to Enroll Student in Class, \n9 to return to main menu.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        tableName = "students"
        inputList = []
        outputList = []
        headers = getTableHeaders(tableName)
        print("f\nPlease fill in the required fields for {tableName}: ")
        
        for header in headers:
            if checkAutoIncrement(header, tableName):
                pass
            else:
                if checkDataType(header, tableName, 'int'):
                    inputList.append(int(input((f"\n {header} : " ))))
                else:
                    inputList.append(input((f"\n {header} : " )))
        
        outputList.append(headers[1:])
        outputList.append(inputList)
        print(outputList)
        
        student = dataRecord(outputList,tableName)
        student.showValues()
        student.pushNewRecord()
    elif menuInput == 2:
        tableName = "classes"
        inputList = []
        outputList = []
        headers = getTableHeaders(tableName)
        print(f"\nPlease fill in the required fields for {tableName}: ")
        
        for header in headers:
            if checkAutoIncrement(header, tableName):
                pass
            else:
                if checkDataType(header, tableName, 'int'):
                    inputList.append(int(input((f"\n {header} : " ))))
                else:
                    inputList.append(input((f"\n {header} : " )))
        
        outputList.append(headers[1:])
        outputList.append(inputList)
        print(outputList)
        
        student = dataRecord(outputList,tableName)
        student.showValues()
        student.pushNewRecord()
    elif menuInput == 3:
        tableName = "enrollments"
        inputList = []
        outputList = []
        headers = getTableHeaders(tableName)
        print(f"\nPlease fill in the required fields for {tableName}: ")
        
        for header in headers:
            if checkAutoIncrement(header, tableName):
                pass
            else:
                if checkDataType(header, tableName, 'int'):
                    inputList.append(int(input((f"\n {header} : " ))))
                else:
                    inputList.append(input((f"\n {header} : " )))
        
        outputList.append(headers)
        outputList.append(inputList)
        print(outputList)
        
        student = dataRecord(outputList,tableName)
        student.showValues()
        student.pushNewRecord()
    else:
        print("\nSorry, invalid input. Please try again!")
        
def updateRecords():
    print("\n -- UPDATE RECORDS MODULE --")
    print("\nPlease select an option:")
    print("\n1 to Update Class Details, \n2 to Update Student Details, \n3 Update Enrolled Classes, \n9 to return to main menu.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        tableName = "classes"
        filterField = "CLASS_NUMBER"
        filterValue = int(input((f"\nWhich {filterField} would you like to edit? " )))
        retrieveFilteredRecords(tableName, filterField, filterValue)
        student = dataRecord(retrieveFilteredRecords(tableName, filterField, filterValue),tableName)
        student.showHeaders()
        fieldName = input("\nWhich field name would you like to edit? " )
        newValue = int(input("\nWhat will be the new value? "))
        student.changeValue(fieldName, newValue)
        student.pushUpdate(fieldName, filterField, filterValue)
        student.showValues() 
    elif menuInput == 2:
        tableName = "students"
        filterField = "STUDENT_ID"
        filterValue = int(input((f"\nWhich {filterField} would you like to edit? " )))
        retrieveFilteredRecords(tableName, filterField, filterValue)
        student = dataRecord(retrieveFilteredRecords(tableName, filterField, filterValue),tableName)
        student.showHeaders()
        fieldName = input("\nWhich field name would you like to edit? " )
        newValue = input("\nWhat will be the new value? ")
        student.changeValue(fieldName, newValue)
        student.pushUpdate(fieldName, filterField, filterValue)
        student.showValues() 
    elif menuInput == 3:
        tableName = "enrollments"
        filterField = "STUDENT_ID"
        filterValue = int(input((f"\nWhich {filterField} would you like to edit? " )))
        retrieveFilteredRecords(tableName, filterField, filterValue)
        student = dataRecord(retrieveFilteredRecords(tableName, filterField, filterValue),tableName)
        student.showHeaders()
        fieldName = input("\nWhich field name would you like to edit? " )
        newValue = input("\nWhat will be the new value? ")
        student.changeValue(fieldName, newValue)
        student.pushUpdate(fieldName, filterField, filterValue)
        student.showValues()
    elif menuInput == 9:
        mainMenu()
        pass
    else:
        print("\nSorry, invalid input. Please try again!")

def dropRecords():
    print("\n -- DELETE RECORDS MODULE --")
    print("\nPlease select an option:")
    print("\n1 to Drop Student from Class, \n9 to return to main menu.")
    menuInput = int(input(("\nPlease select an option: " )))
    
    if menuInput == 1:
        tableName = "enrollments"
        studentNumber = int(input("\nWhich student ID should be dropped? "))
        classNumber = int(input("\nFrom which class number? "))
        
        try:
            #print(f"DELETE FROM {tableName} WHERE student_id = {studentNumber} and class_number = {classNumber}")
            cur.execute(f"DELETE FROM {tableName} WHERE student_id = {studentNumber} and class_number = {classNumber}")
            conn.commit()
        except mariadb.Error as e: 
            print(f"Error: {e}")
    elif menuInput == 9:
        mainMenu()
    else:
        print("\nSorry, invalid input. Please try again!")

def getTableHeaders(tableName):
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tableName}' AND table_schema = '{useDatabase}'")
    tableHeaders = cur.fetchall()
    
    #prepare list of table headers for proper display in tabulate
    headersList = []
    
    for x in tableHeaders:
        headersList.append(x[0])
        
    return headersList

def convertList(inputList): #convert tuples to list
    outputList = []
    for item in inputList:
        outputList.append(list(item))
    
    return outputList
    
def renderResults(result):
    #result.insert(0,getTableHeaders(tableName))
    table = tabulate(result) 
    print(table)

def retrieveRecords(tableName,topic):
    print(f"\nFetching list of {topic}...")
    cur.execute(f"SELECT * FROM {tableName}")
    result = cur.fetchall()
    #insert table headers at start of result list for display
    result.insert(0,getTableHeaders(tableName))
    #return list of tuples
    renderResults(result)
    
def checkAutoIncrement(fieldName,tableName):
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tableName}' AND table_schema = '{useDatabase}' AND extra = 'auto_increment' and column_name = '{fieldName}'")
    result = cur.fetchall()
    
    #print(result)
    
    if len(result) == 0:
        return False
    else:
        return True

def checkDataType(fieldName,tableName,dataType):
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tableName}' AND table_schema = '{useDatabase}' and data_type = '{dataType}' and column_name = 'fieldName'")
    result = cur.fetchall()
        
    if len(result) == 0:
        return False
    else:
        return True
    
def retrieveFilteredRecords(tableName,filterField,filterValue):
    #returns a list of dicts of the result
    cur.execute(f"SELECT * FROM {tableName} WHERE {filterField} = {filterValue}")
    result = cur.fetchall()
    
    result.insert(0,getTableHeaders(tableName))
    
    return result
    
    """
    for x in tableHeaders:
        print(x)
        print(tableHeaders.index(x))
        resultDict[x] = result[0][tableHeaders.index(x)]

    return resultDict
    """
def update():
    pass 

class dataRecord():
    
    def __init__(self,dataList,tableName):
        self.dataList = convertList(dataList) #convert each item to a list since MariaDB outputs tuples as results
        self.tableName = tableName
        
    def showHeaders(self):
        for header in self.dataList[0]:
            print(header)
        return self.dataList[0]
        
    def showValues(self):
        renderResults(self.dataList)
                
    def changeValue(self,fieldName,newValue):
        tempDataList = []
        
        for x in self.dataList:
            tempDataList.append(x)
            
        summaryList = [['Old Value','New Value']]
        oldValues = []
        newValues = []
        fieldIndex = tempDataList[0].index(fieldName)
        print(fieldIndex)
                
        #change values
        for row in tempDataList[1:]: #exclude first item since its the headers
            row[fieldIndex] = newValue #replace value for desired field
            newValues.append(newValue) #store new values in a separate list for summary
        
        for x in self.dataList[1:]:
            oldValues.append(x[fieldIndex]) #store old values in a separate list for summary
            
        #show summary for confirmation
        print("Values successfully changed.")
        
        #self.dataList = tempDataList
        
    def pushUpdate(self,fieldName,filterField,filterValue):
        fieldIndex = self.dataList[0].index(fieldName)
        filterIndex = self.dataList[0].index(filterField)
        #print(f"\nUpdating column {fieldName} in table {self.tableName} to new value {newValue} WHERE {filterField} = {filterValue}.")
        #print(f"UPDATE {self.tableName} SET {fieldName} = {newValue} WHERE {filterField} = {filterValue}")
        for row in self.dataList[1:]: 
            try:
                cur.execute(f"UPDATE {self.tableName} SET {fieldName} = '{row[fieldIndex]}' WHERE {filterField} = {row[filterIndex]}")
                conn.commit()
            except mariadb.Error as e: 
                print(f"Error: {e}")
                
            #print(f"UPDATE {self.tableName} SET {fieldName} = '{row[fieldIndex]}' WHERE {filterField} = {row[filterIndex]}")
            #print(f"{fieldName} set to {row[fieldIndex]} wher2e {filterField} = {row[filterIndex]}")
        
    def pushNewRecord(self):
        for row in self.dataList[1:]:
            try:
                print(f"INSERT INTO {self.tableName} {str(tuple(self.showHeaders())).replace("'","")} VALUES {tuple(row)}")
                cur.execute(f"INSERT INTO {self.tableName} {str(tuple(self.showHeaders())).replace("'","")} VALUES {tuple(row)}")
                conn.commit()
            except mariadb.Error as e: 
                print(f"Error: {e}")
            #print(f"INSERT INTO {self.tableName} ({header}) VALUES ('{row[fieldIndex]})'")
            #conn.commit()
        
#print(retrieveFilteredRecords("students","student_id",21))
#print(retrieveFilteredRecords("enrollments","class_number",1))
#filterValue = int(input(("\nWhich Student ID would you like to edit?" )))
#student = dataRecord(retrieveFilteredRecords("students", "student_id", filterValue),"students")
#student.showValues()
#student.changeValue("EMAIL_ADDRESS","test@yahoo.com")
#student.showValues()
#student.pushUpdate("EMAIL_ADDRESS","STUDENT_ID",filterValue)
#print(checkAutoIncrement('class_number', 'student_id'))

while True:
   mainMenu() #only way to quit is to input 9 in main menu to raise SystemExit
