#!/usr/bin/python3
def number_keys(a_dictionary):
    return len(a_dictionary.keys())
    '''
    Unlike sequences, which are indexed by a range of numbers,
    dictionaries are indexed by keys,
    which can be any immutable type;
    strings and numbers can always be keys.
    Tuples can be used as keys if they contain only strings,
    numbers, or tuples;
    if typle is mutable cant use key
    '''
