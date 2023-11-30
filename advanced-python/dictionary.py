mydict = {"name": "Ben", "age": 41, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=28, city="Manila")
print(mydict2)

value = mydict["name"]
print(value)

value = mydict["age"]
print(value)

mydict["email"] = "ben@email.com"
print(mydict)

mydict["email"] = "benten@email.com"
print(mydict)


del mydict["name"]
print(mydict)


value = mydict["lastname"]
print(value)