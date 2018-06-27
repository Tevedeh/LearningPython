x=0  
while x<5:
    print(x)
    x += 1
else:
    print("X is big")

x = [1,2,3]

for item in x:
    pass

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

x = 0

while x<5:
    if x==2:
        break
    print(x)
    x+=1