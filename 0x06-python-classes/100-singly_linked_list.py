#!/usr/bin/python3
""" Defines a node of a singly-linked list """


class Node:
    """ Initializes the values to self

    Args:
        data: refers to the list's data
        next_node: next node of the linked list 
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves data of the linked list

        The setter method checks if the value passsed is of
        the right type otherwise it raises a TypeError
        """
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrieves next node of the linked list

        The setter method checks if the value passsed is a
        node otherwise it raises a TypeError
        """
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

""" Defines a singly-linked list """


class SinglyLinkedList:
    """ Initializes a singly linked list """
    def __init__(self):
        self.__head = None

    """ Prints the elements of a singly linked list

    Returns:
        The element of a string each on its own line
    """
    def __str__(self):
        val = self.__head

        data = ""
        while val is not None:
            data += str(val.data) + "\n"
            val = val.next_node
        return data[:-1]

    """ Sorts the elements of a list in ascending order

    Args:
        value: data of the linked list
    """
    def sorted_insert(self, value):
        first = Node(value)

        if self.__head is None:
            self.__head = first
            return

        if value < self.__head.data:
            first.next_node = self.__head
            self.__head = first
            return

        second = self.__head
        while second.next_node and second.next_node.data < value:
            second = second.next_node
        if second.next_node:
            first.next_node = second.next_node
        second.next_node = first
