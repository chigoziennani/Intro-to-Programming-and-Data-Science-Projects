"""EX02 - One-Shot Battleship - A cute step toward One-Shot Battleship."""
 
__author__ = "730710373"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

guess_row: int = int(input("Guess a row: "))
while guess_row < 1 or guess_row > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ", end="")
    guess_row = int(input())

guess_column: int = int(input("Guess a column: "))
while guess_column < 1 or guess_column > grid_size:
    print(f"The grid is only {grid_size} by {grid_size}. Try again: ", end="")
    guess_column = int(input())

row_counter: int = 1
hit = False
close_message = ""
while row_counter <= grid_size:
    row_str: str = ""
    column_counter: int = 1
    while column_counter <= grid_size:
        if guess_row == row_counter and guess_column == column_counter:
            if guess_row == secret_row and guess_column == secret_column:
                row_str += RED_BOX
                hit = True
            else:
                row_str += WHITE_BOX
                if guess_row == secret_row:
                    close_message = "Close! Correct row, wrong column."
                elif guess_column == secret_column:
                    close_message = "Close! Correct column, wrong row."
        else:
            row_str += BLUE_BOX
        column_counter += 1
    print(row_str)
    row_counter += 1

if hit:
    print("Hit!")
elif close_message:
    print(close_message)
else:
    print("Miss!")