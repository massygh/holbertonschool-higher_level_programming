#!/usr/bin/python3
"""
Module defines a Square class with attributes and methods to manipulate
square properties.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The size of a side of the square.
        __position (tuple of int): The x, y position of the square when
        printed.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new
        Square.
        area(self): Calculates the area of the square.
        size(self): Gets the current square size.
        size(self, value): Sets the size of the square.
        my_print(self): Prints the square with the character '#'.
        position(self): Gets the current position.
        position(self, value): Sets the position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's side.
            Defaults to 0.
            position (tuple of int, optional): The x, y coordinates where
            the square will be printed. Defaults to (0, 0).

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) for n in value) or \
           any(n < 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            print("\n".join(" " * self.position[0] + "#" * self.__size for _ in range(self.__size)))
