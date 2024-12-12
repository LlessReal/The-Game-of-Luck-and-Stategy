import random
import time
import math
from os import system as sys
from os import name as osname
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"

def clearScreen():
 if osname == "nt":
  sys("cls")
 else:
  sys("clear")
   
# Universal Functions

def PETC_function(): # Press Enter to Continue
       Help = input(yellow + "\n (Press Enter to Continue) \n" + reset)
       clearScreen()

def PNTC_function():  # Press a Number, then Enter to Continue
       print(yellow + "\n (Press a number and then Enter to choose)" + reset)
 
def PNTCOQ_function(): # Same thing but with quit functionality
       print(yellow + "\n (Press a number and then Enter to choose. "+reset+red+"Press 0 to "+reset+Red+"quit."+reset+yellow+")"+reset)
 
def II_function(): # Invalid Input
       clearScreen()
       print(Red + "Invalid Input" + reset)
       time.sleep(1)
       print("\n You must press the number on the left. Then, you press enter to choose.")
       PETC_function()

def YOR_function(): # Yes or No
       time.sleep(0.5)
       print(" \n 1 - "+Blue+"Yes"+reset)
       time.sleep(0.25)
       print("\n 2 - "+Red+"No"+reset)
       time.sleep(0.25)
       PNTC_function()

def Quit_function(): # Want to Quit?
       while True:
              print("Are you sure you want to "+Red+"quit"+reset+"?")
              YOR_function()
              try:
                     Quitchoice = int(input(""))
              except:
                     II_function()
                     continue
              if Quitchoice == 1:
                     print("Understood, You will now return to the menu screen.")
                     time.sleep(2)
                     return "Quit"
              if Quitchoice == 2:
                     print("\n Alrighty then!")
                     time.sleep(1)
                     return

# Custom Functions & Stuff

C4List = []
for i in range(49):
       C4List.append("_") # Makes a list 49 elements index 0 - 48
       Connect4Board = f'''7 | {C4List[42]} | {C4List[43]} | {C4List[44]} | {C4List[45]} | {C4List[46]} | {C4List[47]} | {C4List[48]}
-----------------------------
6 | {C4List[35]} | {C4List[36]} | {C4List[37]} | {C4List[38]} | {C4List[39]} | {C4List[40]} | {C4List[41]}
-----------------------------
5 | {C4List[28]} | {C4List[29]} | {C4List[30]} | {C4List[31]} | {C4List[32]} | {C4List[33]} | {C4List[34]}
-----------------------------
4 | {C4List[21]} | {C4List[22]} | {C4List[23]} | {C4List[24]} | {C4List[25]} | {C4List[26]} | {C4List[27]}
-----------------------------
3 | {C4List[14]} | {C4List[15]} | {C4List[16]} | {C4List[17]} | {C4List[18]} | {C4List[19]} | {C4List[20]}
-----------------------------
2 | {C4List[7]} | {C4List[8]} | {C4List[9]} | {C4List[10]} | {C4List[11]} | {C4List[12]} | {C4List[13]}
-----------------------------
1 | {C4List[0]} | {C4List[1]} | {C4List[2]} | {C4List[3]} | {C4List[4]} | {C4List[5]} | {C4List[6]}
1 | 2 | 3 | 4 | 5 | 6 | 7''' # Connect4Board meant to be used by all functions

YourSd = Blue+"O"+reset # Your defaultly blue
BotSd = Red+"O"+reset # Bot is defaultly red

def ListColumnChoices():
       time.sleep(0.25)
       print("1 - 1st Column",end = '   ')
       print("2 - 2nd Column",end = '   ')
       print("3 - 3rd Column",end = '   ')
       print("4 - 4th Column")
       print("\n 5 - 5th Column",end = '   ')
       print("6 - 6th Column",end = '   ')
       print("7 - 7th Column")
       time.sleep(0.25)
       PNTCOQ_function()

def Connect4Check(): # Win condition
       Connect4Analyzation = ""
       for i in range(28): # Towers (Goes through all 1st 4 rows and check if a tower occurs)
              if C4List[i] == C4List[i + 7] == C4List[i + 14] == C4List[i + 21]:
                     Connect4Analyzation = "game" # Match occurs after bot's turn means they won
       for i in range(0,28,7): # For going to the next row
              for i2 in range(4): # Diagonal Rights (Goes to the right)
                     if C4List[i2 + i] == C4List[i2 + i + 8] == C4List[i2 + i + 16] == C4List[i2 + i + 24]:
                            Connect4Analyzation = "game"
       for i in range(0,28,7): 
              for i2 in range(6,2,-1): # Diagonal Lefts (Starts from the right this time)
                     if C4List[i2 + i] == C4List[i2 + i + 6] == C4List[i2 + i + 12] == C4List[i2 + i + 18]:
                            Connect4Analyzation = "game"
       for i in range(0,42,7): # Straights (Starts at each row, and checks if there's a connect 4 starting from index 0 up to starting at index 3)
              for i2 in range(4):
                     if C4List[i2] == C4List[i2 + 1] == C4List[i2 + 2] == C4List[i2 + 3]:
                            Connect4Analyzation = "game"
       if "_" not in C4List and Connect4Analyzation == "": # If there's no more empty areas
              Connect4Analyzation = "draw"
       return Connect4Analyzation

def DrawFunction():
       print("\n DRAW! \n")
       PETC_function()
       clearScreen()
       temp = BotSd
       BotSd = YourSd 
       YourSd = temp # Swap variables/coin colors
       for i in C4List:
              C4List[i] = "_" # All items are _ again

def ExplanationFunction(): # Custom Explanation
       Explained = False
       while True:
              if Explained == False:
                     print('''Would you like an explanation on this game?''')
              elif Explained == True:
                     print('''Would you like another explanation on this game?''')
                     YOR_function()
              try:
                     Explanationchoice = int(input(""))
              except:
                     II_function()
                     continue
              if Explanationchoice == 1:
                     print("Alright, allow me to explain the game for you.")
                     time.sleep(2)
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
                     Explained = True
                     continue
              elif Explanationchoice == 2:
                     print("Alright, GOOD LUCK!")
                     time.sleep(1.5)
                     clearScreen()
                     return
              else:
                     II_function()

def level10_function():  
       while True:
              DifficultyModes = ["Easy","Hard"]
              print("\n Choose your difficulty for Connect FOUR:")
              time.sleep(0.5)
              print("\n" + Blue + "Easy (Bot has no brain)" + reset)
              time.sleep(0.25)
              print("\n" + Red + "Hard (Bot has big brain) " + reset)
              time.sleep(0.25)
              PNTC_function()
              try:
                     DifficultyChoice = DifficultyModes[int(input(""))] - 1
                     print(f"Alright! {DifficultyChoice} difficulty of Connect FOUR loading!")
                     time.sleep(1.5)
                     clearScreen()
                     break                                              
              except:
                     II_function()
                     continue
       ExplanationFunction()
       Yourturn = True
       while True: 
              YourSd = Red+"O"+reset # You're side one
              BotSd = Blue+"O"+reset # bot is side 2
              while Yourturn == True:
                     print(Connect4Board)
                     print("It's your turn! Choose your Column")
                     ListColumnChoices()
                     try:
                            Yourgo = int(input(""))
                            clearScreen()
                     except:
                            II_function()
                            continue
                     if Yourgo == 0:
                            if Quit_function() == "Quit":
                                   return "Quit"
                            else:
                                   continue

                     for i in range(0,42,7): # Doesn't go to 42 as it will go over the limit
                            ColumnFull = True
                            if C4List[Yourgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                                   continue
                            else:
                                   C4List[Yourgo - 1 + i] = YourSd
                                   ColumnFull = False
                                   print(Connect4Board)
                                   print(f"You chose to fill in Row {math.ceil(Yourgo + i)}, Column {Yourgo}")
                                   Yourturn = False
                                   time.sleep(1)
                                   clearScreen()
                                   break
                     if ColumnFull == True:
                            print(Red+"Column is filled"+reset)
                            PETC_function()
                            continue

              Connect4Results = Connect4Check()  # Checks if your go was the win
              if Connect4Results != "":
                     print(Connect4Board)
                     if Connect4Results == "game":
                            print(Blue+"\n You have connected four! \n"+reset)
                            PETC_function()
                            if DifficultyChoice == "Easy":
                                   return "EW"
                            elif DifficultyChoice == "Medium":
                                   return "MW"
                            elif DifficultyChoice == "Hard":
                                   return "HW"
                     elif Connect4Results == "draw":
                            DrawFunction()
       
              while Yourturn == False:
                     if DifficultyChoice == "Hard": # Still working on this lol
                            for i in range(28): # Diagonals
                                   TowerCheckList = [C4List[i],C4List[i + 7],C4List[i + 14],C4List[i + 21]]
                                   DiagonalRightCheckList = [C4List[i],C4List[i + 8],C4List[i + 16],C4List[i + 24]]
                                   DiagonalLeftCheckList = [C4List[i],C4List[i + 6],C4List[i + 12],C4List[i + 18]]
                                   if TowerCheckList.count(YourSd) == 3:
                                          Botgo = TowerCheckList[TowerCheckList.index("_")]   
                                   elif DiagonalRightCheckList.count(YourSd) == 3:
                                          Botgo = DiagonalRightCheckList[DiagonalRightCheckList.index("_")]  
                                   elif DiagonalLeftCheckList.count(YourSd) == 3:
                                          Botgo = DiagonalLeftCheckList[DiagonalLeftCheckList.index("_")]  
                                         
                            for i in range(4): # Straights
                                   RowCheckList1 = C4List[i] == C4List[i + 1] == C4List[i + 2] == C4List[i + 3]
                                   RowCheckList2 = C4List[i + 7] == C4List[i + 8] == C4List[i + 9] == C4List[i + 10]
                                   RowCheckList3 = C4List[i + 14] == C4List[i + 15] == C4List[i + 16] == C4List[i + 17]
                                   RowCheckList4 = C4List[i + 21] == C4List[i + 22] == C4List[i + 23] == C4List[i + 24]
                     else:
                            Botgo = random.randrange(1,8)

                     for i in range(0,42,7): # Doesn't go to 42 as it will go over the limit
                            ColumnFull = True # May delete because by this time, the bot may already know where they wanna go
                            if C4List[Botgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                                   continue
                            else:
                                   C4List[Botgo - 1 + i] = BotSd
                                   ColumnFull = False # Same
                                   print(Connect4Board)
                                   print(f"Bot chose to fill in Row {math.ceil(Botgo + i)}, Column {Botgo}")
                                   Yourturn = True
                                   time.sleep(1)
                                   clearScreen()
                     if ColumnFull == True:
                            continue
                     Connect4Results = Connect4Check() # Solves the winner
                     if Connect4Results != "":
                            print(Connect4Board)
                            if Connect4Results == "game":
                                   print(Red+"\n Your opponent has connected four! \n"+reset)
                                   PETC_function()
                                   if DifficultyChoice == "Easy":
                                          return "EL"
                                   elif DifficultyChoice == "Medium":
                                          return "ML"
                                   elif DifficultyChoice == "Hard":
                                          return "HL"
                            elif Connect4Results == "draw":
                                   DrawFunction()
   
def pvplevel10_function(Player1Name,Player2Name): # PVP Mode
       ExplanationFunction() # Game gets explained
       Yourturn = True
       while True: 
              while Yourturn == True:
                     print(Connect4Board)
                     print(f"It's {Player1Name}'s turn! Choose your Column")
                     ListColumnChoices() # List Choices
                     try:
                            Yourgo = int(input(""))
                     except:
                            II_function()
                            continue
                     if Yourgo == 0:
                            if Quit_function() == "Quit": # Asks quit if quit was chosen
                                   return "Quit"
                            else:
                                   continue

                     for i in range(0,42,7): # Doesn't go to 49 as it will go over the limit
                            ColumnFull = True # Assumes column is full for now
                            if C4List[Yourgo - 1 + i] != "_": # If your slot in the current row isn't empty, goes to next row
                                   continue
                            else:
                                   C4List[Yourgo - 1 + i] = YourSd # Puts coin in designate row
                                   ColumnFull = False # Column wasn't full after all
                                   clearScreen()
                                   print(Connect4Board) # Clear screen and show new board
                                   print(f"{Player1Name} chose to fill in Row {math.ceil((Yourgo + i) / 7)}, Column {Yourgo}") # Row Calculation: You chose column 2. (2 + 7) / 7 ceiled is 2, so you're on row 2. Ofc column is the # u chose
                                   Yourturn = False # No longer your turn
                                   time.sleep(1)
                                   clearScreen()
                                   break
                     if ColumnFull == True: # Column isn't proved to not be full
                            print(Red+"Column is filled"+reset)
                            PETC_function()
                            continue # Turn repeats

                     Connect4Results = Connect4Check()
                     if Connect4Results != "":
                            print(Connect4Board)
                            if Connect4Results == "game":
                                   print(Blue+f"\n {Player1Name} have connected four! \n"+reset)
                                   PETC_function()
                                   return "W" # Returns back to select, signifying Player 1 the winner
                            elif Connect4Results == "draw":
                                   DrawFunction() # Announces draw, swaps coins, resets board
 
              while Yourturn == False: # Player 2's turn
                     print(Connect4Board)
                     print(f"It's {Player2Name}'s turn!")
                     ListColumnChoices()
                     try:
                            Botgo = int(input(""))
                     except:
                            II_function()
                            continue
                     if Botgo == 0:
                            if Quit_function() == "Quit":
                                   return "Quit"
                            else:
                                   continue

                     for i in range(0, 42, 7): 
                            ColumnFull = True 
                            if C4List[Botgo - 1 + i] != "_": 
                                   continue
                            else:
                                   C4List[Botgo - 1 + i] = BotSd
                                   ColumnFull = False # Same
                                   clearScreen()
                                   print(Connect4Board)
                                   print(f"{Player2Name} chose to fill in Row {math.ceil(Botgo + i)}, Column {Botgo}")
                                   Yourturn = True
                                   time.sleep(1)
                                   clearScreen()
                                   break # breaks outta loop to not repeat
                     if ColumnFull == True:
                            print(Red+"Column is filled"+reset)
                            PETC_function()
                            continue # Turn repeats
                     
                     Connect4Results = Connect4Check()
                     if Connect4Results != "":
                            print(Connect4Board)
                            if Connect4Results == "game":
                                   print(Red+f"\n {Player2Name} has connected four! \n"+reset)
                                   PETC_function()
                                   return "L" # Loser for player 1
                            elif Connect4Results == "draw":
                                   DrawFunction()
#CONNECT FOUR