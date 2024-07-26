# Numbers

a = 10
b = 2
print("The value of a is:", a)
print("The value of b is:", b)
print("The Sum of a and b is:", (a + b))
print("The diff of a and b is:", (a - b))
print("The product of a and b is:", (a * b))
print("a divided by b is:", (a / b))
print("The Reminder of a divided by b is:", (a % b))
print("The square of a is: ", (a ** 2))

# String indexing and slicing:

b = "Kranthi"

print("print the 0th index", b[0])
print("print the 2nd index", b[1])
print("print the 2nd index", b[2])
print("print the 2nd index", b[3])
print("print the 2nd index", b[4])
print("print the 2nd index", b[5])

print("Hello Python")
print(len(b))
print(len("Hello World"))

c = "Kranthi Kumar"

print(c[6:])
print(c[:7])
print(c[3:11])
print(c[::])
print(c[::2])

print('Kranthi Kumar is working'[0:8])
d = 'Geeta'
e = 's' + d[1:5]
print(e)
print(10 * c)
print(c.upper())
print(c.lower())
print(c.split('k'))

# Lists in Python.
# Lists are in square brackets[].
# They can have different objects.
# Lists sort objects in an ordered sequence.

my_list = [1, 2, 3, 4]
print(len(my_list))
my_list[0] = 100
print(my_list)
my_list.append(5)
print(my_list)
my_list.pop()
print(my_list)
new_list = [45, 98, 100, 2, 54, 89]
print(new_list)
new_list.sort()
print(new_list)
print(type(my_list))

# Dictionaries in Python.
# They are Unordered mappings for sorting objects.
# They use a key-value pairing instead.
# Dictionaries use curly brackets{}.
# {'key1':'value1', 'key2':'value2'}

cars = {'car1': 'Honda', 'car2': 'Mahindra', 'car3': 'Kia', 'car4': 'Buggati', 'car5': 'Ford'}
print(cars)
print(cars['car4'])
cars['car6'] = 'Toyota'
print(cars)

my_dict = {'key1': 'cars', 'key2': ['Honda', 'Bugatti', 'Ford', 'Kia'], 'key3': [1, 2, 3, 4, 5],
           'key4': {'car1': 'Honda', 'car2': 'Mahindra', 'car3': 'Kia', 'car4': 'Buggati',
                    'car5': ['Honda', 'Ducati', 'Ktm', 'RE']},
           'key5': "Stringsssssssss"}
print(my_dict)
print(my_dict['key1'])
print(my_dict['key2'][1])
print(my_dict['key3'][4])
print(my_dict['key4']['car2'])
print(my_dict['key4']['car5'][1])
print(my_dict['key5'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(type(my_dict))

# Tuples in Python.

# Tuples are in () brackets.
# Tuples are similar to Lists but tuples are immutability.
# Immutability means they can not be changed, once the element is inside a tuple it can not be reassigned.

t = (10, 20, 30, 40)
t1 = (0, 'Kranthi', 'Kranthi', 'Kranthi', 'Kranthi', 50, 100)
print(t1)
print(t1[6])
print(t1.count('Kranthi'))

# Sets in Python

# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same object.


my_set = set()
print(my_set)
my_set = (1, 3, 4)
print(my_set)

my_set = (1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 'Kranthi')
print(my_set)
print(set(my_set))

# Booleans in Python

# These are Operators that allow to convey True or False Statements.
# Very important for control flow and logics.

print(1 == 1)
print(10 < 5)

# How to perform simple i/o with basic .txt files.

my_file = open('test.txt')

print(my_file.read())

my_file = open("/repo/eakrkmu/test.txt")
print(my_file.read())

with open('test.txt') as my_new_file:
    my_new_file = my_new_file.read()
    print(my_new_file)

# different modes
# mode='r' is read only
# mode='w' is write only (will overwrite files or create new file)
# mode='a' is append only (will add on to files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading( will overwrite existing files or creates a new file)

# mode='r' is read only
with open('test.txt', mode='r') as my_new_file:
    print(my_new_file.read())

# mode='a' is append only (will add on to files)
with open('test.txt', mode='a') as my_new_file:
    my_new_file.write('\n TESTING EDITING TO THE FILE KRANTHIIIII')
    with open('test.txt', mode='r') as my_new_file:
        print(my_new_file.read())

with open('text2.txt', mode='a') as my_new_file_1:
    my_new_file_1.write('I CREATED THIS FILE!!!!!!!!!!')
    with open('text2.txt', mode='r') as my_new_file_1:
        print(my_new_file_1.read())

# Chaining Comparison Operators.

# AND
# OR
# NOT

print(1 < 2)
print(3 == 3)
print(5 > 10)
print('Bye' == 'Bye')
print('Hello' != 2)

# AND keyword
# (Both the conditions should be true)
print(1 < 2 and 2 > 3)

# OR keyword
# (Only one condition should be true)
print(1 < 2 or 2 > 3)

# NOT keyword
# (To change the output of the result)

print(2 == 2)
print(not 2 == 2)

