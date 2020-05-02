# You can either import the node class or write it in this file for the purpose of this example I will write it in linked_list.py

class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next_node(self):
		return self.next_node

	def set_next_node(self, next_node):
		self.next_node = next_node

	
# Start of linked list
class LinkedList:
	def __init__(self, value=None):
		self.head_node = Node(value)

	# Method to find the head node in linked list
	def get_head_node(self):
		return self.head_node

	# Insert new node at the start of a linked list
	def insert_beginning(self,new_value):
		new_node = Node(new_value)
		new_node.set_next_node(self.head_node)
		self.head_node = new_node

	# Method to iterate through linked list
	def stringify_list(self):
		string_list = ""
		current_node = self.get_head_node()
		while current_node:
			if current_node.get_value() != None:
				string_list += str(current_node.get_value()) + "\n"
			current_node = current_node.get_next_node()
		return string_list

    # Method to remove Node by checking its value
	def remove_node(self, value_to_remove):
	    current_node = self.get_head_node()
	    if current_node.get_value() == value_to_remove:
	        self.head_node = current_node.get_next_node()
	    else:
	        while current_node:
		        next_node = current_node.get_next_node()
		        if next_node.get_value() == value_to_remove:
		            current_node.set_next_node(next_node.get_next_node())
		            current_node = None
		        else:
		            current_node = next_node

