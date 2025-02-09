import time
from UsefulStuff import clearScreen
from UsefulStuff import Red, reset, yellow, Blue
import inspect
# Press enter to continue
def PETC_function(): 
    input(yellow + "\n(Press Enter to Continue)\n" + reset)
    clearScreen()
# Press a number to continue
def PNTC_function(): 
    print(yellow + "\n(Press a number and then Enter to choose)" + reset)
# Press a number to continue, but with a quit option.

# Invalid Input detected, 
def InvalidInput(IS="You must press the number on the left. \nThen, you press enter to choose."):
    clearScreen()
    print(Red + "Invalid Input" + reset)
    time.sleep(1)
    print(IS) # Custom input
    PETC_function()

# Yes or no.
def YesOrNo():
    time.sleep(0.5)
    print("\n 1 - "+Blue+"Yes"+reset)
    time.sleep(0.25)
    print("\n 2 - "+Red+"No"+reset)
    time.sleep(0.25)
    PNTC_function()
    try:
        YONChoice = int(input(""))
        if YONChoice not in range (1,3):
            return Exception
        else:
            return YONChoice
    except:
       return Exception
    
def Quitmoment(OGFile="N/A"):
    while True:
        print("Are you sure you want to "+Red+"quit"+reset+"?")
        try:
            YON = YesOrNo()
        except: 
            InvalidInput()
            continue
        if YON == 1:
            if "MenuScreen" in OGFile: # If the function was called from MenuScreen.py
                return "Quit" # Get on with it
            print("Understood.")
            time.sleep(1)
            print("\n You will now return to the menu screen.")
            time.sleep(2)
            return "Quit"
        if YON == 2:
            print("\n Alrighty then!")
            time.sleep(1)
            return "Redo"
        
def NumChoiceWithQuit(): 
    print(yellow + "\n(Press a number and then Enter to choose. "+reset+Red+"Press 0 to "+reset+Red+"quit."+reset+yellow+")"+reset)
    frame = inspect.currentframe().f_back
    FileThatCalledFunction = frame.f_code.co_filename
    while True:
        try:
            NumberChoice = int(input(""))
        except:
            return Exception
        if NumberChoice == 0:
            QuitChoice = Quitmoment(FileThatCalledFunction)
            if QuitChoice == "Continue":
                return "Redo"
            else:
                return "Quit"
        else:
            return NumberChoice

# Explains the game
def explainGame():
    clearScreen()
    print('''Once again, it is the game of luck and strategy, \nso you win THROUGH luck and strategy.''')
    PETC_function()
    print('''It is not just one game we are talking here. It is multiple.''')
    PETC_function()
    print('''These games are such as Tic-Tac-Toe,\nRock Paper Scissors,\nand Four Corners.''')
    PETC_function()
    print('''You will most likely be prompted to type in a certain number in the games.
This is in order for you to make a move on that game.
For example,\nYou must type in 1 in order to fill the top-left spot on Tic Tac Toe''')
    PETC_function()
    print('''There are two modes to this game:\n"Player vs Computer" and "Player vs Player"''')
    PETC_function()
    print('''When you choose "Player vs Computer",
Your goal is to get the highest score that you can get in 7 games.
You gain points by winning/getting close to winning games on this mode''')
    PETC_function()
    print('''When you choose "Player vs Player",
Your goal is the same as "Player vs Computer" except for a few things.
You must have a higher score than your opponent to win!
You gain points on this mode by winning games against your opponent
OR by having a bigger lead than your opponent on certain games.''')
    PETC_function()
        
####################################
#### GAME EXPLANATIONS
####################################

def RPSExplanation():
    clearScreen()
    print('''1 - You choose rock, paper, or scissors to be your weapon.''') 
    PETC_function()
    print('''2 - Your opponent will do the same and you both will clash''')
    PETC_function()
    print('''3 - Rock beats scissors,\npaper beats rock,\nand scissors beats paper.''')
    PETC_function()
    print('''4 - If you and your opponent choose the same weapon,\nthen the clash will be a draw.''')
    PETC_function()
    print('''5 - Whenever you win a clash, you gain a point ''')
    PETC_function()
    print('''6 - Whoever gets 3 points between you and your opponent will win!''')
    PETC_function()

def FourCornersExplanation():
    clearScreen()
    print('''1 - It's like tic-tac-toe, but it's not tic-tac-toe.''') 
    PETC_function()
    print('''2 - There are 6 rows and 7 columns. Each turn, you fill and mark a row in a column.''')
    PETC_function()
    print('''3 - The location that you mark depends on how many rows are filled in that column.''')
    PETC_function()
    print('''4 - You have to get four marks either horizontal or vertical in order to win a point''')
    PETC_function()
    print('''5 - Your opponent can block you from getting four marks vertically or horizontally, but you can bypass that somehow.''')
    PETC_function()
    print('''6 - First player to obtain 2 points will win the game of Connect FOUR''')
    PETC_function()
    print('''7 - If you have a strategy for Connect FOUR, now is the best time to use it.''')
    PETC_function()

def GuessTheNumberExplanation():
    print('''1 - A random number is generated by the system.''') 
    PETC_function()
    print('''2 - You and your opponent has the goal of guessing that number.''')
    PETC_function()
    print('''3 - When you guess the number correctly, you get a point.''')
    PETC_function()
    print('''4 - When you guess the number incorrectly but almost correctly,
    You get half a point''')
    PETC_function()
    print('''5 - You and your opponent also has a goal of getting 3 points.''')
    PETC_function()
    print('''6 - If you both manage to get 3 points, there will be a tiebreaker.
    In the tiebreaker, There is no getting half a point.
    You and your opponent will instead have to guess the number correctly
    The range of numbers generated is smaller in the tiebreaker.''')
    PETC_function()
    print('''7 - If you and your oppponent guess the correct number,
    You both get a point, unless it is a tiebreaker.
    if ''')
    PETC_function()


def ExplanationSuggestion(GameExplained):
    Explained = False
    clearScreen()
    while True:
        if Explained == False:
            print('''Would you like an explanation on this game?''')
        elif Explained == True:
            print('''Would you like another explanation on this game?''')
        YesOrNo()
        try:
            Explanationchoice = int(input(""))
        except:
            InvalidInput()
            continue
        if Explanationchoice == 1:
            print("Alright, allow me to explain the game for you.")
            time.sleep(2)
            if GameExplained == "RPS":
                RPSExplanation()
            elif GameExplained == "4C":
                FourCornersExplanation()
            elif GameExplained == "GTN":
                GuessTheNumberExplanation()
            Explained = True
            continue
        elif Explanationchoice == 2:
            print("Alright, GOOD LUCK!")
            time.sleep(1.5)
            clearScreen()
            break
        else:
            InvalidInput()