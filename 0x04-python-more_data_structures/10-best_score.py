#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # values are integers
        values = sorted(a_dictionary.values())
        result = values[-1]
        for best_key in a_dictionary:
            if result == a_dictionary[best_key]:
                return best_key


'''
other form:
if max(a_dictionary, key=a_dictionary.get) is 0:
        return None
    return max(a_dictionary, key=a_dictionary.get)
'''
