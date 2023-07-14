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



while gamestatusxo and on_move_index < 9:
    system("cls")
    print(source.welcome)
    source.gameboard(game_marks)
    
    mark_choise = 0
    while mark_choise not in range(1,10) and mark_choise not in game_marks.keys():
        print(mark_choise)
        print(mark_choise not in game_marks.keys())
        print(game_marks.keys())
        try:
            mark_choise = input(f"Player {on_move[on_move_index % 2]} | Enter your move number: ")
            if mark_choise == "E": 
                print("Thanks for play. Goodbye")
                quit(10)
            mark_choise = int(mark_choise)
        except ValueError:
            pass
        print("Wrong enter. Try again. ")

    game_marks[mark_choise] = on_move[on_move_index % 2]
    on_move_index += 1
    #source.gameboard(game_marks)
    gamestatusxo, winner = logic.gamestatus(game_marks)
    #print(gamestatusxo)
system("cls")
print(source.welcome)
source.gameboard(game_marks)
if on_move_index == 9 and winner == "": print("Draw")
else: print(f"{winner} WON !!!")
