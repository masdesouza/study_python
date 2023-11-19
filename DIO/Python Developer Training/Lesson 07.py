'''
Study about loops structures in Python
'''

#For loop
for i in range(0, 10):
    print(i)

#For loop with list
list = ['John', 'Paul', 'George', 'Ringo']
for name in list:
    print(name)

#For loop with string
for character in 'Python':
    print(character)

#For loop with tuple
tuple = ('John', 'Paul', 'George', 'Ringo')
for name in tuple:
    print(name)

#For loop with dictionary
# The dictionary is a key-value pair
# The key is unique
# The value can be repeated
# The key is immutable
# The value is mutable
#Example:
# The key is the name of the person and the value is the age

dict = {'John': 40, 'Paul': 39, 'George': 41, 'Ringo': 40}
for key in dict:
    print(key)
    print(dict[key])

#While loop
count = 0
while count < 5:
    print(count)
    count += 1

#While loop with break
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1

#While loop with continue
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

#While loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('End of loop')





