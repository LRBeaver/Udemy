__author__ = 'lyndsay.beaver'
'''
originalList = [8, 7, 12, 4, 9, 6, 5]
bubbleList = []
listLength = len(originalList)
for i in range(listLength):
    if originalList[i+1] > listLength:
        print("We're done")
        break
    else:
        if originalList[i] < originalList[i+1]:
            bubbleList[i] = originalList[i]
    print(bubbleList)
'''
alist = [54,26,93,17,77,31,44,55,20]

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
bubbleSort(alist)
print(alist)




