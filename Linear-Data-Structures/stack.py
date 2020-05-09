from node import Node

class Stack:
    def __init__(self, top_item=None, limit=1000):
        self.top_item = top_item
        self.limit = limit
        self.size = 0

    # Pushes a new item on top of the stack
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("Stack is currently full.")

    # Removes  the first item of the stack    
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_link_node()
            self.size -= 1
        
        return item_to_remove.get_value()

    
    # Returns the value of the first item of the top of the stack
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is currently empty")

    # Helper function that checks if the size is not greater than the limit
    def has_space(self):
        return self.limit > self.size

    # Helper function that cheks if the stack instance has a size of zero
    def is_empty(self):
        return self.size == 0 
    
    