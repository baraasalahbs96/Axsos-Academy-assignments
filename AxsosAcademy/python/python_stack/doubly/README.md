# Doubly Linked List - Python
## Overview
Implementation of a **Doubly Linked List** (DList) data structure in Python.  
Unlike a Singly Linked List, each node has **two pointers**: one to the next node and one to the previous node.
## Singly vs Doubly 
Singly Linked List     |Doubly Linked List 
|Pointers per node
(`next`)                (`next`    +`prev`)
Traversal:Forward only|  Forward & Backward 
Delete node           |Need previous node reference.            |Can delete directly

- `doubly_linked_list.py` — Contains the `Node` and `DoublyLinkedList` classes
## Classes

### `Node`

Represents a single node in the doubly linked list.

|Attribute|Description                 |
|---------|----------------------------|
|`value`  |The data stored in the node |
|`next`   |Pointer to the next node    |
|`prev`   |Pointer to the previous node|

### `DoublyLinkedList`

Method                              Description                              
|`add_to_back(val)`                  Adds a new node at the end                             
|`add_to_front(val)`                 Adds a new node at the beginning                        
|`delete(val)`                       Deletes the first node with the given value             |
|`insert_before(target_val, new_val)`Inserts a new node before a given value                 |
|`print_forward()`                   Prints all values from head to tail                     |
|`print_backward()`                  |Prints all values from tail to head                     |
|`get_middle()`                      |Returns the middle node’s value (uses slow/fast pointer)|
|`remove_duplicates()`               |Removes all duplicate values                            |
|`reverse()`                         |Reverses the entire list in-place                       |
|`is_circular()`                     |Returns `True` if the list is circular                  |

## Usage Example

```python
dll = DoublyLinkedList()
dll.add_to_back(1).add_to_back(2).add_to_back(3)
dll.print_forward()   # 1 <-> 2 <-> 3
dll.print_backward()  # 3 <-> 2 <-> 1

dll.delete(2)
dll.print_forward()   # 1 <-> 3

dll.insert_before(3, 99)
dll.print_forward()   # 1 <-> 99 <-> 3
```
## Puzzle Answers

### 1. How would you know if you have a circular linked list?

Use the **Floyd’s Cycle Detection** algorithm (slow & fast pointers).  
If the slow and fast pointers ever meet, the list is circular.

### 2. How would you get to the middle of the list?

Use two pointers: `slow` moves 1 step, `fast` moves 2 steps.  
When `fast` reaches the end, `slow` is at the middle.

### 3. How would you remove duplicate values?

Use a `set` to track seen values.  
Traverse the list — if a value was seen before, delete that node.

### 4. How would you reverse the values in the list?

Traverse each node and swap its `next` and `prev` pointers.  
Then swap `head` and `tail`.
