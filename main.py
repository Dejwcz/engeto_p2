"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: David Smětala
email: x213@centrum.cz.com
discord: davids1682
"""

import source
import logic
from time import time
from os import system

start_time = time()
game_marks = {}
gamestatusxo = True
on_move = ["O", "X"]
on_move_index = 0
winner = ""
letter = False
oor = False
used_key = False
line = "="*40

# program runs until someone win or is game board full without a winner
while gamestatusxo and on_move_index < 9:
    system("cls")
    print(source.welcome)
    source.gameboard(game_marks)
    print(line)

# annoucment for all types of wrong inputs
    if letter: print("Wrong enter. Try again! ")
    letter = False
    if oor: print("Out of range. Try again! ")
    oor = False
    if used_key: print("There is mark already. Try again! ")
    used_key = False

# choices number of square in game board. E is for exit program. Identification of mistakes in input 
    mark_choise = input(f"{on_move[on_move_index % 2]} give me your move number: ")
    print(line)

    if mark_choise == "E":
        print("Thanks for play. Goodbye".center(40))
        end_time = time()
        logic.timeplay(start_time, end_time)
        print(line)
        quit(10)
    try:
        mark_choise = int(mark_choise)
    except ValueError:
        letter = True
        continue
    
    if mark_choise not in range(1,10):
        oor = True
        continue
    
    if mark_choise in game_marks.keys():
        used_key = True
        continue

# adds players choise to dictonary and evaluates if someone won
    game_marks[mark_choise] = on_move[on_move_index % 2]
    on_move_index += 1
    gamestatusxo, winner = logic.gamestatus(game_marks)
    
system("cls")
print(source.welcome)
source.gameboard(game_marks)
print(line)
if on_move_index == 9 and winner == "": print("Draw".center(40))
else: print(f"Congratulations, the player {winner} WON!".center(40))
end_time = time()
logic.timeplay(start_time, end_time)
print(line)