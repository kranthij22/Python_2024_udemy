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
           'key4': {'car1': 'Honda', 'car2': 'Mahindra', 'car3': 'Kia', 'car4': 'Buggati', 'car5': ['Honda', 'Ducati', 'Ktm', 'RE']},
           'key5': "Stringsssssssss"}
print(my_dict)
print(my_dict['key1'])
print(my_dict['key2'][1])
print(my_dict['key3'][4])
print(my_dict['key4']['car2'])
print(my_dict['key4']['car5'][1])
print(my_dict['key5'])
