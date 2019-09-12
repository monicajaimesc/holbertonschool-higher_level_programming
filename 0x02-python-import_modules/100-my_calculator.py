#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, divi
    c = (len(sys.argv))
    if c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
a = int(sys.argv[1])
b = int(sys.argv[2])
