#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv)
    if a == 1:
        print("{:d} arguments.".format(a - 1))
    elif a == 2:
        print("{:d} argument:".format(a - 1))
        print("{:d}: {:s}".format(a - 1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(a - 1))
        for i in range(a):
            if i == 0:
                continue
            print("{:d}: {:s}".format(i, sys.argv[i]))
