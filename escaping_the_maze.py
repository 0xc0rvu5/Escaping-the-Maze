#refer too:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json


#code to help Reeborg finish the maze
#front_is_clear(), move(), at_goal(), right_is_clear(), turn_left() are all functions already integrated into Reeborg's World
def turn_right():
    turn_left()
    turn_left()
    turn_left()


#edge case
while front_is_clear():
    move()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()