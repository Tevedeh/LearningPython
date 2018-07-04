def myFunc(*args):
    return sum(args)*.05

print(myFunc(3,2,4,3,12))

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f"My fruit of choice is {kwargs['fruit']}")
    else: 
        print('There is no fruit')

myfunc(fruit = 'apple')

def myfunc2(*args, **kwargs):
    print(f"I would like {args[0]} {kwargs['food']}")

myfunc2(10,20,30,food='orange')

def yoda(string):
    sp = string.split()
    sp.reverse()