#!/usr/bin/python3
""" NO MODULE USED MODULE IN SQUARE FILE CLASS """


class Square:
    """
    SQUARE CLASS
    """
    def __init__(self, size=0):
        """
        Returns:
            just init values
        Args: 
            size (int): default to 0 sets side of square
        """
        self.size = size

    @size.setter
    def size(self, value):
        """
        setter method
        Args:
            value(int): size of the side of the square
        Raises:
            TypeError: if not int
            ValueError: if less than 0
        Returns:
            Setter no return
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def size(self):
        """
        GETTER METHOD
        Return:
            size of square
        """
        return self.__size

    def area(self):
        """
        SOME AREA METHOD

        Return:
            the calculated square area
        """
        return self.__size**2
