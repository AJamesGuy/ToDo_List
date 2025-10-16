# Create Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
        return new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return new_node
    
    def delete_at_position(self, position):
        if position < 1 or position > self.size:
            return
        current = self.head
        for _ in range(1, position - 1): # Iterate to position before node_to_delete/position
            current = current.next
        node_to_delete = current.next
        current.next = node_to_delete.next
        self.size -= 1
        return node_to_delete

    def insert_at_position(self, position, data):
        if position < 1 or position > self.size: # Insert Out of Bounds
            return
        new_node = Node(data)
        current = self.head
        if position == 1: # If position is 1, prepend method (updates the head)
            self.prepend(new_node.data)
            return
        if position == self.size(): # If position is last in linkedlist, append method (updates the tail)
            self.append(new_node.data)
            return
        for _ in range(1, position - 1): # Iterate to position before insertion
            current = current.next
        # Insertion Logic
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return new_node

    def get_at_position(self, position):
        if position < 1 or position > self.size:
            return
        if position == 1:
            return self.head
        current = self.head
        for _ in range(1, position - 1):
            current = current.next
        return current.next
    
    def traverse(self):
        current = self.head
        while current:
            print(f"- {current.data}")
            current = current.next
    