def binary_search(lst, target):
    middle = 0
    start = 0
    end = len(lst)
    steps = 0


    while(start <= end):
        print("Step", steps, ":", str(lst[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if target == lst[middle]:
            return middle
        if target < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 12

binary_search(my_list, target)


