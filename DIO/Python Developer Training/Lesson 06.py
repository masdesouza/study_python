'''
Study about conditional in Python
'''

#If statement - Conditional structure in Python
# If the condition is true, the block of code is executed
#Example:
balance = 2000
withdraw = float(input("Enter the amount to withdraw: "))

if balance >= withdraw:
    balance -= withdraw
    print("Withdrawal successfully completed!") 

if balance < withdraw:
    print("Insufficient funds!")


#If-else statement - Conditional structure in Python
# If the condition is true, the first block of code is executed, otherwise the second block is executed
# The else statement is optional
# The else statement is always associated with the last if statement
# The else statement is always executed if the condition of the last if statement is false
# The else statement is always executed only once
# The else statement is always executed only if the condition of the last if statement is false
#Example:

balance = 2000
withdraw = float(input("Enter the amount to withdraw: "))
if balance >= withdraw:
    balance -= withdraw
    print("Withdrawal successfully completed!")
else:
    print("Insufficient funds!")


#If-elif-else statement - Conditional structure in Python
# If the condition is true, the first block of code is executed, otherwise the second block is executed
# The else statement is optional
#Example:
import sys

balance = 0
option = int(input("Enter the option:[1] Deposit [2] Withdraw [3] Balance: "))

#Deposit
if option == 1:
    deposit = float(input("Enter the amount to deposit: "))
    balance += deposit
    print("Deposit successfully completed!")
#Withdraw
elif option == 2:
    withdraw = float(input("Enter the amount to withdraw: "))
    if balance >= withdraw:
        balance -= withdraw
        print("Withdrawal successfully completed!")
    elif balance < withdraw:
        print("Insufficient funds!")
#Balance
elif option == 3:
    print("Your balance is: ", balance)
else:
    sys.exit("Invalid option!")    

       
#Nested if statement - Conditional structure in Python
# If the condition is true, the first block of code is executed, otherwise the second block is executed
# The else statement is optional
#Example:
import sys
balance = 0

type_account = int(input("Enter the type account:[1] Normal [2] Academic : "))

if type_account == 1:

    option = int(input("Enter the option:[1] Deposit [2] Withdraw [3] Balance: "))
    #Deposit
    if option == 1:
        deposit = float(input("Enter the amount to deposit: "))
        balance += deposit
        print("Deposit successfully completed!")
    #Withdraw
    elif option == 2:
        withdraw = float(input("Enter the amount to withdraw: "))
        if balance >= withdraw:
            balance -= withdraw
            print("Withdrawal successfully completed!")
        elif balance < withdraw:
            print("Insufficient funds!")
    #Balance
    elif option == 3:
        print("Your balance is: ", balance)
    else:
        sys.exit("Invalid option!")  

elif type_account == 2:
    
    option = int(input("Enter the option:[1] Deposit [2] Withdraw [3] Balance: "))

    #Deposit
    if option == 1:
        deposit = float(input("Enter the amount to deposit: "))
        balance += deposit
        print("Deposit successfully completed!")
    #Withdraw
    elif option == 2:
        withdraw = float(input("Enter the amount to withdraw: "))
        if balance >= withdraw:
            balance -= withdraw
            print("Withdrawal successfully completed!")
        elif balance < withdraw:
            print("Insufficient funds!")
    #Balance
    elif option == 3:
        print("Your balance is: ", balance)
    else:
        sys.exit("Invalid option!") 

else:
    sys.exit("Invalid option!")


#If ternary statement - Conditional structure in Python
#Allow to write a conditional structure in a single line
#It is not recommended to use it when the conditional structure is too complex
#Example:

balance = 2000
status = "positive" if balance > 0 else "negative"
print(f"balance is {status}")