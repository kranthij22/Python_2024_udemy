# Write a program to find the simple interest

p = int(input('Enter the Principal amount:'))
r = float(input('Enter the rate of interest:'))
t = float(input('Enter the no of years:'))

simple_interest = (p * r * t) / 100
print(simple_interest)

# Write a program to find the factorial of a number . Example: factorial of 6 is 6*5*4*3*2*1 which is 720.

n = int(input('Enter the number:'))
f = 1
i = 1
while i <= n:
    f = f * i
    i = i + 1
print('value of f:', f)

# Write a program to iterate over each character in a string and print it. For example: string = hello , output = h,e,l,l,o


my_string = 'Hello'
for kk in my_string:
    print(kk)

