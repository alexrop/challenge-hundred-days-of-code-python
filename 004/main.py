# Day 4/100
# Create a program that emulate the rock paper and scissors game
# The user must have to choose a number (0: rock, 1: paper, 2: scissors) and the computer randomly will chose an alternative.
# The rules are: rock beats scissors, scissors beats paper, and paper beats rock

################################################################################
# 0.- Libraries
################################################################################
import random
from typing import Optional

################################################################################
# 1.- General messages
################################################################################
rock_background = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper_background = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissors_background = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

background_list = [rock_background, paper_background, scissors_background]
welcome_message = '''Welcome to Rock, Paper & Scissor game!🤖🤟\n'''
user_choice_message = '''What alternative would you like to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '''

# 0: rock, 1: paper, 2: scissors
rule_logics = {'win': [(0,2), (1,0), (2,1)],
               'lose': [(2,0), (0,1), (1,2)]
              }

################################################################################
# 2.- Functions
################################################################################
def validate_input(prompt: str, dtype: type, allowed_values: Optional[list] = None) -> any:
    """
    Prompts the user for input and validates the data type and allowed values.
    
    :param prompt: The input prompt to display to the user.
    :param dtype: The expected data type (e.g., int, float).
    :param allowed_values: Optional list of valid values (default is None, meaning no restriction).
    :return: The validated input converted to the appropriate data type.
    """
    
    while True:
        try:
            user_input = dtype(input(prompt))  # Convert input to the desired data type
            if allowed_values and user_input not in allowed_values:
                print(f"\tInvalid input. Allowed values are: {allowed_values}")
            else:
                return user_input
        except ValueError:
            print(f"\tPlease enter a valid {dtype.__name__}.")

def user_choice(user_choice_message:str, background_list:list)->int:
    '''Function for storing the user choice, and printing out the respective figure (0: rock, 1: paper, 2: scissors).'''
    user_value = validate_input(user_choice_message, int, allowed_values=[0,1,2])
    print('\nYour choice:')

    if user_value == 0:
        print(background_list[0])

    elif user_value == 1:
        print(background_list[1])

    elif user_value == 2:
        print(background_list[2])

    return user_value

def computer_choice():
    '''Function for generating a random choice between 0,1 and 2 values.'''
    computer_value = random.choice([0,1,2])  # I could also use: random.randint(0,2)
    print("\nComputer's choice:")

    if computer_value == 0:
        print(background_list[0])

    elif computer_value == 1:
        print(background_list[1])

    elif computer_value == 2:
        print(background_list[2])

    return computer_value


def game_evaluation(user_choice:int, computer_choice:int, rules:dict=rule_logics)->None:
    '''Evaluate user choice vs computer random choice to see the result of the game.'''
    if user_choice == computer_choice:
        print("\nIt's a draw!")

    elif (user_choice, computer_choice) in rule_logics['win']:
        print("\nYou WIN!!!")

    elif (user_choice, computer_choice) in rule_logics['lose']:
        print("\nYou lose :(")

    else:
        print('\nNo valid result.')

def run()->None:
    '''Running function'''

    # Printing initial message for playing
    print(welcome_message)

    # Ask user to insert a valid value
    user_choice_value = user_choice(user_choice_message, background_list)

    # Generates a computer random choice
    computer_choice_value = computer_choice()

    # Display results (win, lose, draw)
    game_evaluation(user_choice_value, computer_choice_value)

if __name__ == '__main__':
    run()
