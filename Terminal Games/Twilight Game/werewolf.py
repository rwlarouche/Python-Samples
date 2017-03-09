#werewolf.py
#Includes a general description of all werewolf (name and power), and includes
# 2 'actions' - bite and die
#Ryan LaRouche

class Werewolf():
    def __init__(self, name):
        self.__name = name.capitalize()
        self.__power = 5
        self.__anger = "angry"

    def __str__(self):
        printout = self.__name + "  Power: " + str(self.__power) + "  Anger: " + self.__anger
        return(printout)

    def attack(self, werewolf_name, vampire_name, vampire):
        import random
        outcome = -1
        success = random.randint(0,1)
        print(werewolf_name, "will attack", vampire_name + "!")
        if (success == 0):
            print(self.__name + "(" + str(self.__power) + ")" + "'s attack is successful.")
            if (self.__anger == "angry"):
                vampire.die()
                self.__anger = "calm"
                outcome = 0
            elif (self.__anger == "calm"):
                result = vampire.decrement_power()
                if (result == "dead"):
                    outcome = 0
                else:
                    outcome = 1
            if (self.__power != 5):
                self.__power += 1
            return(outcome)
        if (success == 1):
            if (self.__power != 0):
                self.__power -= 1
                print(self.__name + "(" + str(self.__power) + ")" + "'s attack is unsuccessful.\n")
                outcome = 1
            if (self.__power == 0):
                die()
                outcome = 2
            return(outcome)
        
    def decrement_power(self):
        self.__power -= 1
        if (self.__power == 0):
            die()
        return("dead")
    
    def die(self):
        self.__power = 0
        print(self.__name + "(" + str(self.__power) + ")" + "dies!")
