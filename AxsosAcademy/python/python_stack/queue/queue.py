# 1. Reverse a String Using a Stack
class Stack:
    def __init__(self):
        self.elems = []
        
    def pop(self):
        return self.elems.pop() if self.elems else None
    
    def push(self, val):
        self.elems.append(val)
    
    def peek(self):
        return self.elems[-1] if self.elems else None
    
def reverse_string(text):
    stack = Stack()
    for char in text:
        stack.push(char)
        
    reversed_text = ""
    while len(stack.elems) > 0:
        reversed_text += stack.pop()
        
    return reversed_text

print(reverse_string("abc"))
    
# 2. For each temperature find how many days until a warmer temperature.
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = Stack()
    for i in range(len(temps)):
       while stack.elems and temps[i] > temps[stack.elems[-1]]:
           idx = stack.pop()
           result[idx] = i - idx  
       stack.push(i)
    return result



print(daily_temperatures([50,10,8,25,30]))


# 3. First Non-Repeating Character in a Stream. As characters arrive return the first non-repeating one.

class Queue:
    def __init__(self):
        self.elems = []
        
    def Enqueue(self, val):
        self.elems.append(val)

    def Dequeue(self):
        if self.elems:
            return self.elems.pop(0)
    
    def Peek(self):
        return self.elems[0] if self.elems else None
    
    
def first_non_repeating(stream):

    queue = Queue()
    frequency = {}

    for char in stream:
        if char not in frequency:
            frequency[char] = 0

        frequency[char] += 1

        # Add character to queue
        queue.Enqueue(char)

        # Remove repeated characters from front
        while len(queue.elems) > 0 and frequency[queue.Peek()] > 1:
            queue.Dequeue()

        # Print first non-repeating character
        if len(queue.elems) > 0:
            print(queue.Peek())
        else:
            print(-1)


first_non_repeating("aabcbd")