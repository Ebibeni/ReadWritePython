
listDict = {}
numbers = ['Fan', 'Fan', 3, 4, 6, 6, 7, 8, 9, 5, 'Mac', 6, 1, 8, 'Mac', 'Mac']



for i in numbers:
    if i not in listDict:
        listDict[i] = 0

    listDict[i] += 1

print(listDict)