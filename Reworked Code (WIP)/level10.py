import time, math, random
from guide import NumChoiceWithQuit, ExplanationSuggestion, InvalidInput, MessageStop, NumChoice
from UsefulStuff import Red, reset, yellow, Blue, red, clearScreen

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

   
# Universal Functions

# Custom Functions & Stuff

YourSd = Blue+"O"+reset # Your defaultly blue
BotSd = Red+"O"+reset # Bot is defaultly red

def NewConnect4Board(a,b):
       a = b
       clearScreen()
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
       print(Connect4Board)
       return Connect4Board

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
       NumChoiceWithQuit()

def Connect4Check(): # Win condition
       Connect4Analyzation = ""
       for i in range(28): # Towers (Goes through all 1st 4 rows and check if a tower occurs)
              if C4List[i] == C4List[i + 7] == C4List[i + 14] == C4List[i + 21] and C4List[i] != "_": # Checks for a match (That aren't empty)
                     input("Error 1")
                     Connect4Analyzation = "game" # Match occurs after either person's turn means they won
       for i in range(0,28,7): # For going to the next row
              for i2 in range(4): # Starts at column indexes 0 - 3, 7 - 10, etc and goes up
                     if C4List[i2 + i] == C4List[i2 + i + 8] == C4List[i2 + i + 16] == C4List[i2 + i + 24] and C4List[i2] != "_":
                            print(i2)
                            input("Error 2")
                            Connect4Analyzation = "game"
       for i in range(0,28,7): 
              for i2 in range(6,2,-1): # Starts at column indexes 6 - 3 and goes down (Starts from the right edge this time)
                     if C4List[i2 + i] == C4List[i2 + i + 6] == C4List[i2 + i + 12] == C4List[i2 + i + 18 and C4List[i2] != "_"]:
                            input("Error 3")
                            Connect4Analyzation = "game"
       for i in range(0,42,7): # Straights (Starts at each row, and checks if there's a connect 4 starting from index 0 up to starting at index 3)
              for i2 in range(4): 
                     if C4List[i2 + i] == C4List[i2 + i + 1] == C4List[i2 + i + 2] == C4List[i2 + i + 3] and C4List[i2] != "_":
                            input("Error 4") 
                            Connect4Analyzation = "game"
       if "_" not in C4List and Connect4Analyzation == "": # If there's no more empty areas
              Connect4Analyzation = "draw"
       return Connect4Analyzation

def DrawFunction():
       print("\n DRAW! \n")
       MessageStop()
       clearScreen()
       temp = BotSd
       BotSd = YourSd 
       YourSd = temp # Swap variables/coin colors
       for i in C4List:
              C4List[i] = "_" # All items are _ again

def level10_function():  
       while True:
              DifficultyModes = ["Easy","Hard"]
              print("\n Choose your difficulty for Connect FOUR:")
              time.sleep(0.5)
              print("\n" + Blue + "Easy (Bot has no brain)" + reset)
              time.sleep(0.25)
              print("\n" + Red + "Hard (Bot has big brain) " + reset)
              time.sleep(0.25)
              NumChoice()
              try:
                     DifficultyChoice = DifficultyModes[int(input(""))] - 1
                     print(f"Alright! {DifficultyChoice} difficulty of Connect FOUR loading!")
                     time.sleep(1.5)
                     clearScreen()
                     break                                              
              except:
                     InvalidInput()
                     continue
       ExplanationSuggestion("4C")
       Yourturn = True
       while True: 
              while Yourturn == True:
                     print(Connect4Board)
                     print("It's your turn! Choose your Column")
                     ListColumnChoices()
                     try:
                            Yourgo = int(input(""))
                            if Yourgo not in [0,1,2,3,4,5,6,7]:
                                   InvalidInput()
                                   continue
                     except:
                            InvalidInput()
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
                                   NewConnect4Board(C4List[Yourgo - 1 + i],YourSd)
                                   ColumnFull = False
                                   print(f"You chose to fill in Row {math.ceil(Yourgo + i)}, Column {Yourgo}")
                                   Yourturn = False
                                   time.sleep(1)
                                   clearScreen()
                                   break
                     if ColumnFull == True:
                            print(Red+"Column is filled"+reset)
                            MessageStop()
                            continue

              Connect4Results = Connect4Check()  # Checks if your go was the win
              if Connect4Results != "":
                     print(Connect4Board)
                     if Connect4Results == "game":
                            print(Blue+"\n You have connected four! \n"+reset)
                            MessageStop()
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
                                          Oppgo = TowerCheckList[TowerCheckList.index("_")]   
                                   elif DiagonalRightCheckList.count(YourSd) == 3:
                                          Oppgo = DiagonalRightCheckList[DiagonalRightCheckList.index("_")]  
                                   elif DiagonalLeftCheckList.count(YourSd) == 3:
                                          Oppgo = DiagonalLeftCheckList[DiagonalLeftCheckList.index("_")]  
                                         
                            for i in range(4): # Straights
                                   RowCheckList1 = C4List[i] == C4List[i + 1] == C4List[i + 2] == C4List[i + 3]
                                   RowCheckList2 = C4List[i + 7] == C4List[i + 8] == C4List[i + 9] == C4List[i + 10]
                                   RowCheckList3 = C4List[i + 14] == C4List[i + 15] == C4List[i + 16] == C4List[i + 17]
                                   RowCheckList4 = C4List[i + 21] == C4List[i + 22] == C4List[i + 23] == C4List[i + 24]
                     else:
                            Oppgo = random.randrange(1,8)

                     for i in range(0,42,7): # Doesn't go to 42 as it will go over the limit
                            ColumnFull = True # May delete because by this time, the bot may already know where they wanna go
                            if C4List[Oppgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                                   continue
                            else:
                                   C4List[Oppgo - 1 + i] = BotSd
                                   ColumnFull = False # Same
                                   print(Connect4Board)
                                   print(f"Bot chose to fill in Row {math.ceil(Oppgo + i)}, Column {Oppgo}")
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
                                   MessageStop()
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
                            if Yourgo not in [0,1,2,3,4,5,6,7]:
                                   InvalidInput()
                                   continue
                     except:
                            InvalidInput()
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
                                   Connect4Board = NewConnect4Board(C4List[Yourgo - 1 + i],YourSd)
                                   C4List[Yourgo - 1 + i] = YourSd
                                   ColumnFull = False # Column wasn't full after all
                                   print(f"{Player1Name} chose to fill in Row {math.ceil((Yourgo + i) / 7)}, Column {Yourgo}") # Row Calculation: You chose column 2. (2 + 7) / 7 ceiled is 2, so you're on row 2. Ofc column is the # u chose
                                   Yourturn = False # No longer your turn
                                   time.sleep(1)
                                   clearScreen()
                                   break
                     if ColumnFull == True: # Column isn't proved to not be full
                            print(Red+"Column is filled"+reset)
                            MessageStop()
                            continue # Turn repeats

                     Connect4Results = Connect4Check()
                     if Connect4Results != "":
                            print(Connect4Board)
                            if Connect4Results == "game":
                                   print(Blue+f"\n {Player1Name} have connected four! \n"+reset)
                                   MessageStop()
                                   return "W" # Returns back to select, signifying Player 1 the winner
                            elif Connect4Results == "draw":
                                   DrawFunction() # Announces draw, swaps coins, resets board
 
              while Yourturn == False: # Player 2's turn
                     print(Connect4Board)
                     print(f"It's {Player2Name}'s turn!")
                     ListColumnChoices()
                     try:
                            Oppgo = int(input(""))
                            if Oppgo not in [0,1,2,3,4,5,6,7]:
                                   InvalidInput()
                                   continue
                     except:
                            InvalidInput()
                            continue
                     if Oppgo == 0:
                            if Quit_function() == "Quit":
                                   return "Quit"
                            else:
                                   continue

                     for i in range(0, 42, 7): 
                            ColumnFull = True 
                            if C4List[Oppgo - 1 + i] != "_": 
                                   continue
                            else:
                                   C4List[Oppgo - 1 + i] = BotSd
                                   ColumnFull = False # Same
                                   clearScreen()
                                   print(Connect4Board)
                                   print(f"{Player2Name} chose to fill in Row {math.ceil(Oppgo + i)}, Column {Oppgo}")
                                   Yourturn = True
                                   time.sleep(1)
                                   clearScreen()
                                   break # breaks outta loop to not repeat
                     if ColumnFull == True:
                            print(Red+"Column is filled"+reset)
                            MessageStop()
                            continue # Turn repeats
                     
                     Connect4Results = Connect4Check()
                     if Connect4Results != "":
                            print(Connect4Board)
                            if Connect4Results == "game":
                                   print(Red+f"\n {Player2Name} has connected four! \n"+reset)
                                   MessageStop()
                                   return "L" # Loser for player 1
                            elif Connect4Results == "draw":
                                   DrawFunction()
#CONNECT FOUR
