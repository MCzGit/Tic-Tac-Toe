#Tic-Tac-Toe

import random

def createBoard(board):
    #Fuction created to print out the board.
    #"board" is a list of 10 strings representing the board (ignore index 0).
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def selectPlayerLetter():
    #Allows the player to enter the letter they choose to be.
    #Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('\nDo you want to be X or O?\n')
        letter = input().upper()

    #The first element in the list is the player's letter; followed by the computer's letter
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    

def firstMove():
    #Function created to randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'cpu'
    else:
        return 'player'
    

def executeMove(board, letter, move):
    board[move] = letter


def isWinner(board, letter):
    #With the board and player's letter, the function returns True if the player has won.

    return((board[7] == letter and board[8] == letter and board[9] == letter) or #Top Row
    (board[4] == letter and board[5] == letter and board[6] == letter) or #Middle Row
    (board[1] == letter and board[2] == letter and board[3] == letter) or #Bottom Row
    (board[7] == letter and board[4] == letter and board[1] == letter) or #Down Left Row
    (board[8] == letter and board[5] == letter and board[2] == letter) or #Down Middle Row
    (board[9] == letter and board[6] == letter and board[3] == letter) or #Down Right Row
    (board[7] == letter and board[5] == letter and board[3] == letter) or #Diagonal
    (board[9] == letter and board[5] == letter and board[1] == letter)) #Diagonal


def makeBoardCopy(board):
    #Make a copy of the board list and return it.
    boardCopy = []
    for _ in board:
        boardCopy.append(_)
    return boardCopy


def isSpaceEmpty(board, move):
    #Return True if the requested move is free on the board.
    return board[move] == ' '


def makePlayerMove(board):
    #Allows the player to enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceEmpty(board, int(move)):
        print('\nChoose your next move (1-9)\n')
        move = input()
    return int(move)


def selectRandomMove(board, moveList):
    #Returns a random move from the passed list on the board.
    #Returns none if there is no valid move.
    possibleMoves = []
    for _ in moveList:
        if isSpaceEmpty(board, _):
            possibleMoves.append(_)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    

def makeCPUMove(board, cpuLetter):
    #With the board and the cpu's letter, decide where to move and return that move.
    if cpuLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #AI Algorithm
    #First, check if CPU can win in the next move.
    for _ in range(1, 10):
        boardCopy = makeBoardCopy(board)
        if isSpaceEmpty(boardCopy, _):
            executeMove(boardCopy, cpuLetter, _)
            if isWinner(boardCopy, cpuLetter):
                return _
            
    #Check if the Player can win on the next move and block them.
    for _ in range(1, 10):
        boardCopy = makeBoardCopy(board)
        if isSpaceEmpty(boardCopy, _):
            executeMove(boardCopy, playerLetter, _)
            if isWinner(boardCopy, playerLetter):
                return _
            
    #Attempt to take one of the corners, if they are available.
    move = selectRandomMove(board, [1,3,7,9])
    if move != None:
        return move
    
    #Attempt to take the center, if it is available.
    if isSpaceEmpty(board, 5):
        return 5
    
    #If the corners and center are not available, take one of the sides.
    return selectRandomMove(board, [2,4, 6, 8])


def isBoardFull(board):
    #Return true if every space on the board has been filled.
    for _ in range(1, 10):
        if isSpaceEmpty(board, _):
            return False
    return True


print('\nWelcome to Tic Tac Toe!')

while True:
    #Reset the board
    gameBoard = [' '] * 10

    playerLetter, cpuLetter = selectPlayerLetter()

    turn = firstMove()
    print(f'\nThe {turn} will go first\n')

    game_is_on = True

    while game_is_on:
        if turn == 'player':
            #Player's Turn
            createBoard(gameBoard)
            move = makePlayerMove(gameBoard)
            executeMove(gameBoard, playerLetter, move)

            if isWinner(gameBoard, playerLetter):
                createBoard(gameBoard)
                print('\nCongratulations! You are the winner!\n')
                game_is_on = False
            else:
                if isBoardFull(gameBoard):
                    createBoard(gameBoard)
                    print('\nDeadlocked! The game is a tie!\n')
                    break
                else:
                    turn = 'cpu'

        else:
            #CPU's turn
            move = makeCPUMove(gameBoard, cpuLetter)
            executeMove(gameBoard, cpuLetter, move)

            if isWinner(gameBoard, cpuLetter):
                createBoard(gameBoard)
                print('\nTough Luck! The CPU has won!\n')
                game_is_on = False
            else:
                if isBoardFull(gameBoard):
                    createBoard(gameBoard)
                    print('\nDeadlocked! The game is a tie!\n')
                    break
                else:
                    turn = 'player'


    print('Would you like to play again? (Y or N)\n')
    if not input().lower().startswith('y'):
        break

        





    


    







