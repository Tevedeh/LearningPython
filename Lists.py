myList = [1,2,3]

myMixed = [1, 200.3]

print(len(myList))
print(len(myMixed))
print(myList[0])

newList = myList + myMixed
print(newList)

newList[0] = "HELLO"
print(newList)

newList.append("GOODBYE")
print(newList)

pop = newList.pop()
print(newList)
print(pop)

sortThis = [3, 6, 2, 1]
print(sortThis)
sortThis.sort()
print(sortThis)

sortThis.reverse()
print(sortThis)