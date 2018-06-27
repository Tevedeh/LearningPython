myList = [1,2,3]

for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(3,10,2):
    print(num)

print(list(range(3,10,2)))

index = 0
word  = 'abcde'

for letter in 'abcde':
    print(f'At index {index} the letter is {letter}')
    index += 1

for letter in enumerate(word):
    print(letter)

myList1 = [1,2,3]
myList2 = ['a', 'b', 'c']

for item in zip(myList1, myList2):
    print(item)

print(list(zip(myList1, myList2)))

print('x' in [1,2,3])

myList = [10,20,30,40]

print(max(myList))
print(min(myList))

from random import shuffle

shuffle(myList)

print(myList)

from random import randint

print(randint(0,100))

inputt = input('Enter a number ')

print(inputt)