#!/usr/bin/python3
"""
NO MODULE USED YET
"""


class Node:
    """NODE CLASS START """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ SINGLE LINKED LIST CLASS """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            new_node = Node(value)
            temporal = self.__head
            while temporal is not None:
                if temp.__next_node is None:
                    temporal.__next_node = new_node
                    new_node.__next_node = None
                if new_node.__data < temporal.__next_node.__data:
                    new_node.__next_node = temporal.__next_node
                    temporal.__next_node = new_node
                temporal = temporal.__next_node

    def __str__(self):
        output = ""
        temporal = self.__head
        while temporal is not None:
            output += str(self.__data)
            output += '\n'
            temporal = temporal.__next_node
        return output
