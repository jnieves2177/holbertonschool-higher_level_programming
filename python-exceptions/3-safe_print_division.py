#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division_result = a / b
    except(TypeError, ZeroDivisionError):
        division_result = None
    finally:
        print("Inside result: {}".format(division_result))
    return division_result
