list_1 = [1, 2, 3, 3, 4, 5, 6, 4, 7, 8]
new_list = []
for num in list_1:
    if num not in new_list:
        new_list.append(num)
print(new_list)

list = list(set(list_1))
print(list)
