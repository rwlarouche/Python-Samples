#guess_number.py
#Generates a random number in the range of 1 through 100 and asks the user to
#guess what that number is
#Ryan LaRouche

number = 0
lower = 1
upper = 100
import random

def printInfo():
    print("=============== GUESS-O-MATIC ===============\nInstructions: \n 1.\
) The computer will generate a random numer 1-100 \n 2.) When prompted, enter\
a number from 1-100 \n 3.) The computer will tell you if you are too high or \
too low \n 4.) Guess accordingly until you guess the correct number\nGood \
luck!\n=============================================\n") #instructions

def generateNumber():
    global number
    global lower
    global upper
    number = random.randint(1,100)#generate a random number as a global
    
def getGuess():
    global number
    global lower
    global upper
    validguess = False
    while validguess == False:
        try:
            print("The range is:", lower, "-", upper)
            guess = eval(input("Pick a number: ")) #guess
        except:
            print("ERROR: Please input a valid guess/number!")
            continue
        break
    if (guess != number):
        if (guess > number):
            upper = (guess - 1)
            print("Too high, try again.")
        if (guess < number):
            lower = (guess + 1)
            print("Too low, try again.")
        return(0) #wrong number returns 0
    else:
        print("Correct! The chosen number was", number,"!")
        return(1) #correct number returns 1
    
def playGame():
    correct = 0
    generateNumber()
    while (correct != 1):
        getGuess()
        correct = getGuess()
        if (correct == 1):
            break
    
def main():
    printInfo()
    playGame()

main()
