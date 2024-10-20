# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:47:05 2024

@author: Ken
"""

import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=123456, account_firstname="Royce",
                             account_lastname="Chua", current_balance=1000,
                             address="Silver Street Quezon City",
                             email="roycechua123@gmail.com")
print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

Account2 = Accounts.Accounts(account_number=654321, account_firstname="John",
                             account_lastname="Doe", current_balance=2000,
                             address="Gold Street Quezon City",
                             email="johndoe@yahoo.com")

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

print("\nATM part:")
ATM1 = ATM.ATM('123456',100)
ATM1.deposit(Account1, 500)
ATM1.check_currentbalance(Account1)
ATM1.display_serialnumber()

ATM1.deposit(Account2, 300)
ATM1.check_currentbalance(Account2)
ATM1.display_serialnumber()

ATM1.view_transactionsummary()

"""
import accounts
import atm

Account1 = accounts.accounts(account_number=123456, account_firstname="Royce",
                             account_lastname="Chua", current_balance=1000,
                             address="Silver Street Quezon City",
                             email="roycechua123@gmail.com")

print("Account 1")
print(Account1.account_firstname)
print(Account1.account_lastname)
print(Account1.current_balance)
print(Account1.address)
print(Account1.email)

print()

Account2 = accounts.accounts(account_number=654321, account_firstname="John",
                             account_lastname="Doe", current_balance=2000,
                             address="Gold Street Quezon City",
                             email="johndoe@yahoo.com")

print("Account 2")
print(Account2.account_firstname)
print(Account2.account_lastname)
print(Account2.current_balance)
print(Account2.address)
print(Account2.email)

# Creating and Using an atm object
atm1 = atm.atm('123456',0)

atm1.deposit(Account1, 500)
atm1.check_current_balance(Account1)

atm1.deposit(Account2, 300)
atm1.check_current_balance(Account2)

print(atm1.serial_number)

"""