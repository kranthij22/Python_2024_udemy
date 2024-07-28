# Write a program to find the simple interest

p = 1000
r = 5
t = 3

simple_interest = p * (5 / 100) * 3
print(simple_interest)

# Write a program to find the factorial of a number . Example: factorial of 6 is 6*5*4*3*2*1 which is 720.

n = 6
f = 1
i = 1
while i <= n:
    f = f * i
    i = i+1
    print('value of f:', f)
    print('value of i:', i)
# Write a program to iterate over each character in a string and print it. For example: string = hello , output = h,e,l,l,o


my_string = 'Hello'
for kk in my_string:
    print(kk)

print(f'output =', my_string[0:])
print(f'output = ', my_string[0], my_string[1], my_string[2], my_string[3], my_string[4])




