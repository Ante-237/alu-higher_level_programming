#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count < 0:
            print("{:d}".format(my_list[count]), end="")
            count += 1
    except:
        pass
    finally:
        print("\n{:d}".format(count))
