myfile = open("myfile.txt")
print(myfile.read())
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()


#Block that closes the file once you are out of the block.
with open("myfile.txt") as myNewFile:
    contents = myNewFile.readlines()

print(contents)

with open("myfile.txt", mode='a') as thefile:
    thefile.write("/nHello")

with open("newfile.txt", mode='w') as thefile:
    thefile.write("Hey")

with open("newfile.txt", mode='r') as thefile:
    print(thefile.read())
