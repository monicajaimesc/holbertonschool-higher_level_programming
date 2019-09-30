#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        # specting integer, sending string
        except ValueError:
            continue
        #  an operation is not soported
        except TypeError:
            continue

    print()
    return (counter)
