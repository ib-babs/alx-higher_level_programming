#!/usr/bin/python3
class Node:
    """This class 'Node' is a class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes class Node with two optional parameters: 'data set to 0' And 'next_node' to None"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """"The getter method 'data' gets  instance '__position'"""
        return self.__data

    @data.setter
    def data(self, value):
        """"The setter method 'value' sets the private instance '__position'"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"The getter method 'data' gets the private instance '__position'"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """"The setter method 'value' sets the private instance '__position'"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The class 'SinglyLinkedList' defines a singly linked list class"""

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        linked_list_str = ""
        current = self.head
        while current:
            linked_list_str += str(current.data) + "\n"
            current = current.next_node
        return linked_list_str
