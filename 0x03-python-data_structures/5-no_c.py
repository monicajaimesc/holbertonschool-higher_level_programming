#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i is "c" or i is "C":
            continue
        new_string = new_string + i
    return new_string
