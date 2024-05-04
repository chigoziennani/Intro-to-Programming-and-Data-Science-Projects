"""File to define Bear class."""

__author__ = "730710373"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """A simple river ecosystem simulation."""
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove old Fish and Bears based on age limits."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Remove a specified amount of fish from the river."""
        self.fish = self.fish[amount:]
        
    def bears_eating(self):
        """Simulate Bears eating Fish if available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """Remove hungry Bears from the river."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self):
        """Repopulate Fish population by spawning new Fish."""
        num_fish = len(self.fish)
        new_fish = (num_fish // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Repopulate Bear population by spawning new Bears."""
        num_bears = len(self.bears)
        new_bears = num_bears // 2
        for _ in range(new_bears):
            self.bears.append(Bear())
    
    def view_river(self):
        """Display the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        self.day += 1
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(7):
            self.one_river_day()