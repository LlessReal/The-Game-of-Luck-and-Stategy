import time, random
from guide import NumChoiceWithQuit, ExplanationSuggestion, InvalidInput, MessageStop, NumChoice, YesOrNo
from UsefulStuff import Red, reset, yellow, Blue, clearScreen

def level9_function():
 Yourpoints = 0
 Botpoints = 0
 Yourshape = 1
 Botshape = 2
 Sd1 = "_"
 Sd2 = "_"
 Sd3 = "_"
 Sd4 = "_"
 Sd5 = "_"
 Sd6 = "_"
 Sd7 = "_"
 Sd8 = "_"
 Sd9 = "_"
 S1T = False 
 S2T = False 
 S3T = False 
 S4T = False 
 S5T = False 
 S6T = False 
 S7T = False 
 S8T = False 
 S9T = False 
 S1TBY = False 
 S2TBY = False  
 S3TBY = False  
 S4TBY = False 
 S5TBY = False 
 S6TBY = False 
 S7TBY = False  
 S8TBY = False 
 S9TBY = False 
 S1TBB = False 
 S2TBB = False 
 S3TBB = False 
 S4TBB = False 
 S5TBB = False 
 S6TBB = False 
 S7TBB = False 
 S8TBB = False 
 S9TBB = False
 while True:
  print('''
Choose your difficulty for Tic-Tac-Toe''')
  time.sleep(0.5)
  print('''
1 - ''' + Blue + '''Easy (Bot has no brain)''' + reset)
  time.sleep(0.25)
  print('''
2 - ''' + yellow + '''Medium (Bot has a brain)''' + reset)
  time.sleep(0.25)
  print('''
3 - ''' + Red + '''Hard (Bot has a big brain)''' + reset)
  time.sleep(0.25)
  NumChoice()
  try:
   DifficultyChoice = int(input(""))
  except:
   InvalidInput()
   continue
  if DifficultyChoice == 1:
     print("Alright! Easy difficulty for Tic-Tac-Toe loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 2:
     print("Alright! Medium difficulty for Tic-Tac-Toe loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 3:
     print("Alright! Hard difficulty for Tic-Tac-Toe loading!")
     time.sleep(1.5)
     clearScreen()
     break
  else:
    InvalidInput()
    continue
 Explained = False
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
   clearScreen()
   print('''1 - On a 3x3 grid graph, you mark a spot.''') 
   MessageStop()
   print('''2 - The sign that you mark on the spot depends on the winner''')
   MessageStop()
   print('''3 - You mark a row on the 3x3 grid graph in order to win a point''')
   MessageStop()
   print('''4 - The goal for you and your opponent is to get 2 points''')
   MessageStop()
   print('''5 - You can stop your opponent from winning.
This is by stopping your opponent from marking a row on the graph.''')
   MessageStop()
   print('''6 - Strategy is key on this game.''')
   MessageStop()
   Explained = True
   continue
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   InvalidInput()
 TicTacToeBoard = '''{0} | {1} | {2}
----------
{3} | {4} | {5} 
----------
{6} | {7} | {8}'''
 while Yourpoints < 1 and Botpoints < 1: 
  if Yourshape == 1:
   YourSd = "X"
  elif Yourshape == 2:
   YourSd = "O"
  if Botshape == 1:
   BotSd = "X"
  elif Botshape == 2:
   BotSd = "O"
  Yourturn = True
  while Yourturn == True:
   print(TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9))
   print("It's your turn! Choose your spot that you want to mark")
   time.sleep(0.5)
   print("")
   print("1 - Top-left",end = '       ')
   print("2 - Top-middle",end = '      ')
   print("3 - Top-right")
   time.sleep(0.25)
   print("")
   print("4 - Mid-left",end = '       ')
   print("5 - Mid-middle",end = '      ')
   print("6 - Mid-right")
   time.sleep(0.25)
   print("")
   print("7 - Bot-left",end = '       ')
   print("8 - Bot-middle",end = '      ')
   print("9 - Bot-right")
   time.sleep(0.25)
   print("")
   NumChoiceWithQuit()
   try:
    Yourgo = int(input(""))
    clearScreen()
   except:
    InvalidInput()
    continue
   Quitchoice = 0
   while Yourgo == 0:
    print("Are you sure you want to "+Red+"quit"+reset+"?")
    YesOrNo()
    try:
     Quitchoice = int(input(""))
    except:
     InvalidInput()
     continue
    if Quitchoice == 1:
     print("Understood.")
     time.sleep(1)
     print("")
     print("You will now return to the menu screen.")
     time.sleep(2)
     return "Quit"
    if Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
   if Quitchoice == 2:
     continue
   clearScreen()
   if Yourgo == 1:
    if S1T == False:
     Sd1 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Top-left.")
     S1TBY = True
     S1T = True
    elif S1T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 2:
    if S2T == False:
     Sd2 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Top-middle.")
     S2TBY = True
     S2T = True
    elif S2T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 3:
    if S3T == False:
     Sd3 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Top-right.")
     S3TBY = True
     S3T = True
    elif S3T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 4:
    if S4T == False:
     Sd4 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Mid-left.")
     S4TBY = True
     S4T = True
    elif S4T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 5:
    if S5T == False:
     Sd5 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Mid-middle.")
     S5TBY = True
     S5T = True
    elif S5T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 6:
    if S6T == False:
     Sd6 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Mid-right.")
     S6TBY = True
     S6T = True
    elif S6T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 7:
    if S7T == False:
     Sd7 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Bot-left.")
     S7TBY = True
     S7T = True
    elif S7T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 8:
    if S8T == False:
     Sd8 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Bot-middle.")
     S8TBY = True
     S8T = True
    elif S8T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 9:
    if S9T == False:
     Sd9 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("You chose to fill in Bot-right.")
     S9TBY = True
     S9T = True
    elif S9T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   else:
    InvalidInput()
    continue
   time.sleep(1)
   clearScreen()
   Yourturn = False
   if (S1TBY == True and S2TBY == True and S3TBY == True) or (S1TBY == True and S5TBY == True and S9TBY == True) or (S1TBY == True and S4TBY == True and S7TBY == True) or (S2TBY == True and S5TBY == True and S8TBY == True) or (S3TBY == True and S6TBY == True and S9TBY == True) or (S3TBY == True and S5TBY == True and S7TBY == True) or (S4TBY == True and S5TBY == True and S6TBY == True) or (S7TBY == True and S8TBY == True and S9TBY == True):
    print(NewTicTacToeBoard)
    print("")
    print(Blue+"You have made a cross!"+reset)
    print("")
    Yourpoints = Yourpoints + 1
    MessageStop()
    Yourshape = 2
    Botshape = 1
    YourSd = "O"
    BotSd = "X"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False 
    S3TBY = False 
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False 
    S8TBY = False 
    S9TBY = False
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False 
   elif S1T == True and S2T == True and S3T == True and S4T == True and S5T == True and S6T == True and S7T == True and S8T == True and S9T == True:
    print(NewTicTacToeBoard)
    print("")
    print("Full Board!")
    print("")
    MessageStop()
    Yourshape = 2
    Botshape = 1
    YourSd = "O"
    BotSd = "X"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False  
    S3TBY = False  
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False  
    S8TBY = False 
    S9TBY = False 
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False
  Botturn = True
  while Botturn == True and Yourpoints != 2:
   if (S2TBB == True and S3TBB == True and S1T == False and DifficultyChoice == 3) or (S4TBB == True and S7TBB == True and S1T == False and DifficultyChoice == 3) or (S5TBB == True and S9TBB == True and S1T == False and DifficultyChoice == 3):
    Botgo = 1
   elif (S1TBB == True and S3TBB == True and S2T == False and DifficultyChoice == 3) or (S5TBB == True and S8TBB == True and S2T == False and DifficultyChoice == 3):
    Botgo = 2
   elif (S1TBB == True and S2TBB == True and S3T == False and DifficultyChoice == 3) or (S6TBB == True and S9TBB == True and S3T == False and DifficultyChoice == 3) or (S5TBB == True and S7TBB == True and S3T == False and DifficultyChoice == 3):
    Botgo = 3
   elif (S1TBB == True and S7TBB == True and S4T == False and DifficultyChoice == 3) or (S5TBB == True and S6TBB == True and S4T == False and DifficultyChoice == 3):
    Botgo = 4
   elif (S4TBB == True and S6TBB == True and S5T == False and DifficultyChoice == 3) or (S2TBB == True and S8TBB == True and S5T == False and DifficultyChoice == 3) or (S1TBB == True and S9TBB == True and S5T == False and DifficultyChoice == 3) or (S3TBB == True and S7TBB == True and S5T == False and DifficultyChoice == 3):
    Botgo = 5
   elif (S3TBB == True and S9TBB == True and S6T == False and DifficultyChoice == 3) or (S4TBB == True and S5TBB == True and S6T == False and DifficultyChoice == 3):
    Botgo = 6
   elif (S3TBB == True and S5TBB == True and S7T == False and DifficultyChoice == 3) or (S1TBB == True and S4TBB == True and S7T == False and DifficultyChoice == 3) or (S8TBB == True and S9TBB == True and S7T == False and DifficultyChoice == 3):
    Botgo = 7
   elif (S7TBB == True and S9TBB == True and S8T == False and DifficultyChoice == 3) or (S2TBB == True and S5TBB == True and S8T == False and DifficultyChoice == 3):
    Botgo = 8
   elif (S1TBB == True and S5TBB == True and S9T == False and DifficultyChoice == 3) or (S3TBB == True and S6TBB == True and S9T == False and DifficultyChoice == 3) or (S7TBB == True and S8TBB == True and S9T == False and DifficultyChoice == 3):
    Botgo = 9
   elif (S2TBY == True and S3TBY == True and S1T == False and DifficultyChoice >= 2) or (S4TBY == True and S7TBY == True and S1T == False and DifficultyChoice >= 2) or (S5TBY == True and S9TBY == True and S1T == False and DifficultyChoice >= 2):
    Botgo = 1
   elif (S1TBY == True and S3TBY == True and S2T == False and DifficultyChoice >= 2) or (S5TBY == True and S8TBY == True and S2T == False and DifficultyChoice >= 2):
    Botgo = 2
   elif (S1TBY == True and S2TBY == True and S3T == False and DifficultyChoice >= 2) or (S6TBY == True and S9TBY == True and S3T == False and DifficultyChoice >= 2) or (S5TBY == True and S7TBY == True and S3T == False and DifficultyChoice >= 2):
    Botgo = 3
   elif (S1TBY == True and S7TBY == True and S4T == False and DifficultyChoice >= 2) or (S5TBY == True and S6TBY == True and S4T == False and DifficultyChoice >= 2):
    Botgo = 4
   elif (S4TBY == True and S6TBY == True and S5T == False and DifficultyChoice >= 2) or (S2TBY == True and S8TBY == True and S5T == False and DifficultyChoice >= 2) or (S1TBY == True and S9TBY == True and S5T == False and DifficultyChoice >= 2) or (S3TBY == True and S7TBY == True and S5T == False and DifficultyChoice >= 2):
    Botgo = 5
   elif (S3TBY == True and S9TBY == True and S6T == False and DifficultyChoice >= 2) or (S4TBY == True and S5TBY == True and S6T == False and DifficultyChoice >= 2):
    Botgo = 6
   elif (S3TBY == True and S5TBY == True and S7T == False and DifficultyChoice >= 2) or (S1TBY == True and S4TBY == True and S7T == False and DifficultyChoice >= 2) or (S8TBY == True and S9TBY == True and S7T == False and DifficultyChoice >= 2):
    Botgo = 7
   elif (S7TBY == True and S9TBY == True and S8T == False and DifficultyChoice >= 2) or (S2TBY == True and S5TBY == True and S8T == False and DifficultyChoice >= 2):
    Botgo = 8
   elif (S1TBY == True and S5TBY == True and S9T == False and DifficultyChoice >= 2) or (S3TBY == True and S6TBY == True and S9T == False and DifficultyChoice >= 2) or (S7TBY == True and S8TBY == True and S9T == False and DifficultyChoice >= 2):
    Botgo = 9
   else:
    Botgo = random.randrange(1,10)
   if Botgo == 1:
    if S1T == False:
     Sd1 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Top-left.")
     S1T = True
     S1TBB = True
    elif S1T == True:
     continue
   elif Botgo == 2:
    if S2T == False:
     Sd2 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Top-middle.")
     S2T = True
     S2TBB = True
    elif S2T == True:
     continue
   elif Botgo == 3:
    if S3T == False:
     Sd3 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Top-right.")
     S3T = True
     S3TBB = True
    elif S3T == True:
     continue
   elif Botgo == 4:
    if S4T == False:
     Sd4 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Mid-left.")
     S4T = True
     S4TBB = True
    elif S4T == True:
     continue
   elif Botgo == 5:
    if S5T == False:
     Sd5 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Mid-middle.")
     S5T = True
     S5TBB = True
    elif S5T == True:
     continue
   elif Botgo == 6:
    if S6T == False:
     Sd6 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Mid-right.")
     S6T = True
     S6TBB = True
    elif S6T == True:
     continue
   elif Botgo == 7:
    if S7T == False:
     Sd7 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Bot-left.")
     S7T = True
     S7TBB = True
    elif S7T == True:
     continue
   elif Botgo == 8:
    if S8T == False:
     Sd8 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Bot-middle.")
     S8T = True
     S8TBB = True
    elif S8T == True:
     continue
   elif Botgo == 9:
    if S9T == False:
     Sd9 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("Your opponent chose to fill in Bot-right.")
     S9T = True
     S9TBB = True
    elif S9T == True:
     continue
   time.sleep(1)
   clearScreen()
   Botturn = False
   if (S1TBB == True and S2TBB == True and S3TBB == True) or (S1TBB == True and S5TBB == True and S9TBB == True) or (S1TBB == True and S4TBB == True and S7TBB == True) or (S2TBB == True and S5TBB == True and S8TBB == True) or (S3TBB == True and S6TBB == True and S9TBB == True) or (S3TBB == True and S5TBB == True and S7TBB == True) or (S4TBB == True and S5TBB == True and S6TBB == True) or (S7TBB == True and S8TBB == True and S9TBB == True):
    print(NewTicTacToeBoard)
    print("")
    print(Red+"Your opponent has made a cross."+reset)
    Botpoints = Botpoints + 1
    print("")
    MessageStop()
    Yourshape = 1
    Botshape = 2
    YourSd = "X"
    BotSd = "O"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False  
    S3TBY = False  
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False  
    S8TBY = False 
    S9TBY = False 
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False
   elif S1T == True and S2T == True and S3T == True and S4T == True and S5T == True and S6T == True and S7T == True and S8T == True and S9T == True:
    print(NewTicTacToeBoard)
    print("")
    print("Full Board!")
    print("")
    MessageStop()
    Yourshape = 1
    Botshape = 2
    YourSd = "X"
    BotSd = "O"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False  
    S3TBY = False  
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False  
    S8TBY = False 
    S9TBY = False 
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False
   Yourturn = True 
 if Yourpoints == 1 and DifficultyChoice == 1:
  return "EW"
 elif Yourpoints == 1 and DifficultyChoice == 2:
  return "MW"
 elif Yourpoints == 1 and DifficultyChoice == 3:
  return "HW"
 elif Botpoints == 1 and DifficultyChoice == 1:
  return "EL"
 elif Botpoints == 1 and DifficultyChoice == 2:
  return "ML"
 elif Botpoints == 1 and DifficultyChoice == 3:
  return "HL"
#Tic-Tac-Toe

def pvplevel9_function(PlayerOneName,PlayerTwoName):
 Yourpoints = 0
 Botpoints = 0
 Yourshape = 1
 Botshape = 2
 Sd1 = "_"
 Sd2 = "_"
 Sd3 = "_"
 Sd4 = "_"
 Sd5 = "_"
 Sd6 = "_"
 Sd7 = "_"
 Sd8 = "_"
 Sd9 = "_"
 S1T = False 
 S2T = False 
 S3T = False 
 S4T = False 
 S5T = False 
 S6T = False 
 S7T = False 
 S8T = False 
 S9T = False 
 S1TBY = False 
 S2TBY = False  
 S3TBY = False  
 S4TBY = False 
 S5TBY = False 
 S6TBY = False 
 S7TBY = False  
 S8TBY = False 
 S9TBY = False 
 S1TBB = False 
 S2TBB = False 
 S3TBB = False 
 S4TBB = False 
 S5TBB = False 
 S6TBB = False 
 S7TBB = False 
 S8TBB = False 
 S9TBB = False
 Scoreboardpvp = '''{0} - {1} pt(s). 

{2} - {3} pt(s).'''
 Explained = False
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
   clearScreen()
   print('''1 - On a 3x3 grid graph, you mark a spot.''') 
   MessageStop()
   print('''2 - The sign that you mark on the spot depends on the winner''')
   MessageStop()
   print('''3 - You mark a row on the 3x3 grid graph in order to win a point''')
   MessageStop()
   print('''4 - The goal for you and your opponent is to get 2 points''')
   MessageStop()
   print('''5 - You can stop your opponent from winning.
This is by stopping your opponent from marking a row on the graph.''')
   MessageStop()
   print('''6 - Strategy is key on this game.''')
   MessageStop()
   Explained = True
   continue
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   InvalidInput()
 TicTacToeBoard = '''{0} | {1} | {2}
----------
{3} | {4} | {5} 
----------
{6} | {7} | {8}'''
 while Yourpoints < 1 and Botpoints < 1: 
  if Yourshape == 1:
   YourSd = "X"
  elif Yourshape == 2:
   YourSd = "O"
  if Botshape == 1:
   BotSd = "X"
  elif Botshape == 2:
   BotSd = "O"
  Yourturn = True
  while Yourturn == True:
   print(TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9))
   print("It's {}'s turn!".format(PlayerOneName))
   time.sleep(0.5)
   print("")
   print("1 - Top-left",end = '       ')
   print("2 - Top-middle",end = '      ')
   print("3 - Top-right")
   time.sleep(0.25)
   print("")
   print("4 - Mid-left",end = '       ')
   print("5 - Mid-middle",end = '      ')
   print("6 - Mid-right")
   time.sleep(0.25)
   print("")
   print("7 - Bot-left",end = '       ')
   print("8 - Bot-middle",end = '      ')
   print("9 - Bot-right")
   time.sleep(0.25)
   print("")
   NumChoiceWithQuit()
   try:
    Yourgo = int(input(""))
    clearScreen()
   except:
    InvalidInput()
    continue
   Quitchoice = 0
   while Yourgo == 0:
    print("Are you sure you want to "+Red+"quit"+reset+"?")
    YesOrNo()
    try:
     Quitchoice = int(input(""))
    except:
     InvalidInput()
     continue
    if Quitchoice == 1:
     print("Understood.")
     time.sleep(1)
     print("")
     print("You will now return to the menu screen.")
     time.sleep(2)
     return "Quit"
    if Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
   if Quitchoice == 2:
     clearScreen()
     continue
   if Yourgo == 1:
    if S1T == False:
     Sd1 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Top-left.".format(PlayerOneName))
     S1TBY = True
     S1T = True
    elif S1T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 2:
    if S2T == False:
     Sd2 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Top-middle.".format(PlayerOneName))
     S2TBY = True
     S2T = True
    elif S2T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 3:
    if S3T == False:
     Sd3 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Top-right.".format(PlayerOneName))
     S3TBY = True
     S3T = True
    elif S3T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 4:
    if S4T == False:
     Sd4 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Mid-left.".format(PlayerOneName))
     S4TBY = True
     S4T = True
    elif S4T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 5:
    if S5T == False:
     Sd5 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Mid-middle.".format(PlayerOneName))
     S5TBY = True
     S5T = True
    elif S5T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 6:
    if S6T == False:
     Sd6 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Mid-right.".format(PlayerOneName))
     S6TBY = True
     S6T = True
    elif S6T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 7:
    if S7T == False:
     Sd7 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Bot-left.".format(PlayerOneName))
     S7TBY = True
     S7T = True
    elif S7T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 8:
    if S8T == False:
     Sd8 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Bot-middle.".format(PlayerOneName))
     S8TBY = True
     S8T = True
    elif S8T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   elif Yourgo == 9:
    if S9T == False:
     Sd9 = YourSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} to fill in Bot-right.".format(PlayerOneName))
     S9TBY = True
     S9T = True
    elif S9T == True:
     print(Red+"Spot is already filled."+reset)
     MessageStop()
     continue
   else:
    InvalidInput()
    continue
   time.sleep(1)
   clearScreen()
   Yourturn = False
   if (S1TBY == True and S2TBY == True and S3TBY == True) or (S1TBY == True and S5TBY == True and S9TBY == True) or (S1TBY == True and S4TBY == True and S7TBY == True) or (S2TBY == True and S5TBY == True and S8TBY == True) or (S3TBY == True and S6TBY == True and S9TBY == True) or (S3TBY == True and S5TBY == True and S7TBY == True) or (S4TBY == True and S5TBY == True and S6TBY == True) or (S7TBY == True and S8TBY == True and S9TBY == True):
    print(NewTicTacToeBoard)
    print("")
    print("{} ".format(PlayerOneName)+Blue+"has made a cross!"+reset)
    print("")
    Yourpoints = Yourpoints + 1
    MessageStop()
    Yourshape = 2
    Botshape = 1
    YourSd = "O"
    BotSd = "X"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False 
    S3TBY = False 
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False 
    S8TBY = False 
    S9TBY = False
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False 
   elif S1T == True and S2T == True and S3T == True and S4T == True and S5T == True and S6T == True and S7T == True and S8T == True and S9T == True:
    print(NewTicTacToeBoard)
    print("")
    print("Full Board!")
    print("")
    MessageStop()
    Yourshape = 2
    Botshape = 1
    YourSd = "O"
    BotSd = "X"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False  
    S3TBY = False  
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False  
    S8TBY = False 
    S9TBY = False 
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False
  Botturn = True
  while Botturn == True and Yourpoints != 1:
   print(TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9))
   print("It's {}'s turn!".format(PlayerTwoName))
   time.sleep(0.5)
   print("")
   print("1 - Top-left",end = '       ')
   print("2 - Top-middle",end = '      ')
   print("3 - Top-right")
   time.sleep(0.25)
   print("")
   print("4 - Mid-left",end = '       ')
   print("5 - Mid-middle",end = '      ')
   print("6 - Mid-right")
   time.sleep(0.25)
   print("")
   print("7 - Bot-left",end = '       ')
   print("8 - Bot-middle",end = '      ')
   print("9 - Bot-right")
   time.sleep(0.25)
   print("")
   NumChoiceWithQuit()
   try:
    Botgo = int(input(""))
    clearScreen()
   except:
    InvalidInput()
    continue
   Quitchoice = 0
   while Botgo == 0:
    print("Are you sure you want to "+Red+"quit"+reset+"?")
    YesOrNo()
    try:
     Quitchoice = int(input(""))
    except:
     InvalidInput()
     continue
    if Quitchoice == 1:
     print("Understood.")
     time.sleep(1)
     print("")
     print("You will now return to the menu screen.")
     time.sleep(2)
     return "Quit"
    if Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
   if Quitchoice == 2:
     clearScreen()
     continue
   if Botgo == 1:
    if S1T == False:
     Sd1 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Top-left.".format(PlayerTwoName))
     S1T = True
     S1TBB = True
    elif S1T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 2:
    if S2T == False:
     Sd2 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Top-middle.".format(PlayerTwoName))
     S2T = True
     S2TBB = True
    elif S2T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 3:
    if S3T == False:
     Sd3 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Top-right.".format(PlayerTwoName))
     S3T = True
     S3TBB = True
    elif S3T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 4:
    if S4T == False:
     Sd4 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Mid-left.".format(PlayerTwoName))
     S4T = True
     S4TBB = True
    elif S4T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 5:
    if S5T == False:
     Sd5 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Mid-middle.".format(PlayerTwoName))
     S5T = True
     S5TBB = True
    elif S5T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 6:
    if S6T == False:
     Sd6 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Mid-right.".format(PlayerTwoName))
     S6T = True
     S6TBB = True
    elif S6T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 7:
    if S7T == False:
     Sd7 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Bot-left.".format(PlayerTwoName))
     S7T = True
     S7TBB = True
    elif S7T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 8:
    if S8T == False:
     Sd8 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Bot-middle.".format(PlayerTwoName))
     S8T = True
     S8TBB = True
    elif S8T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   elif Botgo == 9:
    if S9T == False:
     Sd9 = BotSd
     NewTicTacToeBoard = TicTacToeBoard.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9)
     print(NewTicTacToeBoard)
     print("{} chose to fill in Bot-right.".format(PlayerTwoName))
     S9T = True
     S9TBB = True
    elif S9T == True:
     print(Red+"Spot is already filled."+reset)
     continue
   time.sleep(1)
   clearScreen()
   Botturn = False
   if (S1TBB == True and S2TBB == True and S3TBB == True) or (S1TBB == True and S5TBB == True and S9TBB == True) or (S1TBB == True and S4TBB == True and S7TBB == True) or (S2TBB == True and S5TBB == True and S8TBB == True) or (S3TBB == True and S6TBB == True and S9TBB == True) or (S3TBB == True and S5TBB == True and S7TBB == True) or (S4TBB == True and S5TBB == True and S6TBB == True) or (S7TBB == True and S8TBB == True and S9TBB == True):
    print(NewTicTacToeBoard)
    print("")
    print("{} ".format(PlayerTwoName)+Blue+"has made a cross!"+reset)
    Botpoints = Botpoints + 1
    print("")
    MessageStop()
    Yourshape = 1
    Botshape = 2
    YourSd = "X"
    BotSd = "O"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False  
    S3TBY = False  
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False  
    S8TBY = False 
    S9TBY = False 
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False
   elif S1T == True and S2T == True and S3T == True and S4T == True and S5T == True and S6T == True and S7T == True and S8T == True and S9T == True:
    print(NewTicTacToeBoard)
    print("")
    print("Full Board!")
    print("")
    MessageStop()
    Yourshape = 1
    Botshape = 2
    YourSd = "X"
    BotSd = "O"
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    S1T = False 
    S2T = False 
    S3T = False 
    S4T = False 
    S5T = False 
    S6T = False 
    S7T = False 
    S8T = False 
    S9T = False 
    S1TBY = False 
    S2TBY = False  
    S3TBY = False  
    S4TBY = False 
    S5TBY = False 
    S6TBY = False 
    S7TBY = False  
    S8TBY = False 
    S9TBY = False 
    S1TBB = False 
    S2TBB = False 
    S3TBB = False 
    S4TBB = False 
    S5TBB = False 
    S6TBB = False 
    S7TBB = False 
    S8TBB = False 
    S9TBB = False
   Yourturn = True 
 if Yourpoints == 1:
  return "W"
 elif Botpoints == 1:
  return "L"
#Tic-Tac-Toe