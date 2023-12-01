dict1 = {"name": "Ben", "age": 41, "city": "New York"}
print(dict1)

dict2 = dict(name="Mary", age=28, city="Manila")
print(dict2)

value = dict1["name"]
print(value)

value = dict1["age"]
print(value)

dict1["email"] = "ben@email.com"
print(dict1)

dict_cpy2 = dict(dict1)
print(dict_cpy2)

dict1["email"] = "benten@email.com"
print(dict1)

dict_cpy = dict1
print(dict_cpy)

dict_cpy1 = dict1.copy()
print(dict_cpy1)

#### merge two dictionaries: update method

# original dict is overwritten and update a dict
dict1.update(dict2)
print(dict1)


dict3 = {3: 9, 6: 36, 9: 81}
print(dict3)

value = dict3[3]
print(value)

tuple1 = (8, 7)
dict3 = {tuple1: 15}
print(dict3)


## TypeError: unhashable type: 'list'
list1 = [8, 7]
dict3 = {list1: 15}
print(list1)


## error because zero is not on the list
value = dict3[0]


