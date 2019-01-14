import sys
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

print(bcolors.INFO+"Loading JSON file in..."+bcolors.RESET)

print(bcolors.INFO + "Loading in the game data..."+bcolors.RESET)
with open('game_data.json') as data_file:
    data = json.load(data_file)

playerHealth=data["player"]["health"]
playerGold=data["player"]["gold"]
print(bcolors.INFO + "Beginning the game..." + bcolors.RESET)

currentPath = None

def printOutStatus():
    print("")
    print(bcolors.RED + "Health: "+str(playerHealth)+bcolors.RESET+","+bcolors.YELLOW+"Current Gold: " +str(playerGold)+bcolors.RESET)

def setPath(numb):
    for idx, val in enumerate(data["paths"]):
        if val["id"]==numb:
            global currentPath
            currentPath = val

# Start of the program below
# vvvvvvvvvvvvvvvvvvvvvvvvvv

setPath(data["game"]["start"])

while True:
    printOutStatus()
    print(currentPath["text"])
    for i,opts in enumerate(currentPath["options"]):
        sys.stdout.write("%s. %s        " %(i,opts["choice"]))
    print("")
    sel = input("What do you choose?")
    setPath(currentPath["options"][sel]["goto"])
