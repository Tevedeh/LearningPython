myIt = [1,2,3,]

for num in myIt:
    if num % 2 == 0:
        print(f"Num is {num} (even)")
    else:
        print(f"Num is {num} (odd)")

listSum = 0

for num in myIt:
    listSum += num

print(listSum)

myStr = 'Hello'

for letter in myStr:
    print(letter)

myList = [(1,2), (3,4), (5,6), (3,4)]
print(len(myList))

for a,b in myList:
    print(a)
    print(b)

d = {'k1': 1, 'k2':2, 'k3':3}

for key,value in d.items():
    print(f"({key}, {value})")