def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_left()