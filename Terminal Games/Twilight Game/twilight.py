#twilight.py
#Includes the modules "vampire" and "werewolf" and simulates a battle.
#Ryan LaRouche

import vampire
import werewolf
import random

def results(name): #print results
    print("\n\n============================== Results ===============================")
    print(name, "win!")
    print("======================================================================")

def fight(vamps, wolves, vamp_names, wolf_names):
    import random
    if (len(vamps) != 0) and (len(wolves) != 0):
        chosen_vamp = random.choice(vamps)
        chosen_wolf = random.choice(wolves)
        number = vamps.index(chosen_vamp)
        vamp_name = vamp_names[number]
        number = wolves.index(chosen_wolf)
        wolf_name = wolf_names[number]
        move = random.randint(0,1) #Decide who attacks first and second
        if (move == 0):
            team1 = vamps
            name1 = vamp_names
            team2 = wolves
            name2 = wolf_names
            actions(chosen_vamp, chosen_wolf, vamp_name, wolf_name, team1, team2,
                    name1, name2, vamps, wolves, vamp_names, wolf_names) 
        elif (move == 1):
            team1 = wolves
            name1 = wolf_names
            team2 = vamps
            name2 = vamp_names
            actions(chosen_wolf, chosen_vamp, wolf_name, vamp_name, team1, team2,
                    name1, name2, vamps, wolves, vamp_names, wolf_names)
def actions(turn1, turn2, turn1_name, turn2_name, team1, team2, name1, name2,
            vamps, wolves, vamp_names, wolf_names):
    print("============================== Actions ===============================")
    try:
        outcome  = turn1.bite(turn1_name, turn2_name, turn2)
    except:
        outcome  = turn1.attack(turn1_name, turn2_name, turn2) 
    if (outcome == 0):
        team2.remove(turn2)
        name2.remove(turn2_name)
    elif (outcome == 2):
        team1.remove(turn1)
        name1.remove(turn1_name)
    print("======================================================================")
    if (len(vamps) != 0) and (len(wolves) != 0):
        name_list(vamps, wolves)
        fight(vamps, wolves, vamp_names, wolf_names)
    elif (len(vamps) == 0):
        results("The Wolves")
    elif (len(wolves) == 0):
        results("The Vampires")

def name_list(vamps, wolves):
    print("\n\n=========== Vampire(s) ===========\t======== Werewolve(s) ========")
    names = []
    count = -1
    for name in range (0,3):
        count += 1
        try:
            names.append(vamps[name])
        except IndexError:
            names.append("\t\t\t\t")
        try:
            names.append(wolves[name])
        except IndexError:
            names.append("\t\t\t")
    for name in range (0,6,2):
        if ((len(str(names[name])) >= 10) and (len(str(names[name + 1])) >= 10)):
            print(str(names[name]) + "\t" + str(names[name + 1]))
    print("\n==================================\t==============================")

def main():
    global vamp
    global wolf
    vamp_names = ["Edward", "Emmett", "Alice"]
    wolf_names = ["Jacob", "Sam", "Leah"]
    vamps = []
    wolves = []
    vamp1 = vampire.Vampire(vamp_names[0]) #New vampires
    vamps.append(vamp1)
    vamp2 = vampire.Vampire(vamp_names[1])
    vamps.append(vamp2)
    vamp3 = vampire.Vampire(vamp_names[2])
    vamps.append(vamp3)
    wolf1 = werewolf.Werewolf(wolf_names[0]) #New werewolves
    wolves.append(wolf1)
    wolf2 = werewolf.Werewolf(wolf_names[1])
    wolves.append(wolf2)
    wolf3 = werewolf.Werewolf(wolf_names[2])
    wolves.append(wolf3)

    print("============================= Instructions ===========================")
    print("1. A set of vampires and werewolves is generated randomly.\n\
2. Each starts out with 5 power.\n\
 \t- Power is indicated by the number in the '()'\n\
 next to each topponent's name.\n\
 \t- If either opponent's power reaches 0, they die.\n\
 \t- An opponent can have a maximum of 5 power.\n\
3. Each fights the other group (1v1) and the first\n\
attacker is chosen randomly.\n\
4. Their move has two possible results:\n\
 \t- Successful: The target dies. Attacker gains 1 \n\
 power if their power less than 5.\n\
 \t- Unsuccessful: The attacker loses 1 power.\n\
6. The last opponent alive wins.")
    print("======================================================================")
    name_list(vamps, wolves)
    fight(vamps, wolves, vamp_names, wolf_names)

main()
