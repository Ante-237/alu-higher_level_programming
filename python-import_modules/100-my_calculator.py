#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as extra
    import sys


argNum = len(sys.argv)# gets number of arguments
allA = sys.argv # stores arguments return by sys module
if argNum != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if allA[2] != "-" or allA[2] != "/" or allA[2] != "*" or allA[2] != "+":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    if allA[2] == "-":
        print("{:d} - {:d} = {:d}".format(int(allA[1]), int(allA[3]), extra.sub(int(allA[1]), int(allA[3]))))
    elif allA[2] == "*":
        print("{:d} * {:d} = {:d}".format(int(allA[1]), int(allA[3]), extra.mul(int(allA[1]), int(allA[3]))))
    elif allA[2] == "/":
        print("{:d} / {:d} = {:d}".format(int(allA[1]), int(allA[3]), extra.div(int(allA[1]), int(allA[3]))))
    elif allA[2] == "+":
        print("{:d} + {:d} = {:d}".format(int(allA[1]), int(allA[3]), extra.add(int(allA[1]), int(allA[3]))))
