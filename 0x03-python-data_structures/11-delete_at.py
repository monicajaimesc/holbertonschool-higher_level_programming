#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    counter = 0
    for i in range(len(my_list)):
        if counter == idx:
            del my_list[counter]
        counter = counter + 1
    return my_list
