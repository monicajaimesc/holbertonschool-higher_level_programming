#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list[:]
    for digit in range(len(copy_list)):
        if copy_list[digit] == search:
            copy_list[digit] == replace

    return copy_list
# copy_list = list(map(lambda digit:
# replace if digit == search else digit, my_list))
# return copy_list
