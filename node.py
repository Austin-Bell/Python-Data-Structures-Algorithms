# Implementation of a Node class to work with other linear data structures

class Node:
    # link_node has a default value of None to show the end of nodelist
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
    # Method to get value in nodes
    def get_value(self):
        return self.value
    # Method to see the next linked node
    def get_link_node(self):
        return self.link_node
    # Changes default value of None and connects nodes together
    def set_next_node(self, next_node):
        self.link_node = next_node

