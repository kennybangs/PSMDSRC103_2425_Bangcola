# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:45:05 2024

@author: Ken
"""

class ATM():
    #constructor
    
    def __init__(self, serial_number, account_current_balance):
        self.account_current_balance = account_current_balance
        self.serial_number = serial_number
    
    #erial_number = 0
    
    def write_transaction(self, message):
        file = open("txn_log2.txt", 'a')
        file.write(message)
        return "Transaction appended to txn_log.txt"

    def deposit(self, account, amount):
        self.account_current_balance = self.account_current_balance + amount
        print("Deposit Complete")
        self.write_transaction("\nDeposit Complete")

    def withdraw(self, account, amount):
        self.account_current_balance = self.account_current_balance - amount
        print("Withdraw Complete")
        self.write_transaction("\nWithdraw Complete")

    def check_currentbalance(self, account):
        print(self.account_current_balance)
        self.write_transaction("\nCurrent Balance: " + str(self.account_current_balance))
        
    def display_serialnumber(self):
        print("The serial number of this ATM is: " + str(self.serial_number))
        self.write_transaction("\nThe serial number of this ATM is: " + str(self.serial_number))
        
    def view_transactionsummary(self):
        file = open("txn_log2.txt", 'r')
        data = file.read()
        print(data)
        file.close() 
        
"""
class ATM():
    serial_number = 0

    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")

    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete")

    def check_currentbalance(self, account):
        print(account.current_balance)

"""

