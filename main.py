"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: David Smětala
email: x213@centrum.cz.com
discord: davids1682
"""

import source
import logic
from os import system

game_marks = {}
gamestatusxo = True
on_move = ["O", "X"]
on_move_index = 0
winner = ""
letter = False
oor = False
used_key = False




while gamestatusxo and on_move_index < 9:
    system("cls")
    print(source.welcome)
    source.gameboard(game_marks)

    if letter: print("Wrong enter. Try again! ")
    letter = False
    if oor: print("Out of range. Try again!")
    oor = False
    if used_key: print("There is mark already. Try again!")
    used_key = False

    mark_choise = input(f"{on_move[on_move_index % 2]} give me your move number: ")

    if mark_choise == "E":
        print("Thans for play. Goodbye")
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

    game_marks[mark_choise] = on_move[on_move_index % 2]
    on_move_index += 1
    gamestatusxo, winner = logic.gamestatus(game_marks)
    
system("cls")
print(source.welcome)
source.gameboard(game_marks)
if on_move_index == 9 and winner == "": print("Draw")
else: print(f"{winner} WON !!!")
