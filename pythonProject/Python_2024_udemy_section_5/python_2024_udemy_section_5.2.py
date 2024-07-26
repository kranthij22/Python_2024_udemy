# FOR LOOPS.

# Many objects in python are "iterable".
# Meaning we can iterate over every element in the object.
# Such as every element in a list or every character in a string.
# We can use for loops to execute a block of code for every iteration.

# Syntax of a for Loop.
# my_iterable = [1,2,3]
# for item_name in my_iterable:
#   print(item_name)

my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for kk in mylist:
    print(kk)

for kk in mylist:
    if kk % 2 == 0:
        print("Even Numbers:", kk)
    else:
        print("Odd Numbers:", kk)

list_sum = 0
for kk in mylist:
    list_sum = list_sum + kk
print(list_sum)

# for loop in Strings:
mynewlist = 'Hello World'
for kk in mynewlist:
    print(kk)

# for loop in tuple:
tup = (1, 2, 3, 4, 5)
for _ in tup:
    print(_)

tuplist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for _ in tuplist:
    print(_)

# for loop in tuple unpacking:
tuplist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (a, b) in tuplist:
    print(a)
    print(b)

newtuplist = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in newtuplist:
    print(b)
    print(a)
    print(c)

# for loop in Dict:

my_dict = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 5}
for pp in my_dict:
    print(pp)

my_dict = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 5}
for pp in my_dict.items():
    print(pp)

my_dict = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 5}
for key, value in my_dict.items():
    print(value)