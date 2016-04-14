__author__ = 'lyndsay.beaver'
appendMe = 'Some additional example text'

saveFile = open('exampleWrite.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()
