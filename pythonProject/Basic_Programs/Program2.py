# Use range() to print all the even number from 0 to 10.

for i in range(0, 11):
    if i % 2 == 0:
        print(i)

# Use List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

result = [x for x in range(0, 51) if x % 3 == 0]
print(result)


# Use for, .split(), and if to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in the sentence'
for x in st.split():
    if x[0] == 's':
        print(x)

# GO through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
    if len(x) % 2 == 0:
        print(x + ' :Even!!')
    else:
        print(x)

# Use List Comprehension to create a list of the letters of every word in the string below:

st = 'create a list of the first letters of every word in the string'
new_st = [x[0] for x in st.split()]
print(new_st)