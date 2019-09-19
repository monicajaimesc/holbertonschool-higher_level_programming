#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    sum = 0
    for digit in set(my_list):
        # suma first asignacion after
        sum += digit
    return sum

# set convert elementos iterables en
# elementos distintos


'''
temporal = set(my_list)
return sum(temporal)
'''

'''
sum = 0 for val in set(my_list):
sum += val
return sum
'''
