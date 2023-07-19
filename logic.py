
# rewrites gamemarks to matrix and then decides if there are any "3 in row".
# if there are "3 in row" returns True value and mark of winner

from random import randint

def gamestatus(gamemarks):
    gamemarks_matrix = [["e", "e", "e"],
                        ["e", "e", "e"],
                        ["e", "e", "e"]]
    gamemarks_for = ["O", "X"] 

    for board_num, board_mark in gamemarks.items():
        if board_num == 1: gamemarks_matrix[0][0] = board_mark
        elif board_num == 2: gamemarks_matrix[0][1] = board_mark
        elif board_num == 3: gamemarks_matrix[0][2] = board_mark
        elif board_num == 4: gamemarks_matrix[1][0] = board_mark
        elif board_num == 5: gamemarks_matrix[1][1] = board_mark
        elif board_num == 6: gamemarks_matrix[1][2] = board_mark
        elif board_num == 7: gamemarks_matrix[2][0] = board_mark
        elif board_num == 8: gamemarks_matrix[2][1] = board_mark
        elif board_num == 9: gamemarks_matrix[2][2] = board_mark
    
    for i in range(2):
        if gamemarks_matrix[0][0] == gamemarks_for[i] and gamemarks_matrix[0][1] == gamemarks_for[i] and gamemarks_matrix[0][2] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[1][0] == gamemarks_for[i] and gamemarks_matrix[1][1] == gamemarks_for[i] and gamemarks_matrix[1][2] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[2][0] == gamemarks_for[i] and gamemarks_matrix[2][1] == gamemarks_for[i] and gamemarks_matrix[2][2] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[0][0] == gamemarks_for[i] and gamemarks_matrix[1][0] == gamemarks_for[i] and gamemarks_matrix[2][0] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[0][1] == gamemarks_for[i] and gamemarks_matrix[1][1] == gamemarks_for[i] and gamemarks_matrix[2][1] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[0][2] == gamemarks_for[i] and gamemarks_matrix[1][2] == gamemarks_for[i] and gamemarks_matrix[2][2] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[0][0] == gamemarks_for[i] and gamemarks_matrix[1][1] == gamemarks_for[i] and gamemarks_matrix[2][2] == gamemarks_for[i]: return(False, gamemarks_for[i])
        if gamemarks_matrix[0][2] == gamemarks_for[i] and gamemarks_matrix[1][1] == gamemarks_for[i] and gamemarks_matrix[2][0] == gamemarks_for[i]: return(False, gamemarks_for[i])

    return(True,"")

# gives the total running time of the program
def timeplay(start_time, end_time, total):
    time = end_time - start_time
    minutes = time // 60
    seconds = time - 60*minutes
    if total:
        if minutes == 0:print(f"Total running time was: {round(seconds)} s.".center(40))
        else:print(f"Total running time was: {round(minutes)}:{round(seconds)}".center(40))
    else:
        if minutes == 0:print(f"Game running time was: {round(seconds)} s.".center(40))
        else:print(f"Game running time was: {round(minutes)}:{round(seconds)}".center(40))
                            
# gives rundom number acording to conditions in list 
def give_random_number():
    random_number = []
    random_number.append(randint(1,9))
    while len(random_number) != 4: 
         if (num_temp := randint(0,9)) not in random_number: random_number.append(num_temp)
    return(random_number)

# decides if input is good and returns empty string or if is bad returns error phrase 
def check_number(players_number):
    try:
        int(players_number)
    except:
        return "Your input is not number"
    if len(players_number) < 4 : return "Your number is too small."
    if len(players_number) > 4 : return "Your number is too big"
    players_number = [int(num) for num in players_number]
    if players_number[0] == 0 : return "0 cannot be the first number."
    if len(set(players_number)) != 4: return "Every number must be unique"
    return ""

# returns the number of bulls and cows in the player's number           
def bacevaluation(guessed_number, players_number):
    cows = 0
    bulls = 0
    for num in guessed_number: 
        if num in players_number: cows += 1
    for index in range(4):
        if guessed_number[index] == players_number[index]: bulls += 1
    cows = cows - bulls
    return(cows, bulls)

# according to how many B & C gives right phrase
def bacverdict(cows, bulls):
    if cows == 1:
        if bulls == 1: print("1 bull, 1 cow")
        else: print(f"{bulls} bulls, 1 cow")
    if bulls == 1 and cows != 1: print(f"1 bull, {cows} cows")
    if bulls == 4: print("Correct, you've guessed the right number.")
    if bulls != 1 and cows != 1 and bulls != 4: print(f"{bulls} bulls, {cows} cows")

# gives feedback to player according to number of attempts
def bacfeedback(attempts):
    if attempts == 1: print("You are lucky. I took you only 1 attemp.")
    else: print(f"I took you {attempts} attempts.",end=" ")
    if attempts <= 4 and attempts > 1: print("That's amazing.")
    if attempts <= 9 and attempts > 4: print("That's average.")
    if attempts >9: print("That's not so good")
                                              
                                              



    