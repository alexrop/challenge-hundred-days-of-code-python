# Day 3/100
# Create a program that based on situations a correct anwswer, tells you when a treasure is found.
# If is not the case, the result must be "Game over".

from typing import Optional

#############################################################
## 1.- General messages
#############################################################
background = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************'''

welcome_message = '''Welcome to Treasure Island!!
Your mission is to find the treasure.\n
'''

first_valid_question = '''-You're at a cross road. Where do you want to go? Type "left" or "right": '''
second_valid_question = '''-You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across: '''
third_valid_question = '''-You arrive at the island unharmed. There is a house with 3 doors: One "red", one "yellow" and one "blue". Which colour do you choose?: '''

winning_message = '''\nYou found the treasure! You Win!!'''

first_losing_message = '''\nYou fell into a hole. Game Over.'''
second_losing_message = '''\nYou get attacked by an angry trout. Game Over.'''
third_losing_message_1 = '''\nIt's a room full of fire. Game Over.'''
third_losing_message_2 = '''\nYou enter a room of beasts. Game Over.'''

#############################################################
## 2.- Functions
#############################################################
def welcome(background:str, message:str)->None:
    '''Function that prints out the welcome message to players.'''
    print(background)
    print(message)

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

def run():
    '''Running function'''
    welcome(background, welcome_message)

    first_input = validate_input(first_valid_question, str, allowed_values=['left', 'right'])
    if first_input[0] != 'l':
        print(first_losing_message)
    
    else:
        second_input = validate_input(second_valid_question, str, allowed_values=['wait', 'swim']).lower()

        if second_input[0] != 'w':
            print(second_losing_message)
        else:
            third_input = validate_input(third_valid_question, str, allowed_values=['red', 'yellow', 'blue']).lower()

            if third_input[0] != 'y':
                if third_input[0] == 'r':
                    print(third_losing_message_1)
                elif third_input[0] == 'b':
                    print(third_losing_message_2)
                else:
                    pass
            else:
                print(winning_message)

if __name__ == "__main__":   
    run()