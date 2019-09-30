#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
    except IndexError:
        print()
        return (i)
# x can be bigger than the length of my_list
    return (i + 1)
