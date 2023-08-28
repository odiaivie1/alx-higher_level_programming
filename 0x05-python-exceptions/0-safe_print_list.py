#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
"""Print x elements of a list.

Args:
    my_list (list): The list all elements are printed from.
    x (int): The number of elements of my_list to print.

    Returns:
    The number of elements printed.
"""

lts = 0
for i in range(x):
    try:
        print("{}".format(my_list[i]), end="")
        ltx += 1
    except indexError:
        break
    print("")
    return (lts)
