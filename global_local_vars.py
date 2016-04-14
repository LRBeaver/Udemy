__author__ = 'lyndsay.beaver'

x=6

def example():
    z=5
    print('example z',z)

def example2():
    z=7
    print('example2 z', z)
    y= x +1
    print('example2 y',y)


def example3():
    global x
    x += 1
    print('example3 x', x)

example()
example2()
example3()
