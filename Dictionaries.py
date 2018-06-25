myDictionary = {"key1":"value1", "key2":"value2"}
print(myDictionary["key1"])

prices = {"Apples": 3, "Bannanas": 4}
print(prices["Apples"])
print(prices.keys())
print(prices.values())
print(prices.items())

#You can also stack dictionaries

diction = {"key1": {"key1": 1, "key2": 2}}
print(diction["key1"]["key2"])