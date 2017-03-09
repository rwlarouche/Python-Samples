#rolling_dice
#Dice rolling game where two dice are rolled and the sum determines winning or
#losing (see instructions)
#Ryan LaRouche

point = 0
numberofgames = 0
turns = 0
import random

def printInfo(): #instructions
        print("=============== MAKE-OR-BREAK-DICE ===============\nInstructio\
ns: \n 1.) You will be prompted to roll two dice. \n 2.) Follow the rules in th\
table below::\nTurn\tRoll Value\tOutcome\n 1\t 7\t\t Win\n 1\t 2,3,or 12\t Lose\
\n 1\t 4,5,6,8,9,10\t *Value Becomes Your 'Point'\n +1\t 7\t\t Lose\n +1\t = 'P\
oint'\t Win\n +1\t != 'Point'\t Continue Rolling\n**Your 'Point' is the saved\
value you must roll in order to win\n  It equals the value of your first roll\
\n\nGoodluck!\n==================================================\n")

def getGames():
    global numberofgames
    while True:
        try:
            numberofgames = eval(input("How many games would you like to simulate: "))
        except:
            print("ERROR: Please enter a valid positive integer greater than 0!")
            continue
        if (numberofgames > 0):
            break
        else:
            continue

def rollDice(gamenumber):
    global point
    global turns
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    point = (die1 + die2)
    turns += 1
    print("== Roll 1 ==")
    print("Die\tValue\n 1\t", die1, "\n 2\t", die2, "\nRoll Value:", (die1 + die2), "\nPoint Value:", point, "\nCurrent Win Probability:", str((round((gamenumber/turns),3)*100)), "%\n============")
    return(die1, die2)

def rollPoint(gamenumber):
    global point
    global numberofgames
    global turns
    turn = 1
    gamenumber = 1
    keeprolling = True
    die1, die2 = rollDice(gamenumber)
    if ((die1 + die2) == 7):
        print("Congrats, you rolled 7 on your first roll and won!")
        keeprolling = False
    while keeprolling == True:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        turn += 1
        turns +=1
        print("== Roll", turn, "==")
        print("Die\tValue\n 1\t", die1, "\n 2\t", die2, "\nRoll Value:", (die1 + die2), "\nPoint Value:", point, "\nCurrent Win Probability:", str((round((gamenumber/turns)*100,2))) + "%\n============")
        rollvalue = (die1 + die2)
        if (rollvalue == 7):
            print("Sorry, you lose!\n\n")
            break
        if (rollvalue == point):
            print("Congrats, you rolled your 'point' value and won!\n\n")
            break

def playGame():
    global numberofgames
    gamenumber = 1
    endsim = False
    getGames()
    while endsim == False:
        print("-- Game", gamenumber, "--")
        rollPoint(gamenumber)
        gamenumber += 1
        print(turns)
        print(gamenumber)
        if (gamenumber == (numberofgames+1)):
            endsim = True
    
def main():
    printInfo()
    playGame()

main()
