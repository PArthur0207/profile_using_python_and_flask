class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def remove_at_beginning(self):
        if self.head:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.data
        return None
    
    def remove_at_end(self):
        if self.head:
            if self.head == self.tail:
                removed_node = self.head
                self.head = None
                self.tail = None
                return removed_node.data
            else:
                removed_node = self.tail
                current_node = self.head
                while current_node.next != removed_node:
                    current_node = current_node.next
                self.tail = current_node
                self.tail.next = None
                return removed_node.data
        return None
    
    def remove_at(self, data):
        if self.head:
            if self.head.data == data:
                return self.remove_at_beginning()
            elif self.tail.data == data:
                return self.remove_at_end()
            else:
                current_node = self.head
                while current_node.next and current_node.next.data != data:
                    current_node = current_node.next
                if not current_node.next:
                    return "Data not in list"
                removed_node = current_node.next
                current_node.next = removed_node.next
                return removed_node.data
        return None