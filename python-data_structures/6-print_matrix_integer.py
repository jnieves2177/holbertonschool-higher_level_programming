#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    max_width = max(len(str(element)) for row in matrix for element in row)

    for row in matrix:
        for element in row:
            print("{:>{width}}".format(element, width=max_width), end=" ")
        print()
