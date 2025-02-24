# Day 6/100
# The challenge is the following: 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# The solution is a "pseudo-code" in python, which is on the IDE of the above website
# However, next is the solution that will work (only on the specific IDE from the challenge)

"""
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def wall_on_left():
    turn_around()
    if wall_on_right():
        turn_around()
        return True
    else:
        turn_around()
        return False
    
def is_right_corner():
    if wall_on_right() and not front_is_clear():
        return True
    else:
        return False

def is_left_corner():
    if wall_on_left() and not front_is_clear():
        return True
    else:
        return False
    
def is_street_with_no_exit():
    if wall_on_right() and wall_on_left() and not front_is_clear():
        return True
    else:
        return False
    
def is_right_facing_to_north():
    turn_right()
    if is_facing_north():
        turn_left()
        return True
    else:
        turn_left()
        return False

# Run
total_steps = 0
while not at_goal():
    if front_is_clear():
        if right_is_clear() and is_right_facing_to_north():
            turn_right()
            move()
        else:
            move()
        
    elif is_street_with_no_exit():
        turn_around()
        move()

    else:
        if is_right_corner():
            turn_left()
            move()
            
        else:
            turn_right()
            move()
            
    total_steps +=1
    
print(f"Total steps were {total_steps}")
"""