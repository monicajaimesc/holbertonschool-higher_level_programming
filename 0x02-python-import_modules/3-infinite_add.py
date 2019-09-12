#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    argc = len(argv)
    if argv == 1:
        print(0)
    for i in range(1, argc):
        a += int(argv[i])  # save the result in itself
    print(a)
