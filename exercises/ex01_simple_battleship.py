"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730710373"

secret_boat_guess1: str = input("Pick a secret boat location between 1 and 4: ")

if int(secret_boat_guess1) < 1:
    print("Error! " + secret_boat_guess1 + " too low!")
    exit()
elif int(secret_boat_guess1) > 4:
    print("Error! " + secret_boat_guess1 + " too high!")
    exit()

number_guess2: str = input("Guess a number between 1 and 4: ")
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if int(number_guess2) < 1:
    print("Error! " + number_guess2 + " too low!")
    exit()
elif int(number_guess2) > 4:
    print("Error! " + number_guess2 + " too high!")
    exit()
else:
    result: str = ""
    if int(secret_boat_guess1) == 1:
        result += RED_BOX if int(number_guess2) == 1 else BLUE_BOX
        result += BLUE_BOX if int(number_guess2) != 1 else ""
        result += BLUE_BOX if int(number_guess2) != 2 else ""
        result += BLUE_BOX if int(number_guess2) != 3 else ""
        result += BLUE_BOX if int(number_guess2) != 4 else ""
    elif int(secret_boat_guess1) == 2:
        result += BLUE_BOX if int(number_guess2) != 1 else ""
        result += RED_BOX if int(number_guess2) == 2 else BLUE_BOX
        result += BLUE_BOX if int(number_guess2) != 2 else ""
        result += BLUE_BOX if int(number_guess2) != 3 else ""
        result += BLUE_BOX if int(number_guess2) != 4 else ""
    elif int(secret_boat_guess1) == 3:
        result += BLUE_BOX if int(number_guess2) != 1 else ""
        result += BLUE_BOX if int(number_guess2) != 2 else ""
        result += RED_BOX if int(number_guess2) == 3 else BLUE_BOX
        result += BLUE_BOX if int(number_guess2) != 3 else ""
        result += BLUE_BOX if int(number_guess2) != 4 else ""
    elif int(secret_boat_guess1) == 4:
        result += BLUE_BOX if int(number_guess2) != 1 else ""
        result += BLUE_BOX if int(number_guess2) != 2 else ""
        result += BLUE_BOX if int(number_guess2) != 3 else ""
        result += RED_BOX if int(number_guess2) == 4 else BLUE_BOX
    else:
        result = BLUE_BOX * 4

    print(result)
    if int(number_guess2) == int(secret_boat_guess1):
        print("Correct! You hit the ship.")
    else:
        print("Incorrect! You missed the ship.")