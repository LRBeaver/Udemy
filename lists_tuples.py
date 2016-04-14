__author__ = 'lyndsay.beaver'

def example():
    return 15, 19

a,b = example()

print('a is:', a)
print('b is:', b)

x = [3,5,6,1,2,8,2]

print(x)

print(x[2])
x.append(12)

x.insert(5,7)
print(x)

print(x.index(12))

print(x.count(3))

x.sort()
print(x)
