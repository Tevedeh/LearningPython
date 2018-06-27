def name(name):
    print(name)

name("Tristan")

def add(one, two):
    '''
    DOCSTRING: Add two numbers
    INPUT: Two numbers
    OUTPUT: Sum
    '''
    return one+two

print(add(3, 4))
help(add)

def defaultName(name='NAME'):
    print(f"Hello {name}")
    return (f"Hello {name} (returned)")

defaultName()
defaultName("Tristan")
print(defaultName("Tristan"))

#Find out if 'dog' is in a string

def isDog(string):
    return 'dog' in string.lower()

print(isDog("Hello"))

print(isDog("Hello Dog"))

def pigLatin(word):
    if word[0] in 'aeiou': return (word+'ay').capitalize()
    else: return (word[1:] + word[0] + 'ay').capitalize()

print(pigLatin("Hello"))
print(pigLatin("Tristan"))