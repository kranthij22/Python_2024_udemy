# Write a program to print integers from 1 to 100. but for Multiples of 3 print "Fizz" instead of number,
# and for multiples of 5 print "BUZZ". for number which are multiples of both 3 and 5 print "FizzBuzz".

# Code Using while loop.
num = 0
while num <= 100:
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
# Code using for loop.
num = 0
for n in range(0, 100):
    num = num + 1
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

