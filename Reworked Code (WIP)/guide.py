from time import sleep
from UsefulStuff import clearScreen
from UsefulStuff import Red, reset, yellow, Blue
import inspect
# Press enter to continue (With Message if there is one)
def MessageStop(Message=""): 
    if Message != "": print(Message)
    input(f"\n{yellow}(Press Enter to Continue){reset}\n")
    clearScreen()

# Press a number to continue
def NumChoice(x,y): 
    NumberChoice = int(input(f"\n{yellow}(Press a number and then Enter to choose){reset}"))
    if NumberChoice in range(x,y): return NumberChoice
    else: raise ValueError("Number not within limit") 

# Invalid Input detected (Usually put this under except:) 
def InvalidInput(IS="You must press the number on the left. \nThen, you press enter to choose."): # Default message
    clearScreen()
    print(f"{Red}Invalid Input{reset}"); sleep(1)
    MessageStop(IS)
    # ALWAYS PUT A CONTINUE AFTER THIS FUNCTION ENDS

# Yes / No | (ALWAYS PUT THIS UNDER try: IN A TRY AND EXCEPT PLS)
# clearScreen before this is optional
def YesOrNo(YNQuestion="\nConfirm?"):
    print(YNQuestion); sleep(0.5)
    print(f"\n 1 - {Blue}Yes{reset}"); sleep(0.25)
    print(f"\n 2 - {Red}No{reset}"); sleep(0.25)
    YONChoice = NumChoice() # An error could occur here (Follow above if u havent)
    if YONChoice not in range(1,3): raise ValueError("not 1 or 2")
    else: return YONChoice


# Press a number to continue, but with a quit option.
def NumChoiceWithQuit(x,y): 
    frame = inspect.currentframe().f_back
    FileThatCalledFunction = frame.f_code.co_filename
    while True:
        NumberChoice = int(input(f"\n{yellow}(Press a number and then Enter to choose. {reset}{Red}Press 0 to {reset}{Red}quit.{reset}{yellow}){reset}\n"))
        if NumberChoice != 0 and NumberChoice in range(x,y): return NumberChoice
        elif NumberChoice == 0: # If we chose to quit
            while True:
                clearScreen()
                try: YON = YesOrNo(f"Are you sure you want to {Red}quit{reset}?")
                except: InvalidInput(); continue
                if YON == 1:
                    # If the function was called from MenuScreen.py
                    if "MenuScreen" in FileThatCalledFunction: return "Quit" # Get on with it
                    else:
                        print("\nUnderstood. You will now return to the menu screen."); sleep(2)
                        return "Quit"
                if YON == 2: print("\n Alrighty then!"); sleep(1); return "Redo"
        else: raise ValueError("Number not within limit") 
        
# Prepare to put something like below after this.
"""
if GameChoice == "Redo": continue
elif GameChoice == "Quit": return
"""
        
####################################
#### GAME EXPLANATIONS
####################################
# Put Numbers before each explanation ty :)
def GameExplanation(GameBeingExplained):
    clearScreen()
    if GameBeingExplained == "Game System":  
        MessageStop("Once again, it is the game of luck and strategy, \nso you win THROUGH luck and strategy.")
        MessageStop("It is not just one game we are talking here. It is multiple.")
        MessageStop("These games are such as Tic-Tac-Toe,\nRock Paper Scissors,\nand Four Corners.")
        MessageStop('''You will most likely be prompted to type in a certain number in the games.
This is in order for you to make a move on that game.
For example,\nYou must type in 1 in order to fill the top-left spot on Tic Tac Toe''')
        MessageStop("There are two modes to this game:\n\"Player vs Computer\" and \"Player vs Player\"")
        MessageStop('''When you choose "Player vs Computer",
Your goal is to get the highest score that you can get in 7 games.
You gain points by winning/getting close to winning games on this mode''')
        MessageStop('''When you choose "Player vs Player",
Your goal is the same as "Player vs Computer" except for a few things.
You must have a higher score than your opponent to win!
You gain points on this mode by winning games against your opponent
OR by having a bigger lead than your opponent on certain games.''')
    elif GameBeingExplained == "RPS":
        MessageStop("1 - You choose rock, paper, or scissors to be your weapon.")
        MessageStop("2 - Your opponent will do the same and you both will clash")
        MessageStop("3 - Rock beats scissors,\npaper beats rock,\nand scissors beats paper.")
        MessageStop("4 - If you and your opponent choose the same weapon,\nthen the clash will be a draw.")
        MessageStop("5 - Whenever you win a clash, you gain a point ")
        MessageStop("6 - Whoever gets 3 points between you and your opponent will win!")
    elif GameBeingExplained == "BG":
        MessageStop("1 - It's a board game. You cross through the trail to win.") 
        MessageStop('''2 - There are 50 tiles on the trail''')
        MessageStop('''3 - You roll an imaginary dice that I made to move
        (You do this by pressing enter)''')
        MessageStop('''4 - Whenever you land on an even tile (tile 92 for example), 
        You are given a chance to test your luck.
        When you take the chance to test your luck,
        you have a chance of getting boosts or traps.
        You will be introduced to that later.''')
        MessageStop('''5 - The farther you go/the more tiles you walk through on the trail,
        the higher the chances of you encountering a trap when testing luck
        However, you can avoid this but not testing your luck.''')
        MessageStop('''6 - While you can play safe by not testing your luck throughout the board game,
        Other players can use weapons against you when having good luck''')
        MessageStop("7 - First player to cross through the entire trail of the board game wins!")
    elif GameBeingExplained == "Connect4":
        MessageStop("1 - It's like tic-tac-toe, but it's not tic-tac-toe.")
        MessageStop("2 - There are 6 rows and 7 columns. Each turn, you fill and mark a row in a column.")
        MessageStop("3 - The location that you mark depends on how many rows are filled in that column.")
        MessageStop("4 - You have to get four marks either horizontal or vertical in order to win a point")
        MessageStop("5 - Your opponent can block you from getting four marks vertically or horizontally, but you can bypass that somehow.")
        MessageStop("6 - First player to obtain 2 points will win the game of Connect FOUR")
        MessageStop("7 - If you have a strategy for Connect FOUR, now is the best time to use it.")
    elif GameBeingExplained == "4C":
        MessageStop("1 - A random color is chosen by the system") 
        MessageStop("2 - There is a list of four colors that will be randomly chosen")
        MessageStop("3 - Those colors are red, green, yellow, and blue.")
        MessageStop("4 - You will also choose the color that you want to pick")
        MessageStop("5 - You have 3 lives in this game.")
        MessageStop('''6 - If the color that you choose gets picked, you lose a life
Once you run out of lives, you lose''')
        MessageStop('''7 - Only a certain amount of players can win.
This depends on difficulty.''')
    elif GameBeingExplained == "TTT":
        MessageStop("1 - On a 3x3 grid graph, you mark a spot.") 
        MessageStop("2 - The sign that you mark on the spot depends on the winner")
        MessageStop("3 - You mark a row on the 3x3 grid graph in order to win a point")
        MessageStop("4 - The goal for you and your opponent is to get 2 points")
        MessageStop("5 - This is by stopping your opponent from marking a row on the graph.")
        MessageStop("6 - Strategy is key on this game.")  
    elif GameBeingExplained == "GTN":
        MessageStop("1 - A random number is generated by the system.") 
        MessageStop("2 - You and your opponent has the goal of guessing that number.")
        MessageStop("3 - When you guess the number correctly, you get a point.")
        MessageStop("4 - When you guess the number incorrectly but almost correctly,\nYou get half a point")
        MessageStop("5 - You and your opponent also has a goal of getting 3 points.")
        MessageStop('''6 - If you both manage to get 3 points, there will be a tiebreaker.
In the tiebreaker, There is no getting half a point.
You and your opponent will instead have to guess the number correctly
The range of numbers generated is smaller in the tiebreaker.''')
        MessageStop('''7 - If you and your oppponent guess the correct number,
You both get a point, unless it is a tiebreaker.''')

def ExplanationSuggestion(GametoExplain):
    Explained = False
    clearScreen()
    while True:
        try:
            Explanationchoice = YesOrNo(f"Would you like {"an" if Explained == False else "another"} explanation on this game?")
        except: InvalidInput(); continue
        if Explanationchoice == 1:
            print("Alright, allow me to explain the game for you."); sleep(2)
            GameExplanation(GametoExplain) # "Game System", "RPS" , "4C" , "GTN" , "BG" , "TTT" , "Connect4"
            Explained = True # No Continue needed
        elif Explanationchoice == 2: print("Alright, GOOD LUCK!"); sleep(1.5); clearScreen(); break