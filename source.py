# initial text part
welcome = """Welcome to Game machine!!!
========================================
I have 2 really good games for your fun.
You can choose wich one you want to play.
Press T for Tic Tac Toe or
press B for Bulls & Cows.
========================================
Let's choose the game
If you want to exit press E"""

possible_chooses = ["E", "T", "B"]

# initial text part for Tic Tac Toe
welcomexo = """Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game
If you want to exit press E"""

# rewrites gameboard according to used marks already recorded in gamemarks dictonary
def gameboard(gamemarks):
    gameboard = """
-------------------------
|1      |2      |3      |
|       |       |       |
|       |       |       |
-------------------------
|4      |5      |6      |
|       |       |       |
|       |       |       |
-------------------------
|7      |8      |9      |
|       |       |       |
|       |       |       |
-------------------------
"""
    for board_num, board_mark in gamemarks.items():      
        if board_num in range(1,4): gameboard = gameboard[:(57 + ((board_num - 1) * 8))] + board_mark + gameboard[(57 + ((board_num - 1) * 8))+1:]
        elif board_num in range(4,7): gameboard = gameboard[:(161 + ((board_num - 4) * 8))] + board_mark + gameboard[(161 + ((board_num - 4) * 8))+1:]
        elif board_num in range(7,10): gameboard = gameboard[:(265 + ((board_num - 7) * 8))] + board_mark + gameboard[(265 + ((board_num - 7) * 8))+1:]

    print(gameboard)

# initial text part for Bulls & Cows.
welcomebc = """Welcome to Bulls & Cows
========================================
GAME RULES:
I've generated a random 4 digit number
for you. The digits are all different.
If the matching digits are in their 
right positions, they are "bulls", 
if in different positions, they are "cows"
You win when reveal secret number.
========================================
Let's play a Bulls & Cows game.
If you want to exit press E"""
