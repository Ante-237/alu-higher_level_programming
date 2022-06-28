#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    int_last_number = (-1 * number) % 10
    int_last_number *= -1
else:
    int_last_number = number % 10
if int_last_number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,int_last_number))
elif int_last_number == 0 :
    print("Last digit of {:d} is {:d} and is 0".format(number,int_last_number))
elif int_last_number < 6 and int_last_number != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number,int_last_number))
