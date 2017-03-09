#tictactoe.py
#Generate a tictactoe board game and play against a random computer
#User inputs move, then randomly pick a computer move, if one of the player
#wins, print win, if tie, print tie, if not, reloop until win.
#Ryan LaRouche

board = ("\t| - | - | - |\n\t| - | - | - |\n\t| - | - | - |")
playersign = "X"
computersign = "O"
takenmoves = []
gameinprogress = True
import random

def initGame():
    global board
    print("Welcome to Tic-Tac-Toe - Celebrity Edition TM\n") #instructions
    print(" Here are some basic rules you should understand:\n\
    1. The board has 9 positions. (See below)\n\
    2. Enter a position 1-9 based on the grid below to choose your move.\n\
    3. A random celebrity [the computer] will then choose a move against you.\n\
    4. If you get three-in-a-row you win.\n\
          ** But be careful: if the computer does, you lose.\n\
    5. If the board fills up and there is no winner, the game ends in a tie.\n\n\
    User symbol is :", playersign, " \n\
    Computer Symbol:", computersign, " \n\n\
        === BOARD ===")
    boardlist = list(board)
    location = 1
    for dash in range(len(boardlist)):
        if (location != 10):
            if (boardlist[dash]== "-"):
                boardlist[dash] = (str(location))
                location += 1
    sampleboard = ''.join(boardlist)
    print(sampleboard)
    print("\t=============\n")
    print("    Good luck and have fun!")


def printBoard(movelocation, movestyle,currentplayer):
    global board
    global takenmoves
    location = 0
    boardlist = list(board)
    for dash in range(len(boardlist)): #update position with move
        if (location != 10):
            if boardlist[dash] in ['-', 'X', 'O']:
                location += 1
                if (location == movelocation):
                    boardlist[dash] = (movestyle)
    board = ''.join(boardlist)
    print("\t=============\n", board, "\n\t=============") #print updated board
    check_win(currentplayer)

  
def getPlayerMove():
    global playersign
    validmove = False
    currentplayer = "NA"
    while validmove == False:
        try:
            playermove = input("What is your next move? ") #input
        except:
            print("ERROR: Please enter a valid move that has not been used yet!")
            break
        if (len(playermove) != 0):
            playermove = int(playermove)
            if ((playermove >= 1) and (playermove <= 9)):
                if playermove not in takenmoves:
                    validmove = True
                    break
        print("ERROR: Please enter a valid move that has not been used yet!")
    takenmoves.append(playermove)
    printBoard(playermove, playersign, currentplayer) #output to printBoard


def getComputerMove():
    global board
    global computersign
    global takenmoves
    global computermove
    validmove = False
    celebrity = ["George Clooney's", "Brad Pitt's", "Leonardo DiCaprio's", "Justin Bieber(EW)'s", "Your Mom's", "Kim Kardashian's"]
    chosencelebrity = random.choice(list(celebrity))#"input"
    computermove = computerAI()
    print(chosencelebrity, "move is:", computermove, "\n")
    takenmoves.append(computermove)
    printBoard(computermove, computersign, chosencelebrity)#ouput to printBoard

def computerAI():
    global takenmoves
    global board
    global gameinprogress
    computermove = 0
    location = 0
    boardlist = list(board)
    aiboard = check_win("NA") #run to get list of moves without rewriting the code
    gameinprogess = True #undo global changed by check_win()
    for row in range(3):
        for column in range(3):
            location += 1
            if (aiboard[row][column] == "E"):
                aiboard[row][column] = "O" #sim computer move to check for win
                computerwin, playerwin = sim_win(aiboard)
                if computerwin == True:
                    computermove = location
                    return(computermove)
                else:
                    aiboard[row][column] = "E"
            if (aiboard[row][column] == "E"):
                aiboard[row][column] = "X" #sim player move to check for win
                computerwin, playerwin = sim_win(aiboard)
                if playerwin == True:
                    computermove = location
                    return(computermove)
                else:
                    aiboard[row][column] = "E"
    if (computermove == 0):
        validmoves = [1,3,7,9]
        shuffledmoves = random.sample(validmoves, 4)
        for move in shuffledmoves:
            if (computermove == 0):
                if (move not in takenmoves): #corners
                    computermove = move
                    return(computermove)
        if ((move in [5]) and (move not in takenmoves) and (computermove == 0)): #center
                computermove = move
                return(computermove)
        validmoves = [2,4,6,8]
        shuffledmoves = random.sample(validmoves, 4)
        for moves in shuffledmoves:
            if (computermove == 0):
                if ((move in [2,4,6,8]) and (move not in takenmoves)): #sides
                    computermove = move
                    return(computermove)

def sim_win(move):
    computerwin = False
    playerwin = False
    for rows in range(3):
        if (move[rows][0] == move[rows][1]) and (move[rows][1] == move[rows][2]): #rows check
            if (move[rows][0] != "E"):
                if (move[rows][0] == "X"):
                    playerwin = True
                if (move[rows][0] == "O"):
                    computerwin = True
    for column in range(3):
        if (move[0][column] == move[1][column]) and (move[1][column] == move[2][column]): #colums check
            if (move[0][column] != "E"):
                if (move[0][column] == "X"):
                    playerwin = True
                if (move[0][column] == "O"):
                    computerwin = True
    if (move[0][0] != "E"):
        if ((move[0][0] == move[1][1]) and (move[0][0] == move[2][2])): #diagonal check
                if (move[0][0] == "X"):
                    playerwin = True
                if (move[0][0] == "O"):
                    computerwin = True
    if (move[2][0] != "E"):
        if ((move[2][0] == move[1][1]) and (move[2][0] == move[0][2])): #diagonal check
                if (move[2][0] == "X"):
                    playerwin = True
                if (move[2][0] == "O"):
                    computerwin = True
    return(computerwin, playerwin)

def check_win(currentplayer):
    global board
    global gameinprogress
    location = 0
    move = []
    playerwin = False
    computerwin = False
    emptyspaces = 0
    boardlist = list(board)
    for row in range(3):
        move.append([])
        for dash in range(14):
                    if (boardlist[location] == "-"):
                        move[row].append("E")
                        emptyspaces += 1
                    elif (boardlist[location] == "X"):
                        move[row].append("X")
                    elif (boardlist[location] == "O"):
                        move[row].append("O")
                    location += 1
    for rows in range(3):
        if (move[rows][0] == move[rows][1]) and (move[rows][1] == move[rows][2]): #rows check
            if (move[rows][0] != "E"):
                if (move[rows][0] == "X"):
                    playerwin = True
                if (move[rows][0] == "O"):
                    computerwin = True
    for column in range(3):
        if (move[0][column] == move[1][column]) and (move[1][column] == move[2][column]): #colums check
            if (move[0][column] != "E"):
                if (move[0][column] == "X"):
                    playerwin = True
                if (move[0][column] == "O"):
                    computerwin = True
    if (move[0][0] != "E"):
        if ((move[0][0] == move[1][1]) and (move[0][0] == move[2][2])): #diagonal check
                if (move[0][0] == "X"):
                    playerwin = True
                if (move[0][0] == "O"):
                    computerwin = True
    if (move[2][0] != "E"):
        if ((move[2][0] == move[1][1]) and (move[2][0] == move[0][2])): #diagonal check
                if (move[2][0] == "X"):
                    playerwin = True
                if (move[2][0] == "O"):
                    computerwin = True
    if playerwin == True:
        print("Congrats! You win!")
        gameinprogress = False
    elif computerwin == True:
        print("Sorry, but", currentplayer, "move won him/her the game.")
        gameinprogress = False
    elif emptyspaces == 0:
        print("No available spaces: The game ends in a tie!")
        gameinprogress = False
    return(move)


        
def playAgain():
    global gameinprogress
    global board
    global takenmoves
    while True:
        try:
            answer = input("Would you like to play again? ('Y' for Yes / 'N' for No) ")
        except:
            print("ERROR: Please answer 'Y' or 'N'")
            continue
        if ((len(answer)) != 0):
            if answer in ['Y', 'y', 'N', 'n']:
                if answer in ['Y', 'y']:
                    gameinprogress = True
                    board = ("\t| - | - | - |\n\t| - | - | - |\n\t| - | - | - |")
                    print("\t=============\n", board, "\n\t=============")
                    takenmoves = []
                    playGame()
                else:
                    break
        else:
            print("ERROR: Please answer 'Y' or 'N'")
            continue
                
def playGame():
    turn = 1
    global gameinprogress
    while gameinprogress == True: #loop to cycle turns until game ends
        print("Turn:", turn)
        turn += 1
        getPlayerMove()
        getComputerMove()
    playAgain()

def main():
    initGame()
    playGame()
    
    print("END OF GAME! THANKS FOR PLAYING")
    
main()
