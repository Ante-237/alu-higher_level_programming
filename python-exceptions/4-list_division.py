#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    counter = 0
    result = 0
    while counter < list_length:
        try:
            result = 0
            result = my_list_1[counter]/my_list_2[counter]
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
