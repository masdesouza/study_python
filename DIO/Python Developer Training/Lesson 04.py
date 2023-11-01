'''
Studying the use of functions in Python
'''

#Reading values from input function built-in
name = input('What is your name? ')
age = input('How old are you? ')
weight = input('How much do you weigh? ')

#Printing the values read, using the print function built-in
print(name, age, weight)
#Use option sep to separate the values with a character
print(name, age, weight, sep=';')
#Use option end to end the print with a character
print(name, age, weight, sep=';', end='.')
#Use option end to end the print with a character
print(name, age, weight, sep=';', end='.\n')
#Use option file to print to a file
print(name, age, weight, sep=';', end='.\n', file=open('print.txt', 'w'))




