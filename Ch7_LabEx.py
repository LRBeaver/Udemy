__author__ = 'lyndsay.beaver'
entry = '82914656273523:a4edFea2786DGex'

splitting = entry.split(':')
print(splitting)
id = splitting[0]
key = splitting[1]


if len(id) < 14:
    print('Error. Too few characters')
else:
    for i in range(len(id)):
        if id[i] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            print('ID may only contain numbers')

    print('All is good')



