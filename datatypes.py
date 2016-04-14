__author__ = 'lyndsay.beaver'
x = 42

a = '''
A
multi
line
string
'''
print(a)

b = '''This \
is
a
multi
line
string
'''
print(b)

print("This are %s items" % x)

print("There are {} item".format(x))

#tuple  - uses parens  ()
y = (1,2,3,4,5)
print(type(y),y)
print('')

#list - uses brackets []
z = [1,2,3,4,5]
print(type(z),z)
z.append(6)
print(type(z),z)
print('')

#dictionary  - uses braces {}
j = {'one': 1, 'two':2}
print(type(j),j)
print('')