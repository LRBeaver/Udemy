__author__ = 'lyndsay.beaver'
'''
gender = input('What is your gender?\n')
#print(type(gender))
if gender == 'm' or 'M' or 'f' or 'F':
    print(gender)
else:
    print("please enter M, m, F, or f")
'''
print('Hello there')

name=input('what\'s your name?\n')

gender=input('please enter your gender (m/M or f/F)\n')

while gender not in ['m','M','f','F']:

    gender = input('please re-enter your gender (m/M or f/F)\n')

if gender in ['m', 'M']:

    print('{}, you\'re a man!'.format(name))

else:

    print('{}, you\'re a woman!'.format(name))
