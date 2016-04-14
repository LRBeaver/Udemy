__author__ = 'lyndsay.beaver'
#input from user

#name = input('What is your name?: ')
#print('Hello', name)

import statistics

exList = [5,3,2,5,1,5,6,2,3]

w = statistics.mean(exList)
print(w)

x = statistics.median(exList)
print(x)

y = statistics.mode(exList)
print(y)

z= statistics.stdev(exList)
print(z)

v = statistics.variance(exList)
print(v)