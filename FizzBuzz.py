for x in range(1,101):
    out = ""
    if x%3 == 0: out = out + "Fizz"
    if x%5 == 0: out = out + "Buzz"
    if out == "": out = x
    print(out)

    