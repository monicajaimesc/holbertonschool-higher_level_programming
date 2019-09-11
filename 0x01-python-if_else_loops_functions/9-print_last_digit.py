#!/usr/bin/python3
def print_last_digit(letter):
    print("{:d}".format((abs(letter) % 10)), end="")
    return (abs(letter) % 10)
