def square(num):
    return num**2

myNums = [1,2,3,4,5]

for item in map(square, myNums):
    print(item)

print(list(map(square,myNums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'Even'
    else:
        return mystring[0]

name = ['Andy', 'Sam', 'Sall']

print(list(map(splicer,name)))

def check_even(num):
    return num%2 ==0

mynums = [1,2,3,4,5,6]

print(list(filter(check_even, mynums)))

squarer = lambda num: num**2

print(squarer(3))

print(list(map(lambda num:num**2, mynums)))

print(list(map(lambda name:name[0], name)))