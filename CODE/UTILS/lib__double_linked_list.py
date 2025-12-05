# lib__double_linked_list.py - double linked list implementation from https://chalmersgu-data-structure-courses.github.io/OpenDSA/Published/ChalmersGU-DSABook/html/ListDouble.html


# Python does not have internal classes, so we have to make the list node standalone.
class DoubleLinkedListNode:
    def __init__(self, elem, prev, next):
        self.elem = elem   # Value for this node
        self.prev = prev   # Pointer to previous node in list
        self.next = next   # Pointer to next node in list
####


class DoubleLinkedList(List):
    def __init__(self):
        self._head = None    # Pointer to list header
        self._tail = None    # Pointer to list tail
        self._listSize = 0   # Size of list

    def get(self, i):
        if not (0 <= i < self._listSize): raise IndexError("list index out of range")
        current = self._head
        for _ in range(i):
            current = current.next
        return current.elem

    def set(self, i, x):
        if not (0 <= i < self._listSize): raise IndexError("list index out of range")
        current = self._head
        for _ in range(i):
            current = current.next
        old = current.elem
        current.elem = x
        return old

    def add(self, i, x):
        if not (0 <= i <= self._listSize): raise IndexError("list index out of range")
        if self._listSize == 0:
            self._head = self._tail = DoubleLinkedListNode(x, None, None)
        elif i == 0:
            newhead = DoubleLinkedListNode(x, None, self._head)
            self._head.prev = newhead
            self._head = newhead
        elif i == self._listSize:
            newtail = DoubleLinkedListNode(x, self._tail, None)
            self._tail.next = newtail
            self._tail = newtail
        else:
            prev = self._head
            for _ in range(i-1):
                prev = prev.next
            next  = prev.next
            newnode = DoubleLinkedListNode(x, prev, next)
            prev.next = newnode
            next.prev = newnode
        self._listSize += 1

    def remove(self, i):
        if not (0 <= i < self._listSize): raise IndexError("list index out of range")
        if i == 0:
            removed = self._head
            self._head = removed.next
            self._head.prev = None
        elif i == self._listSize-1:
            removed = self._tail
            self._tail = removed.prev
            self._tail.next = None
        else:
            prev = self._head
            for _ in range(i-1):
                prev = prev.next
            removed = prev.next
            prev.next = removed.next
            prev.next.prev = prev
        removed.prev = removed.next = None   # For garbage collection
        self._listSize -= 1
        return removed.elem

    def isEmpty(self):
        return self._listSize == 0

    def size(self):
        return self._listSize

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.elem
            current = current.next
####


