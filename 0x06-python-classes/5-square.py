#!/usr/bin/python3

class Square:


    def __init__(self, size=0):
    """Initialize a new square.
    Args:
    size (int): The size of the new square.
    """

    self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise <typeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

        def area(self):
            return (self.__size * self.__size)

        def my_print(self):
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
                if self.__size == 0:
                    print("")
