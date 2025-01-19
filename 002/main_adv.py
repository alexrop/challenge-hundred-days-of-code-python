# Day 2/100
# Create a program that runs a tip calculator based on certain logics
# It has to return the total amount of money per each people of the bill.
# Step 1: Ask the total bill amount
# Step 2: Request the total tip percentage to donate
# Step 3: Ask fot the total of people to split the bill

# Math Operations Orders:
# PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Substraction

from typing import Optional

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

def tip_calculator()->float:
    '''Function that based on the total bill, it returns the total amount of money per each people of the bill.'''
    
    total_bill = validate_input('-What was the total bill?: ', float)
    tip_to_give = validate_input('-How much tip would you like to give? 10, 12, or 15: ', int, allowed_values=[10, 12, 15])
    people_to_split = validate_input('-How many people to split the bill: ', int)

    calculator = (total_bill + (total_bill * tip_to_give/100))/people_to_split

    return calculator

if __name__ == "__main__":
    print('Welcome to the tip calculator!\n')

    money_to_pay = tip_calculator()

    print(f'\nEach person should pay: ${round(money_to_pay,2):.2f}')