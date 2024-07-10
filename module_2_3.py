my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

length_of_the_list = len(my_list)
a = 0

while a < length_of_the_list:
    if my_list[a] >= 0:
        if my_list[a] != 0:
            print(my_list[a])
        a += 1
    else:
        break
