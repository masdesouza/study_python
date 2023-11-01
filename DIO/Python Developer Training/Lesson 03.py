'''
Stydying about type conversion in Python
'''

# Type conversion is the process of converting one data type to another data type.
# Implicit Type Conversion
# Explicit Type Conversion

# Implicit Type Conversion
# In Implicit type conversion, Python automatically converts one data type to another data type.
# This process doesn't need any user involvement.
# For example, if we assign an integer value to a variable, the compiler will automatically change the type to integer.
# This type conversion process is also called Coercion.
# Let's see an example where Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.

# Conversion of int to float
price = 100
price_float = float(price)
print(price_float)

print(price / 10)
print(price // 10)
# Conversion of float to int
price = 100.5
price_int = int(price)
print(price_int)


# Numeric to string conversion
# We can convert one type of numeric data into a string using the str() function.
# This function takes the object as a parameter and returns the string in the format that can be easily understood by the user.
# For example, if we pass an integer value to the str() function, it will return the string version of that integer.
# Similarly, if we pass a float value to the str() function, it will return the string version of that float value.
# Let's see an example.
price = 100.50
print(str(price))
print(type(str(price)))


# String to numeric conversion
# We can convert a string to numeric data using the int() and float() functions.
# The int() function takes a string as a parameter and returns an integer object.
# Similarly, the float() function takes a string as a parameter and returns a float object.
# Let's see an example.
price = "100.50"
height = "55"
print(int(height))
print(int(float(price)))