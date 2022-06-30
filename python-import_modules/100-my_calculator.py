#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as extra
    import sys


argNum = len(sys.argv)  # gets number of arguments
allA = sys.argv  # stores arguments return by sys module
a = int(allA[1])
b = int(allA[3])
s = allA[2]
if argNum != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    if s == "-":
        print("{:d} - {:d} = {:d}".format(a, b, extra.sub(a, b)))
    elif s == "*":
        print("{:d} * {:d} = {:d}".format(a, b, extra.mul(a, b)))
    elif s == "/":
        print("{:d} / {:d} = {:d}".format(a, b, extra.div(a, b)))
    elif s == "+":
        print("{:d} + {:d} = {:d}".format(a, b, extra.add(a, b)))
    else:
        print("Unkown operator, Available operators: +, -, * and /")
        exit(1)
