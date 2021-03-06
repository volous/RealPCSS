class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, first, next=()):
        self.head = None
        self.first = first
        self.next = next

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        current = self.head

        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False