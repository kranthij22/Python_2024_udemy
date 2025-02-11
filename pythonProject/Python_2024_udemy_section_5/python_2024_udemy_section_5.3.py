# While Loops in Python.
# While loops will continue to execute a block of code "while" some condition remains True.
# Syntax of a while loop
# while some_boolean_condition:
#   do something.
# else:
#   do something different.

x = 0

while x < 5:
    x = x + 1
    print(x)
else:
    print("X is grater then 5")

# we can use Break, continue and pass statements in out loops to add additional functionality for various cases.
# Break: Breaks out of the current closest enclosing loop.
# Continue: Goes to top of the closest enclosing loop.
# Pass: Does nothing at all.

# ex of Pass


x = [1, 2, 3, 4, 5]
for k in x:
    # if we want to keep this blank and to avoid the error we can use PASS
    # if we dont use pass we will get error
    pass
print('End of the script')

# Ex for Continue

mystring = 'Kranthi'
for kk in mystring:
    if kk == 'i':
        continue
    print(kk)

# List Comprehensions in python

mylist = []

for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        mylist.append(x * y)
print(mylist)

# can be done using List Comprehension in python:

mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print(mylist)

# We can also use if else in ListComprehension:

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)
