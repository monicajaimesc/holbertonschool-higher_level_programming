#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 1
            # append0 cause division is not posible
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            result = 1
            new_list.append(0)
            print("division by 0")
        except IndexError:
            result = 1
            new_list.append(0)
            print("out of range")
        finally:
            if result == 0:
                new_list.append(my_list_1[i] / my_list_2[i])
    return new_list
