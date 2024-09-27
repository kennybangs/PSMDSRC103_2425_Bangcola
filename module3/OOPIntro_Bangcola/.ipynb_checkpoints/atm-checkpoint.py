# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:45:05 2024

@author: Ken
"""

class atm():
    #constructor
    
    def __init__(self, serial_number, account_current_balance):
        self.account_current_balance = account_current_balance
        self.serial_number = serial_number
    
    #erial_number = 0

    def deposit(self, account, amount):
        self.account_current_balance = self.account_current_balance + amount
        print("Deposit Complete")

    def withdraw(self, account, amount):
        self.account_current_balance = self.account_current_balance - amount
        print("Withdraw Complete")

    def check_current_balance(self, account):
        print(self.account_current_balance)