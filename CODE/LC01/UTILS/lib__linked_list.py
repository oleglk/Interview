# lib__linked_list.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from UTILS.lib__linked_list import *

# RELOAD:
# import importlib;  import UTILS.lib__linked_list;  importlib.reload(UTILS.lib__linked_list);  from UTILS.lib__linked_list import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

        
class LinkedList:
    def __init__(self):
        self.head = None  # The first node in the list

    #staticmethod
    def from_python_list(pyList):
        lst = LinkedList()
        if ( not pyList ):
            return(lst)
        for x in reversed(pyList):
            lst.prepend(x)
        return(lst)

    def append(self, data: int):
        """Adds a new node with key 'data' to the end of the list."""
        new_node = Node(data)
        return(self.append_node(new_node))

    ## Example of creating and printing cycled list:
    ##  lst = LinkedList();  lst.append(1);  e2 = lst.append(2);  lst.append_node(e2);    lst.display_limited(8)
    def append_node(self, new_node: Node):
        """Adds 'new_node' to the end of the list."""
        if ( new_node is None ):
            raise Exception("prepend(None)")
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return(new_node)

    def prepend(self, data: int):
        """Adds a new node with key 'data' to the beginning of the list."""
        new_node = Node(data)
        return(self.prepend_node(new_node))

    def prepend_node(self, new_node: Node):
        """Adds a new node to the beginning of the list."""
        if ( new_node is None ):
            raise Exception("prepend(None)")
        new_node.next = self.head
        self.head = new_node
        return(new_node)

    def delete(self, key):
        """Deletes the first node containing the given key."""
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:  # Key not found
            return

        prev_node.next = current_node.next
        current_node = None

    def display(self):
        """Prints the elements of the linked list."""
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        print(" -> ".join(map(str, elements)))

    def display_limited(self, maxCnt: int):
        """Prints up to 'maxCnt' elements of the linked list."""
        elements = []
        cnt = 0
        current_node = self.head
        while current_node and (cnt < maxCnt):
            cnt += 1
            elements.append(current_node.data)
            current_node = current_node.next
        continued = " ..." if (cnt >= maxCnt) else ""
        print(f'{" -> ".join(map(str, elements))}{continued}')

# Example Usage
def example_usage():
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.prepend(5)
    my_list.display()  # Output: 5 -> 10 -> 20

    my_list.delete(10)
    my_list.display()  # Output: 5 -> 20

    my_list.delete(5)
    my_list.display()  # Output: 20

    my_list.delete(30) # Deleting a non-existent element
    my_list.display() # Output: 20
