class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None  
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_back(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return self
    
    def add_to_front(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return self
    
    def delete(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                if current.prev is None and current.next is None:
                    self.head = None
                    self.tail = None
                elif current.prev is None:
                    self.head = current.next
                    self.head.prev = None
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return self
            current = current.next
        return self
    
    def insert_before(self, target_val, new_val):
        current = self.head
        while current is not None:
            if current.value == target_val:
                if current.prev is None:
                    return self.add_to_front(new_val)
                new_node = Node(new_val)
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                return self
            current = current.next
        return self

    def print_forward(self):
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        print(" <-> ".join(values))
        return self

    def print_backward(self):
        current = self.tail
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.prev
        print(" <-> ".join(values))
        return self

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def remove_duplicates(self):
        seen = set()
        current = self.head
        while current is not None:
            if current.value in seen:
                next_node = current.next
                self.delete(current.value)
                current = next_node
            else:
                seen.add(current.value)
                current = current.next
        return self

    def reverse(self):
        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev  
        self.head, self.tail = self.tail, self.head
        return self

    def is_circular(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
