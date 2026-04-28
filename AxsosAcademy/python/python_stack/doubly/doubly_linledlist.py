class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None  # الفرق عن Singly

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # إضافة في النهاية
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

    # إضافة في البداية
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

    # حذف node بقيمة معينة
    def delete(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                # حالة: Node وحيدة
                if current.prev is None and current.next is None:
                    self.head = None
                    self.tail = None
                # حالة: Node في البداية
                elif current.prev is None:
                    self.head = current.next
                    self.head.prev = None
                # حالة: Node في النهاية
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                # حالة: Node في المنتصف
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return self
            current = current.next
        return self

    #  اضافةnode قبل قيمة معينة
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

    # طباعة من البداية للنهاية
    def print_forward(self):
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        print(" <-> ".join(values))
        return self

    # طباعة من النهاية للبداية
    def print_backward(self):
        current = self.tail
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.prev
        print(" <-> ".join(values))
        return self

    # الحصول على Node الوسط
    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    # حذف القيم المكررة
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

    # عكس  list
    def reverse(self):
        current = self.head
        while current is not None:
            # نبدّل next و prev لكل node
            current.next, current.prev = current.prev, current.next
            current = current.prev  # بعد التبديل، prev هي القديمة next
        # نبدّل head و tail
        self.head, self.tail = self.tail, self.head
        return self

    # التحقق من Circular List
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

# — اختبار —

if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("=== إضافة قيم ===")
    dll.add_to_back(1).add_to_back(2).add_to_back(3).add_to_back(4)
    dll.print_forward()   # 1 <-> 2 <-> 3 <-> 4

    print("\n=== إضافة في البداية ===")
    dll.add_to_front(0)
    dll.print_forward()   # 0 <-> 1 <-> 2 <-> 3 <-> 4

    print("\n=== حذف قيمة 2 ===")
    dll.delete(2)
    dll.print_forward()   # 0 <-> 1 <-> 3 <-> 4

    print("\n=== إدراج 99 قبل 3 ===")
    dll.insert_before(3, 99)
    dll.print_forward()   # 0 <-> 1 <-> 99 <-> 3 <-> 4

    print("\n=== الطباعة بالعكس ===")
    dll.print_backward()  # 4 <-> 3 <-> 99 <-> 1 <-> 0

    print("\n=== الوسط ===")
    print(dll.get_middle())

    print("\n=== عكس الـ List ===")
    dll.reverse()
    dll.print_forward()

    print("\n=== حذف المكررات ===")
    dll2 = DoublyLinkedList()
    dll2.add_to_back(1).add_to_back(2).add_to_back(2).add_to_back(3).add_to_back(1)
    dll2.print_forward()
    dll2.remove_duplicates()
    dll2.print_forward()

    print("\n=== Circular Check ===")
    print("Is circular?", dll.is_circular())  # False
