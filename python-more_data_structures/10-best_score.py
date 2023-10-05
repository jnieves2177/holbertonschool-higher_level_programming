#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = None
    max_key = None

    for key, value in a_dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key

    return max_key
