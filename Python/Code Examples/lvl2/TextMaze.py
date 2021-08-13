# TextMaze.py
__author__ = "Josh Smith"
# v. 0.0.1

# Import necessary libraries
import random
import time

# Declare necessary variables (2-dimensional array)
maze = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", "X", "X", "#", "X", "X", "X", "X", "X", "#", "#"],
    ["#", "#", "#", "X", "#", "X", "#", "#", "#", "X", "#", "#"],
    ["#", "X", "X", "X", "X", "X", "X", "X", "#", "X", "#", "#"],
    ["#", "X", "#", "#", "#", "#", "#", "X", "#", "#", "#", "#"],
    ["#", "X", "#", "#", "#", "X", "#", "X", "X", "X", "#", "#"],
    ["#", "X", "#", "#", "#", "X", "#", "X", "#", "#", "#", "#"],
    ["#", "X", "X", "X", "#", "X", "#", "X", "#", "#", "#", "#"],
    ["#", "#", "#", "X", "#", "X", "#", "X", "X", "X", "X", "#"],
    ["#", "X", "#", "X", "#", "X", "#", "X", "#", "#", "X", "#"],
    ["#", "X", "X", "X", "X", "X", "#", "X", "#", "#", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]

location = { "x": 0, "y": 0 }

# Run every time the player moves:
def frame():
    layerNumber = 0
    for i in maze:
        
        a = i[:] # Clones array so that map does not permanantely keep the tile as "O"
        if layerNumber == location["y"]:
            a[location["x"]] = "O"
        
        print(" ".join(a))
        layerNumber += 1
    
    print("Where do you go next?")
    direction = input("up/down/left/right > ")
    
    movePlayer(direction)
    
    if maze[location["y"]][location["x"]] == "E":
        print("Congratulations! You finished the maze.")
    else:
        frame()

def movePlayer(direction):
    
    if direction == "up" and maze[location["y"] - 1][location["x"]] != "#":
        location["y"] -= 1
    elif direction == "down" and maze[location["y"] + 1][location["x"]] != "#":
        location["y"] += 1
    elif direction == "left" and maze[location["y"]][location["x"] - 1] != "#":
        location["x"] -= 1
    elif direction == "right" and maze[location["y"]][location["x"] + 1] != "#":
        location["x"] += 1
    else:
        print("You cannot move in that direction!")

# Setup Game:
def startGame():
    # Find the starting location (marked "S" on the map)
    levelY = 0
    levelX = 0
    
    for i in maze:
        
        for j in i:
            
            if j == "S":
                location["x"] = levelX
                location["y"] = levelY
                
            levelX += 1
        
        levelY += 1
        levelX = 0
    
    frame()

startGame()