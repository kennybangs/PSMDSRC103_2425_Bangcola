# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:38:16 2024

@author: Ken
"""
import mariadb
import sys
from tabulate import tabulate

"""
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="finals_db"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
"""
#def connectServer():
# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="finals_db"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

def getTableHeaders(tableName):
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tableName}'")
    tableHeaders = cur.fetchall()
    
    #prepare list of table headers for proper display in tabulate
    headersList = []
    
    for x in tableHeaders:
        headersList.append(x[0])
        
    return headersList
    
def renderResults(result,tableName):
    #insert table headers at start of result list for display
    result.insert(0,getTableHeaders(tableName))
    table = tabulate(result) 
    print(table)

def viewClasses():
    print("\nFetching list of classes...")
    cur.execute("SELECT * FROM V_CLASSES")
    result = cur.fetchall()
    renderResults(result,"V_CLASSES")

def viewStudents():
    print("\nFetching list of students...")
    cur.execute("SELECT * FROM V_STUDENTS")
    result = cur.fetchall()
    renderResults(result,"V_STUDENTS")

def viewProfessors():
    print("\nFetching list of professors...")
    cur.execute("SELECT * FROM V_PROFESSORS")
    result = cur.fetchall()
    renderResults(result,"V_PROFESSORS")

def viewDepartments():
    print("\nFetching list of departments...")
    cur.execute("SELECT * FROM V_DEPARTMENTS")
    result = cur.fetchall()
    renderResults(result,"V_DEPARTMENTS")
    
def viewEnrollments():
    print("\nFetching list of enrollments...")
    cur.execute("SELECT * FROM V_ENROLLMENTS")
    result = cur.fetchall()
    renderResults(result,"V_ENROLLMENTS")



conn.commit()
conn.close()
