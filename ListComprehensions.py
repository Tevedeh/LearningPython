mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

mystring2 = 'hello'

mylist2 = [letter for letter in mystring2]

print(mylist2)

mylist2 = [num**2 for num in range(0,11)]

print(mylist2)

mylist = [x for x in range(0,11) if x%2 == 0]

print(mylist)

celcius = [0,10,20,35.4]

farenheight = [((9/5)*x + 32) for x in celcius]

print(farenheight)

results = [x if x%2 == 0 else 'ODD' for x in range(0,11)]

print(results)

mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

print(mylist)

mylist = [x*y for x in [2,4,6] for y in [100,200,300]]

print(mylist)