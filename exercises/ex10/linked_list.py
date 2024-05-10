"""Utility functions for working with Linked Lists."""
 
from __future__ import annotations
 
__author__ = "730710373"
 
 
class Node:
    """An item in a singly-linked list."""
    data: int
    next: Node | None
 
    def __init__(self, data: int, next: Node | None):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next
 
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return the data attribute of the first element in the linked list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return a linked list of every element minus the head."""
        return self.next
    
    def last(self) -> int:
        """Return the data of the last element in the linked list."""
        current = self
        while current.next is not None:
            current = current.next
        return current.data
    

def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    
    max_value = head.data
    current = head.next
    
    while current is not None:
        if current.data > max_value:
            max_value = current.data
        current = current.next

    return max_value


def linkify(items: list[int]) -> Node | None:
    """Return a Linked List of Nodes with the same values as the input list."""
    if not items:
        return None
    
    head = Node(items[0], None)
    current = head
    
    for item in items[1:]:
        current.next = Node(item, None)
        current = current.next
    
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list where each value is scaled by the factor."""
    if head is None:
        return None
    
    scaled_head = Node(head.data * factor, None)
    current = head.next
    scaled_current = scaled_head
    
    while current is not None:
        scaled_current.next = Node(current.data * factor, None)
        current = current.next
        scaled_current = scaled_current.next
    
    return scaled_head