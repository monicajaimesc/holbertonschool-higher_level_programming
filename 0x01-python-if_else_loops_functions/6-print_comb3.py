#!/usr/bin/python3
for i in range(10):
    for j in range(10):
    # print numbers until 09
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
            break
    # print numbers after 09
        if j > i:
            print("{}{}, ".format(i, j), end="")
