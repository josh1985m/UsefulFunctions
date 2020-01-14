firstList = [1, 2, 3, 4, 5]
secondList = ['A', 'B', 'C', 'D', 'E']
zippedList = list(zip(firstList, secondList))
#returns object: <zip object at 0x7f770afa8948> if not list, pairs in tuples#
print(zippedList)
for val in zippedList: #unpack tuples#
    print(val)
    for value in val: #unpack values#
        print(value)
for key, value in zippedList: #unpack values#
    print(key, value)