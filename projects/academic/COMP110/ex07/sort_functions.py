"""Functions that implement sorting algorithms."""

__author__ = "730710373"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(1, len(x)): 
        unsorted_index = i 
        current_element = x[unsorted_index] 
        while unsorted_index > 0 and x[unsorted_index - 1] > current_element:
            x[unsorted_index] = x[unsorted_index - 1]
            unsorted_index -= 1
        x[unsorted_index] = current_element


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for i in range(len(x)):
        min_index = i 
        for j in range(i + 1, len(x)):  
            if x[j] < x[min_index]:
                min_index = j
        if min_index != i: 
            x[i], x[min_index] = x[min_index], x[i]