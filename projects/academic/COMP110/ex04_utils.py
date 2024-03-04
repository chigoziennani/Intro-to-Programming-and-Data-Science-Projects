"""EX04 - List Utility Functions - A cute step toward List Utility Functions."""

__author__ = "730710373"

def all(lst: list[int], num: int) -> bool:
    """Pretend this was a meaningful docstring."""
    if len(lst) == 0:
        return False
    for item in lst:
        if item != num:
            return False
    return True

def max(lst: list[int]) -> int:
    """Pretend this was a meaningful docstring."""
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = lst[0] 
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Pretend this was a meaningful docstring."""
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

def extend(lst1: list[int], lst2: list[int]) -> None:
    """Pretend this was a meaningful docstring."""
    for num in lst2:
        lst1.append(num)
    return None