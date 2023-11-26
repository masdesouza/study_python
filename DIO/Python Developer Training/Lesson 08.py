'''
Study about String Class in Python
String Class
     String is a sequence of characters
     String is immutable
     String is a sequence of Unicode characters
     String is a sequence of Unicode code points
     String is a sequence of Unicode code units    
     String is a sequence of bytes
     String is a sequence of 8-bit bytes
     String is a sequence of octets
     String is a sequence of 7-bit ASCII characters
     String is a sequence of 16-bit Unicode characters
     String is a sequence of 32-bit Unicode characters
     String is a sequence of 8-bit unsigned integers
'''

# String Class Methods

#Example

txt = "hello, and welcome to my world."

# upper() - Converts a string into upper case
txt = txt.upper() 
print(txt) # Output: HELLO, AND WELCOME TO MY WORLD.

# lower() - Converts a string into lower case
x = txt.lower()
print(x) # Output: hello, and welcome to my world.

#title() - Converts the first character of each word to upper case
x = txt.title()
print(x) # Output: Hello, And Welcome To My World.

# capitalize() - Converts the first character to upper case
x = txt.capitalize()
print(x) # Output: Hello, and welcome to my world.

# center() - Returns a centered string
x = txt.center(50,'#')
print(x) # Output: #########HELLO, AND WELCOME TO MY WORLD.##########

# join() - Joins the elements of an iterable to the end of the string
x = ".".join(txt)
print(x) # Output: H.E.L.L.O.,. .A.N.D. .W.E.L.C.O.M.E. .T.O. .M.Y. .W.O.R.L.D..

# casefold() - Converts string into lower case
x = txt.casefold()
print(x) # Output: hello, and welcome to my world.

# count() - Returns the number of times a specified value occurs in a string
x = txt.count("WELCOME")
print(x) # Output: 1

txt = "   Hello, welcome to my world.   "

# strip() - Returns a trimmed version of the string
x = txt.strip()
print(x) # Output: Hello, welcome to my world.

# lsstrip() - Returns a left trim version of the string
x = txt.lstrip()
print(x) # Output: Hello, welcome to my world.

# rstrip() - Returns a right trim version of the string
x = txt.rstrip()
print(x) # Output:    Hello, welcome to my world.

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
x = txt.swapcase()
print(x) # Output:    hELLO, WELCOME TO MY WORLD.

# replace() - Returns a string where a specified value is replaced with a specified value
x = txt.replace("H", "J")
print(x) # Output:    Jello, welcome to my world.

# split() - Splits the string at the specified separator, and returns a list
x = txt.split(",")
print(x) # Output: ['   Hello', ' welcome to my world.   ']

# splitlines() - Splits the string at line breaks and returns a list
x = txt.splitlines()
print(x) # Output: ['   Hello, welcome to my world.   ']

# partition() - Returns a tuple where the string is parted into three parts
x = txt.partition("welcome")
print(x) # Output: ('   Hello, ', 'welcome', ' to my world.   ')

# rpartition() - Returns a tuple where the string is parted into three parts
x = txt.rpartition("welcome")
print(x) # Output: ('   Hello, ', 'welcome', ' to my world.   ')

# rfind() - Searches the string for a specified value and returns the last position of where it was found
x = txt.rfind("welcome")
print(x) # Output: 10

# rindex() - Searches the string for a specified value and returns the last position of where it was found
x = txt.rindex("welcome")
print(x) # Output: 10

# rjust() - Returns a right justified version of the string
x = txt.rjust(50)
print(x) # Output:                Hello, welcome to my world.

'''
    Interpolation of Strings

'''

# Example
name = 'Marcos Aurélio'
age = 42
profession = 'Python Developer'
language = 'Python'
salary = 1000.00

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# Example

print('My name is %s, I am %d years old, I am a %s and I like %s' % (name, age, profession, language))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

# Example with %f
print('My name is %s, I am %d years old, I am a %s and I like %s and salary %f ' %(name, age, profession, language, salary))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python adn salary 1000.000000

# Example with %.2f
print('My name is %s, I am %d years old, I am a %s and I like %s and salary %.2f ' %(name, age, profession, language, salary))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python and salary 1000.00

# Example with %x
print('My name is %s, I am %x years old, I am a %s and I like %s and salary %.2f ' %(name, age, profession, language, salary))
# Output: My name is Marcos Aurélio, I am 2a years old, I am a Python Developer and I like Python and salary 1000.00

# Example with %X
print('My name is %s, I am %X years old, I am a %s and I like %s and salary %.2f ' %(name, age, profession, language, salary))
# Output: My name is Marcos Aurélio, I am 2A years old, I am a Python Developer and I like Python and salary 1000.00


# Using the format() and f-string method
# Example
print('My name is {}, I am {} years old, I am a {} and I like {}'.format(name, age, profession, language))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

# Example with index
print('My name is {0}, I am {1} years old, I am a {2} and I like {3}'.format(name, age, profession, language))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

# Example with variable names
print(f'My name is {name}, I am {age} years old, I am a {profession} and I like {language}'.format(name=name, age=age, profession=profession, language=language))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

# Example with variable names in f-string
print(f'My name is {name}, I am {age} years old, I am a {profession} and I like {language}')
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

# Example with dictionary
person = {'name': 'Marcos Aurélio', 'age': 42, 'profession': 'Python Developer', 'language': 'Python'}

# Example with dictionary in f-string
print(f"My name is {person['name']}, I am {person['age']} years old, I am a {person['profession']} and I like {person['language']}")
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

print(f"My name is {name}, I am {age} years old, I am a {profession} and I like {language}".format(**person))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

# Example with list
person_list = ['Marcos Aurélio', 42, 'Python Developer', 'Python']
print(f"My name is {person_list[0]}, I am {person_list[1]} years old, I am a {person_list[2]} and I like {person_list[3]}")
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python

print(f"My name is {name}, I am {age} years old, I am a {profession} and I like {language}".format(*person_list))
# Output: My name is Marcos Aurélio, I am 42 years old, I am a Python Developer and I like Python


'''
Study about String Slicing

'''

txt = "hello, and welcome to my world."

# Example
print(txt[1]) # Output: e
print(txt[2:5]) # Output: llo
print(txt[-5:-2]) # Output: orl
print(txt[0]) # Output: h
print(txt[:]) # Output: hello, and welcome to my world.
print(txt[::2]) # Output: hlo n olm o.
print(txt[::3]) # Output: hl deo   r.
print(txt[:4]) # Output: hell 
print(txt[4:]) # Output: o, and welcome to my world.



'''
Multiline Strings
    
    Using three single quotes 
    Using three double quotes

'''

# Example
name = 'Marcos Aurélio'
txt = f'''I am Python developer 
and might call me {name}.'''

print(txt)








