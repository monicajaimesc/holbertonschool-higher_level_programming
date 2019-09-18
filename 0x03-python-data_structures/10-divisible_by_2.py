#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    counter = 0
    copy_list = my_list[:]
    for i in copy_list:
        # multiples of 2
        if i % 2 is 0:
            copy_list[counter] = True
        else:
            copy_list[counter] = False
        counter = counter + 1
    return copy_list
