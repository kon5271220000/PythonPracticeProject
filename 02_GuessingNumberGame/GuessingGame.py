import random


def StartGame():
    b = input("Start Game (y/n):")
    if b == "y":
        GamePlay()
    else:
        exit()
    
        
def AfterGuessing(playerNum, randomNum):  
    if playerNum == randomNum:
        print("Correct")
        print("you win")
        RestartGame()
    elif(playerNum > randomNum):
        print("Too high")
    else:
        print("Too low")

def RestartGame():
    c = input("Do you want to start again (y/n): ")
    if c == "y":
        GamePlay()
    else:
        exit()

def GamePlay():
    #initial random number for game
    randomNum = random.randrange(1, 100)
    #remaining_time
    remaining_times = 7 #remaning time
    while(True):
        playerNum = input("Enter your number: ").strip()
        if playerNum == "":
            print("you have to guess a number")
            playerNum = input("Enter your number: ")
        playerNum = int(playerNum)
        AfterGuessing(playerNum,randomNum)
        remaining_times -= 1
        print(f"your reamining times: {remaining_times}")
        if remaining_times <= 0:
            print("you loose, better next times")
            RestartGame()

StartGame()