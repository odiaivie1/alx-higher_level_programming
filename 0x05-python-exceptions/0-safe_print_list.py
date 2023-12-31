#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
    my_list (list): The list all elements are printed from.
    x (int): The number of elements of my_list to print.

    Returns:
    The number of elements printed.
    """

    try:
        print("{}".format(my_list[i]), end="")
        total += 1
    except IndexError: break
    print("")
    return (total)
