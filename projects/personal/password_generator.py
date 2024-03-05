"""A simple complex-password generator based on user input created by Chigozie Nnani."""
import random

# all possible characters to be used for generated password
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special_characters = "!@#$*"

# defining function that will create generated password
def generated_password(length = 16, use_letters = True, use_numbers = True, use_special = True):
    # blank list for character storage
    characters = []
    # using characters based on user choices
    if use_letters:
        characters.extend(letters)
    if use_numbers:
        characters.extend(numbers)
    if use_special:
        characters.extend(special_characters)
    if not (use_letters or use_numbers or use_special):
        print("Please choose at least one type of characters.")
        return None

    # generate password using random.choice() to randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# get user's choices for types of characters
def get_user_choices():
    print("Choose the types of characters you wish to include in your password:")
    print("1. Letters")
    print("2. Numbers")
    print("3. Special characters")
    
    # get user input
    choices = input("Enter your choice(s) separated by commas (e.g., 1,2,3) or spaces (e.g., 1 2 3): ").split(',')
    if len(choices) == 1:  # if no commas found, try splitting by space
        choices = choices[0].split()
    # remove spaces from each choice and convert to integers
    choices = [int(choice.strip()) for choice in choices]
    use_letters = 1 in choices
    use_numbers = 2 in choices
    use_special = 3 in choices
    return use_letters, use_numbers, use_special

# terminal output/input prompts when program is run
if __name__ == "__main__":
    length = int(input("Enter the length of your desired password: "))
    use_letters, use_numbers, use_special = get_user_choices()
    password = generated_password(length, use_letters, use_numbers, use_special)
    if password:
        print("Here is your randomly generated password:", password)