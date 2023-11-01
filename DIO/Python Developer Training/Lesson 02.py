'''
Study about variables and constants in Python
Author: Marcos Souza
'''
#Variables

#Attributing values to variables using in one line
account, name, balance, limit = 0, "", 0.0, 0.0

#Attributing values to variables using in multiple lines (recommended). using input function.
account = input("Enter account number: ")
name = input("Enter the customer's name: ")
balance = float(input("Enter the account balance: "))
limit = float(input("Enter the account limit: "))

print("The account number is:", account)
print(f"The account number is: {account}")
print("The customer's name is:", name)
print(f"The customer's name is: {name}")
print("The account balance is:", balance)
print(f"The account balance is: {balance}")
print("The account limit is:", limit)
print(f"The account limit is: {limit}")


#Constants

#Defining constants
#The convention is to use all letters in uppercase
#The convention is to use _ to separate words

#Using in one line
PI = 3.1415
GRAVITY = 9.8
EULER = 2.7182
STATES = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Ceará"]
STATES_TUPLE = ("São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Ceará")
STATES_DICT = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Minas Gerais", "BA": "Bahia", "CE": "Ceará"}








