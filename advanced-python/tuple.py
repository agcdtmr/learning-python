myTuple = ("Ben", 30, "Berlin")
print(myTuple)
print(type(myTuple))


myTuple1 = ("Ben")
print(type(myTuple1))

myTuple2 = ("Ben",)
print(type(myTuple2))

myTuple3 = tuple(["Ben", 30, "Berlin"])
print(type(myTuple3))
print(myTuple3)


item = myTuple[0]
print(item)


item1 = myTuple[-1]
print(item1)


for item3 in myTuple:
    print(item3)


if "Ben" in myTuple:
    print("yes")
else:
    print("no")

if "Tim" in myTuple:
    print("yes")
else:
    print("no")


my_tuple = ('a', 'p', 'p', 'l', 'e')
print(len(my_tuple))

print(my_tuple.count('a'))
print(my_tuple.count('p'))
print(my_tuple.count('l'))
print(my_tuple.count('o'))

print(my_tuple.index('p'))
print(my_tuple.index('a'))
print(my_tuple.index('l'))


my_list = list(my_tuple)
print(my_list)
print(type(my_list))


my_tuple2 = tuple(my_list)
print(my_tuple2)
print(type(my_tuple2))

# slicing

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
print(b)

b = a[:5]
print(b)

b = a[2:]
print(b)

b = a[::2]
print(b)

b = a[::-1]
print(b)


# unpack

myTuple4 = ("Ben", 30, "Berlin")

name, age, city = myTuple4
print(name)
print(age)
print(city)


my_tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

i1, *i2, i3 = my_tuple1
print(i1)
print(i3)
print(i2)


print(my_tuple.index('i'))

myTuple[0] = "Tim"


item2 = myTuple[3]
print(item2)
