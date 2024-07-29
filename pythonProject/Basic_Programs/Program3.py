# program to convert the weight from Kg's to pounds and pounds to Kg's.

Weight = float(input('Enter your weight: '))
Unit = str(input('(K)g or (L)bs: ').upper())

if Unit == 'K':
    pound = Weight * 2.20462
    print('Your weight in pounds is: ', pound)
elif Unit == 'L':
    Kg = (Weight / 2.20462)
    print('Your weight in Kgs is: ', Kg)



