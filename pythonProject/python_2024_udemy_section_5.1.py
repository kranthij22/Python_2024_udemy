# IF, ELIF, ELSE STATEMENTS:
# CONTROL FLOW
# to control the flow of logic we use some keywords:
    # if
    # elif
    # else
# control flow syntax makes use of colons and indentation(whitespace)
# The indentation system is crucial to python and is what sets it apart from other programming languages.
# syntax of an statements

    # if some_condition:
        # execute some code
    # elif some_other_condition:
        # do something different
    # else:
        # do something else

if True:
    print('Its TRUE!!')

if 5 == 5:
    print('Its True!!')

hungry = True
if hungry:
    print('Feed me!!')

hungry = False
if hungry:
    print('Feed me!!')

hungry = False
if hungry:
    print('Feed me!!')
else:
    print('I am not hungry')

hungry = True
if hungry:
    print('Feed me!!')
else:
    print('I am not hungry')

loc = 'Bank'
if loc == 'auto shop':
    print('Cars are cool!!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!!')
else:
    print('I dont know much')

loc = 'auto shop'
if loc == 'auto shop':
    print('Cars are cool!!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!!')
else:
    print('I dont know much')

loc = 'Store'
if loc == 'auto shop':
    print('Cars are cool!!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!!')
else:
    print('I dont know much')

loc = 'Game'
if loc == 'auto shop':
    print('Cars are cool!!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!!')
else:
    print('I dont know much')

