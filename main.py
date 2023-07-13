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


while gamestatusxo and (on_move_index < 9):
    #system("cls")
    print(source.welcome)
    source.gameboard(game_marks)
    mark_choise = int(input(f"Player {on_move[on_move_index % 2]} | Enter your move number: "))
    game_marks[mark_choise] = on_move[on_move_index % 2]
    on_move_index += 1
    #source.gameboard(game_marks)
    gamestatusxo, winner = logic.gamestatus(game_marks)
    #print(gamestatusxo)
source.gameboard(game_marks)
if on_move_index == 9: print("Draw")
else: print(f"{winner} WON !!!")
