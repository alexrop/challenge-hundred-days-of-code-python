# Day 2/100
# Create a program that runs a tip calculator based on certain logics
# It has to return the total amount of money per each people of the bill.
# Step 1: Ask the total bill amount
# Step 2: Request the total tip percentage to donate
# Step 3: Ask fot the total of people to split the bill

# Math Operations Orders:
# PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Substraction

def tip_calculator()->float:
    '''Function that based on the total bill, it returns the total amount of money per each people of the bill.'''
    
    total_bill = float(input('-What was the total bill?: '))
    tip_to_give = int(input('-How much tip would you like to give? 10, 12, or 15: '))
    people_to_split = int(input('-How many people to split the bill: '))

    calculator = (total_bill + (total_bill * tip_to_give/100))/people_to_split

    return calculator

if __name__ == "__main__":
    print('Welcome to the tip calculator!\n')

    money_to_pay = tip_calculator()

    print(f'\nEach person should pay: ${round(money_to_pay,2):.2f}')