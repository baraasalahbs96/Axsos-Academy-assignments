class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
class SList:
    def __init__(self):
        self.head = None
    # إضافة في البداية
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    # طباعة كل القيم
    def print_values(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        return self
    # إضافة في النهاية
    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        current = self.head
        while current.next != None:
           current = current.next
        current.next = new_node
        return self
    # حذف من البداية
    def remove_from_front(self):
        if self.head == None:
            return None
        removed = self.head
        self.head = self.head.next
        return removed.value
    # حذف من النهاية
    def remove_from_back(self):
        if self.head == None:
            return None
        if self.head.next == None:
            removed = self.head
            self.head = None
            return removed.value
        current = self.head
        while current.next.next != None:
            current = current.next
        removed = current.next
        current.next = None
        return removed.value
    #  حذف أول node بقيمة معينة
    def remove_val(self, val):
        if self.head == None:
            return None
        if self.head.value == val:
            return self.remove_from_front()
        current = self.head
        while current.next != None:
            if current.next.value == val:
                current.next = current.next.next
                return val
            current = current.next
        return None
    #  إدراج في موقع n
    def insert_at(self, val, n):
        if n == 0:
            return self.add_to_front(val)
        current = self.head
        for i in range(n - 1):
            if current == None:
                return self
            current = current.next
        if current == None:
            return self
        new_node = SLNode(val)
        new_node.next = current.next
        current.next = new_node
        return self
# مثال
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
