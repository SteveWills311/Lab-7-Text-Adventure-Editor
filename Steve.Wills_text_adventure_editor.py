#Steve Wills
#Text Adventure Editor
#10/4/24

import json

def main():
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            print("quitter...")
            keepGoing = False
        elif menuChoice == "1":
            print("Load Default Game")
            game = getDefaultGame()
        elif menuChoice == "2":
            print("Load Game File")
            game = loadGame()
        elif menuChoice == "3":
            print("Saved it!")
            saveGame(game)
        elif menuChoice == "4":
            print("Edit/Add a node")
            game = editNode(game)
        elif menuChoice == "5":
            print("Let's Go! Beginning Game!")
            playGame(game)
        else:
            print("And... you broke it... pick 0-5 please.")
            
def getMenuChoice():
    keepGoing = True
    while keepGoing:
        print(""" 
            0. Exit
            1. Load default game
            2. Load game file
            3. Save current game
            4. Edit or add node
            5. Play current game
            """)
        menuChoice = input("What'll it be? ")
        if menuChoice in ("0", "1", "2", "3", "4", "5"):
            keepGoing = False
        else:
            print("you broke it! 0-5 please.")
    return menuChoice

def playGame(game):
    currentGame = "start"
    keepGoing = True
    while keepGoing:
        currentGame = playNode(game, currentGame)
        if currentGame == "quit":
            keepGoing = False

def playNode(game, currentGame):
    (description, menuA, nodeA, menuB, nodeB) = game[currentGame]
    keepGoing = True
    while keepGoing:
        print(f"""
        {description}
        1. {menuA}
        2. {menuB}
        """)
        choice = input("What'll it be?!")
        if choice == "1":
            nextNode = nodeA
            keepGoing = False
        elif choice == "2":
            nextNode = nodeB
            keepGoing = False
        #else:
        #    print("ah ah ah! you didnt say the magic word! 'you know... Jurassic park...'")
        return nextNode
    
def getDefaultGame():
    game = {"start": ["Start or Quit? Thought there was more, eh?!", "Start over", "start", "Quit", "quit"]}
    return game

def editNode(game):
    print("These are the current nodes...")
    print(json.dumps(game, indent = 2))
    for nodeName in game.keys():
        print(f"{nodeName}")
    newNodeName = input("Input a new name, if it already exists, it will not be made again. ")
    if newNodeName in game.keys():
        newNode = game[newNodeName]
    else:
        newNode = ["", "", "", "", ""]
    (description, menuA, nodeA, menuB, nodeB) = newNode
    newDescription = editField("description", description)
    newMenuA = editField("Menu A", menuA)
    newNodeA = editField("Node A", nodeA)
    newMenuB = editField("Menu B", menuB)
    newNodeB = editField("Node B", nodeB)
    game[newNodeName] = {newDescription, newMenuA, newNodeA, newMenuB, newNodeB}
    return game

def editField(prompt, currentValue):
    newValue = input(f"{prompt} ({currentValue}): ")
    if newValue == "":
        newValue = currentValue
    return newValue

def saveGame(game):
    outFile = open("game.json", "w")
    json.dump(game, outFile, indent = 2)
    print(json.dumps(currentGame, indent = 2))
    outFile.close()
       
    
def loadGame(game):
    inFile = open("game.json", "r")
    game = json.load(inFile)
    print(game)
    inFile.close()
    return game

main()