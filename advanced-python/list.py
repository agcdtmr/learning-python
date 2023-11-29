myList = ["banana", "cherry", "apple"]
print(myList)

myList2 = list()
print(myList2)


myList3 = [5, True, "apple"]
print(myList3)


item = myList[0]
print(item)

for item in myList:
    print(item)


if "banana" in myList:
    print("yes")
else:
    print("no")


if "pineapple" in myList:
    print("yes")
else:
    print("no")

print(len(myList))


myList.append("lemon")
print(myList)

myList.insert(1, "blueberry")
print(myList)

popItem = myList.pop()
print(popItem)
print(myList)

removeItem = myList.remove("cherry")
print(removeItem)

clearItem = myList.clear()
print(clearItem)

reverseItem = myList3.reverse()
print(reverseItem)


myList4 = [2, 400, 60, 2304, 9]
# sortItem = myList4.sort()
# print(sortItem)
new_list = sorted(myList4)
print(myList4)
print(new_list)


myList5 = [0] * 5
print(myList5)

myList6 = [1, 2, 3, 4, 5]
new_list1 = myList5 + myList6
print(new_list1)


new_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = new_list2[1:5]
print(a)


a = new_list2[1]
print(a)

a = new_list2[::2]
print(a)

a = new_list2[::-1]
print(a)

list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy2 = list_org.copy()
list_cpy.append("lemon")
list_cpy3 = list(list_org)
list_cpy4 = list_org[:]

print(list_cpy)
print(list_org)
print(list_cpy2)
print(list_cpy3)
print(list_cpy4)


item2 = myList[3]
print(item2)

removeItem = myList.remove("cherry2")
print(removeItem)


