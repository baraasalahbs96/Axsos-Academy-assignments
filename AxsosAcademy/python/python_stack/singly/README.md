# Singly Linked List - Python
## Overview
Implementation of a **Singly Linked List** data structure in Python.
`singly_linked_list.py` — Contains the `SLNode` and `SList` classes
## Classes
`SLNode`
Represents a single node in the list.
|Attribute|Description                               
|`value`  |The data stored in the node               |
|`next`   |Pointer to the next node (default: `None`)|
`SList`
Represents the linked list itself.
|Method             Description                                  
|`add_to_front(val)`  |Adds a new node at the beginning of the list       |
|`add_to_back(val)`   |Adds a new node at the end of the list             |
|`print_values()`     |Prints all values from head to tail                |
|`remove_from_front()`|Removes and returns the first node’s value         |
|`remove_from_back()` |Removes and returns the last node’s value          |
|`remove_val(val)`    |Removes the first node that matches the given value|
|`insert_at(val, n)`  |Inserts a new node at position `n`                 |
> All methods return `self` to support **method chaining**.
## Usage Example
```python
my_list = SList()
my_list.add_to_front("are") \
       .add_to_front("Linked lists") \
       .add_to_back("fun!") \
       .print_values()
## Method Chaining Example
```python
my_list = SList()
my_list.add_to_front(1).add_to_front(2).add_to_back(3).print_values()
## 
- Adding to back when list is **empty** → calls `add_to_front` instead
- Removing from **empty list** → returns `None`
- `remove_val` on a value that is the **head node**
- `insert_at` with `n = 0` → inserts at front
-----
- Linked list structure (nodes + pointers)
- Traversal using a `runner` variable
- The difference between **indexed arrays** and **pointer-based lists**
- Method chaining with `return self`