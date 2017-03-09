#vampire.py
#Includes a general description of all vampires (name and power), and includes
# 2 'actions' - bite and die
#Ryan LaRouche

class Vampire():
    def __init__(self, name):
        self.__name = name.capitalize()
        self.__power = 5
        self.__hunger = "starving"

    def __str__(self):
        printout = self.__name + "  Power: " + str(self.__power) + "  Hunger: " + self.__hunger
        return(printout)

    def bite(self, vamp_name, werewolf_name, werewolf):
        import random
        outcome = -1
        success = random.randint(0,1)
        print(vamp_name, "will bite", werewolf_name + "!")
        if (success == 0):
            print(self.__name + "(" + str(self.__power) + ")" + "'s bite is successful.")
            if (self.__hunger == "starving"):
                werewolf.die()
                self.__hunger = "full    "
                outcome = 0
            elif (self.__hunger == "full    "):
                result = werewolf.decrement_power()
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
                print(self.__name + "(" + str(self.__power) + ")" + "'s bite is unsuccessful.\n")
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
