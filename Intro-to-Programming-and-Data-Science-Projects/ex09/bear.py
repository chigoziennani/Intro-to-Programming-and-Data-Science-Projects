"""File to define Bear class."""
__author__ = "730710373"


class Bear:
    """Defines a Bear in the river ecosystem."""   
    def __init__(self):
        """Initialize a Bear with default age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        
    def one_day(self):
        """Simulate one day of aging and hunger increase for the Bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase Bear's hunger score after eating a specified number of fish."""
        self.hunger_score += num_fish