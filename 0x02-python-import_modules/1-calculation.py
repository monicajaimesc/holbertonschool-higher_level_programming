#!/usr/bin/python3
if __name__ == "__main__":
	from calculator_1 import add, sub, mul, div
	a = 10
	b = 5
	c = add(a, b)
	print("{0} + {1} = {2}".format(a, b, c))
	c = sub(a, b)
	print("{0} - {1} = {2}".format(a, b, c))
	c = mul(a, b)
	print("{0} * {1} = {2}".format(a, b, c))
	c = div(a, b)
	print("{0} / {1} = {2}".format(a, b, c))
