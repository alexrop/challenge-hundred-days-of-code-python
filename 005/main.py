# Day 5/100
# Based on user input, create a strong password 

################################################################################
# 0.- Libraries
################################################################################
import random
from typing import Optional

################################################################################
# 1.- Parameters
################################################################################
# Variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

list_of_combinations = [letters, symbols, numbers]

# Messages
welcome_message = '''Welcome to the PyPassword Generator!\n'''

n_letters_message = '''- How many letters would you like in your password?: '''
n_symbols_message = '''- How many symbols would you like?: '''
n_numbers_message = '''- How many numbers would you like?: '''

list_of_questions = [n_letters_message, n_symbols_message, n_numbers_message]

################################################################################
# 2.- Functions
################################################################################
def validate_input(prompt: str, dtype: type, allowed_values: Optional[list] = None) -> any:
    """
    Prompts the user for input and validates the data type and allowed values.
    
    Input
    -> prompt: The input prompt to display to the user.
    -> dtype: The expected data type (e.g., int, float).
    -> allowed_values: Optional list of valid values (default is None, meaning no restriction).

    Output
    -> Return: The validated input converted to the appropriate data type.
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

def user_choice(input_message:str) -> int:
    '''Function that ask to any user to add a int value of his/her choice based on an input message.'''
    return validate_input(input_message, int)

def user_random_elements(user_choice_values:list, possible_alternatives:list=list_of_combinations)->list:
    '''Function that wil take the user inputs and then will create a list based on his/her choices.'''
    result_list = []
    for user_value, list_of_combs in zip(user_choice_values,possible_alternatives):
        result_list.extend(random.choices(list_of_combs, k=user_value))

    ordered_results = result_list[:]

    random.shuffle(result_list)
    shuffled_results = result_list

    return ordered_results, shuffled_results


def run() -> None:
    '''Running Function'''
    # Print welcome message
    print(welcome_message)

    # Ask for the length of different characteres for ther making their password stronger
    # Store the values results into a list
    list_of_user_choices_values = []
    for question in list_of_questions:
        user_choice_value = user_choice(question)
        list_of_user_choices_values.append(user_choice_value)

    # Display ordered and shuffled alternatives, based on user inputs values
    ordered_results, shuffled_results = user_random_elements(list_of_user_choices_values, list_of_combinations)
    print('\n')
    print(ordered_results)
    print(shuffled_results)

    # Create
    password = ''.join(shuffled_results)
    print(f'\nYour password is: {password}')


if __name__ == '__main__':
    
    run()