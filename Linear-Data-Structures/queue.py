from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    # Add node value to the end of the queue
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            # If there are no nodes in queue set first value to be both the head and tail
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    # Removes the head node in the queue
    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print("Removing " + str(item_to_get.get_value()) + " from the queue")
            # If queue only has a single data point just set head and tail to None
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                # Set head to the next linked node
                self.head = self.head.get_link_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")

    # Return the value of the first self.head data
    def peek(self):
        if self.size > 0:
            return self.head.get_value()

    # Check to see if queue has available space
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.size
    
    # Return the current data nodes in the queue
    def get_size(self):
        return self.size

    # Check to see if the queue size is empty
    def is_empty(self):
        return self.size == 0




