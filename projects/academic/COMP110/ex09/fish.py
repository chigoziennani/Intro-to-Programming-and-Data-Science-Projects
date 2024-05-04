"""File to define Fish class."""
__author__ = "730710373"


class Fish:
    """Defines a Fish in the river ecosystem."""
    def __init__(self):
        """Initialize a Fish with default age."""
        self.age = 0
        
    def one_day(self):
        """Simulate one day of aging for the Fish."""
        self.age += 1