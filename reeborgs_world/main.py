def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        if is_facing_north():
            if front_is_clear():
                move()
            else:
                turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()
