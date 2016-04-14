__author__ = 'lyndsay.beaver'

readMe = open('exampleWrite.txt', 'r').read()
print(readMe)

splitMe = readMe.split('\n')

print(splitMe)
print(splitMe[2])


readMe2 = open('exampleWrite.txt', 'r').readlines()
print(readMe2)