"""EX03 - Functional Battleship - A cute step toward Functional Battleship."""
 
__author__ = "730710373"

import random

def input_guess(size: int, type: str) -> int:
    """Prompt user for a row or column guess and return it."""
    assert type == "row" or type == "column"
    if type == "row":
        message = "Guess a row: "
        error_message = f"The grid is only {size} by {size}. Try again: "
    else:
        message = "Guess a column: "
        error_message = f"The grid is only {size} by {size}. Try again: "
    guess = int(input(message))
    while guess < 1 or guess > size:
        guess = int(input(error_message))
    return guess

def print_grid(size: int, row_guess: int, col_guess: int, correct_guess: bool) -> None:
    """Print grid with boxes representing the game board."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"
    i = 0
    while i < size:
        j = 0
        while j < size:
            if i == row_guess - 1 and j == col_guess - 1:
                if correct_guess:
                    print(RED_BOX, end="")
                else:
                    print(WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
            j += 1
        print()
        i += 1

def correct_guess(secret_row: int, secret_col: int, row_guess: int, col_guess: int) -> bool:
    """Check if user's guess matches secret boat location."""
    return secret_row == row_guess and secret_col == col_guess

def main(grid_size: int, secret_row: int, secret_col: int) -> None:
    """Run main game loop."""
    MAX_TURNS = 5
    current_turn = 0
    won = False
    while current_turn < MAX_TURNS and not won:
        current_turn += 1
        print(f"=== Turn {current_turn}/{MAX_TURNS} ===")
        row_guess = input_guess(grid_size, "row")
        col_guess = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_col, row_guess, col_guess)
        print_grid(grid_size, row_guess, col_guess, correct)
        if correct:
            print("Hit!")
            print(f"You won in {current_turn}/{MAX_TURNS} turns!")
            won = True
        else:
            print("Miss!")
    if not won:
        print(f"X/{MAX_TURNS} - Better luck next time!")

if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))