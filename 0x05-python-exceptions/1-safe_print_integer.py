#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print an integer with "{:d}".format().

    Args:
    Value (int): THe integer to be printed

    Returns:
    True if value has been correctly printed.
    (it means the value is an integer) Otherwise, returns False.
"""

try:
    print("{:d}".format(value))
    return (True)
except (TypeError, ValueError):
    return (False)
