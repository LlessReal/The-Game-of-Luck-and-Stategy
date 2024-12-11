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
   
def PETC_function(): 
 Help = input(yellow + '''
(Press Enter to Continue)
''' + reset)
 clearScreen()

def PNTC_function():  # Press a number then enter
 print(yellow + '''
(Press a number and then Enter to choose)''' + reset)
 
def PNTCOQ_function(): # Same thing but with quit functionality
 print(yellow + '''
(Press a number and then Enter to choose. '''+reset+red+'''Press 0 to '''+reset+Red+'''quit.'''+reset+yellow+''')'''+reset)
 
def II_function():
 clearScreen()
 print(Red + "Invalid Input" + reset)
 time.sleep(1)
 print('''You must press the number on the left.
Then, you press enter to choose.''')
 PETC_function()

def YOR_function(): # Yes or No
 time.sleep(0.5)
 print('''
1 - '''+Blue+'''Yes'''+reset)
 time.sleep(0.25)
 print('''
2 - '''+Red+'''No'''+reset)
 time.sleep(0.25)
 PNTC_function()

def level10_function():
       C4List = []
       for i in range(42):
              C4List.append("_")
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
                     break
              else:
                     II_function()
 
       Connect4Board = f'''6 | {C4List[35]} | {C4List[36]} | {C4List[37]} | {C4List[38]} | {C4List[39]} | {C4List[40]} | {C4List[41]}
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
1 | 2 | 3 | 4 | 5 | 6 | 7'''
       Yourturn = True
       while winstatement != "win" and winstatement != "lose": 
              YourSd = Red+"O"+reset # You're side one
              BotSd = Blue+"O"+reset # bot is side 2
              while Yourturn == True:
                     print(Connect4Board)
                     print("It's your turn! Choose your Column")
                     time.sleep(0.25)
                     print("1 - 1st Column",end = '   ')
                     print("2 - 2nd Column",end = '   ')
                     print("3 - 3rd Column",end = '   ')
                     print("4 - 4th Column")
                     print("\n 5 - 5th Column",end = '   ')
                     print("6 - 6th Column",end = '   ')
                     print("7 - 7th Column")
                     time.sleep(0.25)
                     PNTCOQ_function() # Quit choice is 0, remember
              try:
                     Yourgo = int(input(""))
                     clearScreen()
              except:
                     II_function()
                     continue
              while Yourgo == 0:
                     print("Are you sure you want to "+Red+"quit"+reset+"?")
                     YOR_function() # prints yes or no
                     try:
                            Quitchoice = int(input(""))
                     except:
                            II_function()
                            continue
                     if Quitchoice == 1:
                            print("Understood, you will now return to the menu screen.")
                            time.sleep(2)
                            return "Quit"
                     if Quitchoice == 2:
                            print("\n Alrighty then!")
                            time.sleep(1)
                            break
              if Quitchoice == 2:
                     continue

              for i in range(0, 35, 7): # Doesn't go to 42 as it will go over the limit
                     SideFull = True
                     if C4List[Yourgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                            continue
                     else:
                            C4List[Yourgo - 1 + i] = YourSd
                            SideFull = False
                            print(Connect4Board)
                            print(f"You chose to fill in Row {math.ceil(Yourgo + i)}, Column {Yourgo}")
                            Yourturn = False
                            time.sleep(1)
                            break

              if SideFull == True:
                     print(Red+"Column is filled"+reset)
                     PETC_function()
                     continue

              winstatement = ""
              for i in range(28): # Diagonals
                     if C4List[i] == C4List[i + 7] == C4List[i + 14] == C4List[i + 21] or C4List[i] == C4List[i + 8] == C4List[i + 16] == C4List[i + 24] or C4List[i] == C4List[i + 6] == C4List[i + 12] == C4List[i + 18]:
                            if C4List[i] == YourSd:
                                   winstatement = "win"
              for i in range(4): # Straights
                     if C4List[i] == C4List[i + 1] == C4List[i + 2] == C4List[i + 3] or C4List[i + 7] == C4List[i + 8] == C4List[i + 9] == C4List[i + 10] or C4List[i + 14] == C4List[i + 15] == C4List[i + 16] == C4List[i + 17] or C4List[i + 21] == C4List[i + 22] == C4List[i + 23] == C4List[i + 24]:
                            if C4List[i] == YourSd:
                                   winstatement = "win"
              if "_" not in C4List and winstatement == "":
                     winstatement = "draw"
              elif winstatement != "":
                     print(Connect4Board)
                     if winstatement == "win":
                            print(Blue+"\n You have connected four! \n"+reset)
                            PETC_function()
                            if DifficultyChoice == "Easy":
                                   return "EW"
                            elif DifficultyChoice == "Medium":
                                   return "MW"
                            elif DifficultyChoice == "Hard":
                                   return "HW"
                     elif winstatement == "draw":
                            print("\n DRAW! \n")
                            PETC_function()
                            clearScreen()
                            YourSd = Blue+"O"+reset
                            BotSd = Red+"O"+reset
                            for i in C4List:
                                   C4List[i] = "_" # Replacement of all sides equaling _ again
                                   # R1Clmn1T means taken R1Clmn1TBY means taken by you R1Clmn1TBB means Taken by bot (All no longer needed)
              while Yourturn == False:
                     if DifficultyChoice == "Hard":
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

                     for i in range(0, 35, 7): # Doesn't go to 42 as it will go over the limit
                            SideFull = True # May delete because by this time, the bot may already know where they wanna go
                            if C4List[Botgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                                   continue
                            else:
                                   C4List[Botgo - 1 + i] = BotSd
                                   SideFull = False # Same
                                   print(Connect4Board)
                                   print(f"Bot chose to fill in Row {math.ceil(Botgo + i)}, Column {Botgo}")
                                   Yourturn = True
                                   time.sleep(1)
                                   clearScreen()
                     if SideFull == True:
                            continue
                     
                     for i in range(28): # Diagonals
                            if C4List[i] == C4List[i + 7] == C4List[i + 14] == C4List[i + 21] or C4List[i] == C4List[i + 8] == C4List[i + 16] == C4List[i + 24] or C4List[i] == C4List[i + 6] == C4List[i + 12] == C4List[i + 18]:
                                   if C4List[i] == BotSd:
                                          winstatement = "loss"
                     for i in range(4): # Straights
                            if C4List[i] == C4List[i + 1] == C4List[i + 2] == C4List[i + 3] or C4List[i + 7] == C4List[i + 8] == C4List[i + 9] == C4List[i + 10] or C4List[i + 14] == C4List[i + 15] == C4List[i + 16] == C4List[i + 17] or C4List[i + 21] == C4List[i + 22] == C4List[i + 23] == C4List[i + 24]:
                                   if C4List[i] == BotSd:
                                          winstatement = "loss"
                     if "_" not in C4List and winstatement == "":
                            winstatement = "draw"
                     elif winstatement != "":
                            print(Connect4Board)
                            if winstatement == "loss":
                                   print(Red+"\n Your opponent has connected four! \n"+reset)
                                   PETC_function()
                                   if DifficultyChoice == "Easy":
                                          return "EL"
                                   elif DifficultyChoice == "Medium":
                                          return "ML"
                                   elif DifficultyChoice == "Hard":
                                          return "HL"
                            elif winstatement == "draw":
                                   print("\n DRAW! \n")
                                   PETC_function()
                                   clearScreen()
                                   YourSd = Red+"O"+reset
                                   BotSd = Blue+"O"+reset
                                   for i in C4List:
                                          C4List[i] = "_" # Replacement of all sides equaling _ again
                                          # R1Clmn1T means taken R1Clmn1TBY means taken by you R1Clmn1TBB means Taken by bot (All no longer needed)
   
def pvplevel10_function(OnePlayerName,TwoPlayerName):
       C4List = []
       for i in C4List:
              C4List[i] = "_" # Replacement of all sides equaling _ again
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
                     break
              else:
                     II_function()
       Yourturn = True
       Connect4Board = f'''6 | {C4List[35]} | {C4List[36]} | {C4List[37]} | {C4List[38]} | {C4List[39]} | {C4List[40]} | {C4List[41]}
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
    1 | 2 | 3 | 4 | 5 | 6 | 7'''
       while True: 
              YourSd = Red+"O"+reset
              BotSd = Blue+"O"+reset
              while Yourturn == True:
                     print(Connect4Board)
                     print(f"It's {OnePlayerName}'s turn! Choose your Column")
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
                     try:
                            Yourgo = int(input(""))
                            clearScreen()
                     except:
                            II_function()
                            continue
                     Quitchoice = 0
                     while Yourgo == 0:
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
                            break
                     if Quitchoice == 2:
                            continue
                     for i in range(0, 35, 7): # Doesn't go to 42 as it will go over the limit
                            SideFull = True
                            if C4List[Yourgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                                   continue
                            else:
                                   C4List[Yourgo - 1 + i] = YourSd
                                   SideFull = False
                                   print(Connect4Board)
                                   print(f"{OnePlayerName} chose to fill in Row {math.ceil(Yourgo + i)}, Column {Yourgo}")
                                   Yourturn = False
                                   time.sleep(1)
                                   break

                     if SideFull == True:
                            print(Red+"Column is filled"+reset)
                            PETC_function()
                            continue

                     winstatement = ""
                     for i in range(28): # Diagonals
                            if C4List[i] == C4List[i + 7] == C4List[i + 14] == C4List[i + 21] or C4List[i] == C4List[i + 8] == C4List[i + 16] == C4List[i + 24] or C4List[i] == C4List[i + 6] == C4List[i + 12] == C4List[i + 18]:
                                   if C4List[i] == YourSd:
                                          winstatement = "win"
                     for i in range(4): # Straights
                            if C4List[i] == C4List[i + 1] == C4List[i + 2] == C4List[i + 3] or C4List[i + 7] == C4List[i + 8] == C4List[i + 9] == C4List[i + 10] or C4List[i + 14] == C4List[i + 15] == C4List[i + 16] == C4List[i + 17] or C4List[i + 21] == C4List[i + 22] == C4List[i + 23] == C4List[i + 24]:
                                   if C4List[i] == YourSd:
                                          winstatement = "win"
                     if "_" not in C4List and winstatement == "":
                            winstatement = "draw"
                     elif winstatement != "":
                            print(Connect4Board)
                            if winstatement == "win":
                                   print(Blue+f"\n {OnePlayerName} have connected four! \n"+reset)
                                   PETC_function()
                                   return "W"
                            elif winstatement == "draw":
                                   print("\n DRAW! \n")
                                   PETC_function()
                                   clearScreen()
                                   YourSd = Blue+"O"+reset
                                   BotSd = Red+"O"+reset
                                   for i in C4List:
                                          C4List[i] = "_" # Replacement of all sides equaling _ again
                                          # R1Clmn1T means taken R1Clmn1TBY means taken by you R1Clmn1TBB means Taken by bot (All no longer needed)
 
              while Yourturn == False:
                     print(Connect4Board)
                     print(f"It's {TwoPlayerName}'s turn!")
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
                     try:
                            Botgo = int(input(""))
                            clearScreen()
                     except:
                            II_function()
                            continue
                     while Botgo == 0:
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
                                   break
                     if Quitchoice == 2:
                            continue

                     for i in range(0, 35, 7): # Doesn't go to 42 as it will go over the limit
                            SideFull = True # May delete because by this time, the bot may already know where they wanna go
                            if C4List[Botgo - 1 + i] != "_": # If your slot in the row is not empty, continues
                                   continue
                            else:
                                   C4List[Botgo - 1 + i] = BotSd
                                   SideFull = False # Same
                                   print(Connect4Board)
                                   print(f"{TwoPlayerName} chose to fill in Row {math.ceil(Botgo + i)}, Column {Botgo}")
                                   Yourturn = True
                                   time.sleep(1)
                                   clearScreen()
                     if SideFull == True:
                            continue
                     
                     for i in range(28): # Diagonals
                            if C4List[i] == C4List[i + 7] == C4List[i + 14] == C4List[i + 21] or C4List[i] == C4List[i + 8] == C4List[i + 16] == C4List[i + 24] or C4List[i] == C4List[i + 6] == C4List[i + 12] == C4List[i + 18]:
                                   if C4List[i] == BotSd:
                                          winstatement = "loss"
                     for i in range(4): # Straights
                            if C4List[i] == C4List[i + 1] == C4List[i + 2] == C4List[i + 3] or C4List[i + 7] == C4List[i + 8] == C4List[i + 9] == C4List[i + 10] or C4List[i + 14] == C4List[i + 15] == C4List[i + 16] == C4List[i + 17] or C4List[i + 21] == C4List[i + 22] == C4List[i + 23] == C4List[i + 24]:
                                   if C4List[i] == BotSd:
                                          winstatement = "loss"
                     if "_" not in C4List and winstatement == "":
                            winstatement = "draw"
                     elif winstatement != "":
                            print(Connect4Board)
                            if winstatement == "loss":
                                   print(Red+f"\n {TwoPlayerName} has connected four! \n"+reset)
                                   PETC_function()
                                   return "L"
                            elif winstatement == "draw":
                                   print("\n DRAW! \n")
                                   PETC_function()
                                   clearScreen()
                                   YourSd = Red+"O"+reset
                                   BotSd = Blue+"O"+reset
                                   for i in C4List:
                                          C4List[i] = "_" # Replacement of all sides equaling _ again
                                          # R1Clmn1T means taken R1Clmn1TBY means taken by you R1Clmn1TBB means Taken by bot (All no longer needed)
#CONNECT FOUR