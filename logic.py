# rewrites gamemarks to matrix and then decides if there are any "3 in row".
# if there are "3 in row" returns True value and mark of winner
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



        
        