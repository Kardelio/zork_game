import sys
import os
import time
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    RED = '\033[91m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INFO = '\033[96m'
    YELLOW = '\033[93m'
    STANDARD = '\033[97m'
    OPTION = '\033[30;47m'

INCREASE_HEALTH = "health + 1"
DECREASE_HEALTH = "health - 1 "


print(bcolors.INFO+"Loading JSON file in..."+bcolors.RESET)

print(bcolors.INFO + "Loading in the game data..."+bcolors.RESET)
with open('game_data.json') as data_file:
    data = json.load(data_file)

playerHealth=data["player"]["health"]
playerGold=data["player"]["gold"]
print(bcolors.INFO + "Beginning the game..." + bcolors.RESET)
time.sleep(1)
os.system("clear")
currentPath = None

def printOutStatus():
    print("")
    print(bcolors.RED + "Health: "+str(playerHealth)+bcolors.RESET+","+bcolors.YELLOW+"Current Gold: " +str(playerGold)+bcolors.RESET)

def setPath(numb):
    for idx, val in enumerate(data["paths"]):
        if val["id"] == numb:
            global currentPath
            currentPath = val
            if "effect" in currentPath:
#                print(currentPath["effect"]["status"])
                print(currentPath["effect"]["consequence"])
                print(currentPath["effect"]["text"])
                out = currentPath["effect"]["consequence"]
                global playerHealth
                if out == INCREASE_HEALTH:
                    playerHealth += 1
                    printOutStatus()
                elif out == DECREASE_HEALTH:
                    playerHealth -= 1
                    printOutStatus()
                else:
                    print("Unknown Conseq")

# Start of the program below
# vvvvvvvvvvvvvvvvvvvvvvvvvv

setPath(data["game"]["start"])

while True:
    print(currentPath["text"])
    print("")
    time.sleep(1)
    for i,opts in enumerate(currentPath["options"]):
       print(bcolors.OPTION+""+str(i)+". "+opts["choice"]+""+bcolors.RESET+"        ", end ="")
    print("")
    sel = input(bcolors.STANDARD + "What do you choose?"+bcolors.RESET)
    #TODO validate input 
    setPath(currentPath["options"][int(sel)]["goto"])
    print("")
#    os.system("clear")
    time.sleep(1)
