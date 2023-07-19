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
from random import randint



wrong_choose = False
total_start_time = time()
line = "="*40

while True:
    system("cls")
    print(source.welcome)
    print(line)
    if wrong_choose:
        print("Wrong enter!")
        wrong_choose = False
    game_choose = input("Give me your option: ")
    if game_choose not in source.possible_chooses:
        wrong_choose = True
        continue
    if game_choose == "E":
        print(line)
        print("Thanks for using Game machine. Goodbye".center(40))
        end_time = time()
        logic.timeplay(total_start_time, end_time, True)
        print(line)
        quit(1)
    if game_choose == "T":
        # Tic Tac Toe program runs until someone win or is game board full without a winner
        start_time_xo = time()
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
            print(source.welcomexo)
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
                logic.timeplay(start_time_xo, end_time, False)
                print(line)
                gamestatusxo = False
                continue
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
        print(source.welcomexo)
        source.gameboard(game_marks)
        print(line)
        if on_move_index == 9 and winner == "": print("Draw".center(40))
        else: print(f"Congratulations, the player {winner} WON!".center(40))
        end_time = time()
        logic.timeplay(start_time_xo, end_time, False)
        print(line)
        input("Press enter to continue".center(40))
    if game_choose == "B":
    
        gamestatusbc = True
        players_number = ""

        # prints greetings, rules, generates number, gets start time
        system("cls")
        print(source.welcomebc)
        guesed_number = logic.give_random_number()
        print(guesed_number)
        start_time_bc = time()
        error = ""
        attempts = 0

        # plays until player do not hit right number or press E
        while gamestatusbc:
            if error != "": print(error)
            print(line)
            players_number = input("Give me your number: ")
            if players_number == "E":
                print("Thanks for play. Goodbye".center(40))
                end_time = time()
                logic.timeplay(start_time_bc, end_time, False)
                print(line)
                gamestatusbc = False
                continue
            error = logic.check_number(players_number)
            if error != "": continue
            players_number = [int(num) for num in players_number]
            cows, bulls = logic.bacevaluation(guesed_number, players_number)
            logic.bacverdict(cows, bulls)
            attempts += 1
            if bulls == 4: gamestatusbc = False
        # gives feedback about game
        logic.bacfeedback(attempts)
        end_time = time()
        logic.timeplay(start_time_bc, end_time, False)
        print(line)
        input("Press enter to continue".center(40))