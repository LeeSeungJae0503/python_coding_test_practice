class Node(object):
    def __init__(self, data):
        self.value = data
        self.next = None
    
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
           current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return 
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next
                return 
            current = current.next

class Double_Node(object):
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class Double_LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Double_Node(data)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")