__author__ = 'lyndsay.beaver'

try:
    print('Running the try...')
    import marsh
    print('5' + 5)

except TypeError as t:
    print('Type Error')

except NameError as n:
    print('Name Error')

except Exception as e:
    print('General Error')

