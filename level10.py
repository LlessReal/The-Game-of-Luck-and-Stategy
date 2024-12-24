import random
import time
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
def PNTC_function(): 
 print(yellow + '''
(Press a number and then Enter to choose)''' + reset)
def PNTCOQ_function(): 
 print(yellow + '''
(Press a number and then Enter to choose. '''+reset+red+'''Press 0 to '''+reset+Red+'''quit.'''+reset+yellow+''')'''+reset)
def II_function():
 clearScreen()
 print(Red + "Invalid Input" + reset)
 time.sleep(1)
 print('''You must press the number on the left.
Then, you press enter to choose.''')
 PETC_function()
def YOR_function():
 time.sleep(0.5)
 print('''
1 - '''+Blue+'''Yes'''+reset)
 time.sleep(0.25)
 print('''
2 - '''+Red+'''No'''+reset)
 time.sleep(0.25)
 PNTC_function()

def level10_function():
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
 Sd10 = "_"
 Sd11 = "_"
 Sd12 = "_"
 Sd13 = "_"
 Sd14 = "_"
 Sd15 = "_"
 Sd16 = "_"
 Sd17 = "_"
 Sd18 = "_"
 Sd19 = "_"
 Sd20 = "_"
 Sd21 = "_"
 Sd22 = "_"
 Sd23 = "_"
 Sd24 = "_"
 Sd25 = "_"
 Sd26 = "_"
 Sd27 = "_"
 Sd28 = "_"
 Sd29 = "_"
 Sd30 = "_"
 Sd31 = "_"
 Sd32 = "_"
 Sd33 = "_"
 Sd34 = "_"
 Sd35 = "_"
 Sd36 = "_"
 Sd37 = "_"
 Sd38 = "_"
 Sd39 = "_"
 Sd40 = "_"
 Sd41 = "_"
 Sd42 = "_"
 R1Clmn1T = False 
 R1Clmn2T = False 
 R1Clmn3T = False 
 R1Clmn4T = False 
 R1Clmn5T = False 
 R1Clmn6T = False 
 R1Clmn7T = False 
 R2Clmn1T = False 
 R2Clmn2T = False 
 R2Clmn3T = False 
 R2Clmn4T = False 
 R2Clmn5T = False 
 R2Clmn6T = False 
 R2Clmn7T = False 
 R3Clmn1T = False 
 R3Clmn2T = False 
 R3Clmn3T = False 
 R3Clmn4T = False 
 R3Clmn5T = False 
 R3Clmn6T = False 
 R3Clmn7T = False 
 R4Clmn1T = False 
 R4Clmn2T = False 
 R4Clmn3T = False 
 R4Clmn4T = False 
 R4Clmn5T = False 
 R4Clmn6T = False 
 R4Clmn7T = False 
 R5Clmn1T = False 
 R5Clmn2T = False 
 R5Clmn3T = False 
 R5Clmn4T = False 
 R5Clmn5T = False 
 R5Clmn6T = False 
 R5Clmn7T = False 
 R6Clmn1T = False 
 R6Clmn2T = False 
 R6Clmn3T = False 
 R6Clmn4T = False 
 R6Clmn5T = False 
 R6Clmn6T = False 
 R6Clmn7T = False 
 R1Clmn1TBY = False 
 R1Clmn2TBY = False 
 R1Clmn3TBY = False 
 R1Clmn4TBY = False 
 R1Clmn5TBY = False 
 R1Clmn6TBY = False 
 R1Clmn7TBY = False 
 R2Clmn1TBY = False 
 R2Clmn2TBY = False 
 R2Clmn3TBY = False 
 R2Clmn4TBY = False 
 R2Clmn5TBY = False 
 R2Clmn6TBY = False 
 R2Clmn7TBY = False 
 R3Clmn1TBY = False 
 R3Clmn2TBY = False 
 R3Clmn3TBY = False 
 R3Clmn4TBY = False 
 R3Clmn5TBY = False 
 R3Clmn6TBY = False 
 R3Clmn7TBY = False 
 R4Clmn1TBY = False 
 R4Clmn2TBY = False 
 R4Clmn3TBY = False 
 R4Clmn4TBY = False 
 R4Clmn5TBY = False 
 R4Clmn6TBY = False 
 R4Clmn7TBY = False 
 R5Clmn1TBY = False 
 R5Clmn2TBY = False 
 R5Clmn3TBY = False 
 R5Clmn4TBY = False 
 R5Clmn5TBY = False 
 R5Clmn6TBY = False 
 R5Clmn7TBY = False 
 R6Clmn1TBY = False 
 R6Clmn2TBY = False 
 R6Clmn3TBY = False 
 R6Clmn4TBY = False 
 R6Clmn5TBY = False 
 R6Clmn6TBY = False
 R6Clmn7TBY = False 
 R1Clmn1TBB = False 
 R1Clmn2TBB = False 
 R1Clmn3TBB = False 
 R1Clmn4TBB = False 
 R1Clmn5TBB = False 
 R1Clmn6TBB = False 
 R1Clmn7TBB = False 
 R2Clmn1TBB = False 
 R2Clmn2TBB = False 
 R2Clmn3TBB = False 
 R2Clmn4TBB = False 
 R2Clmn5TBB = False 
 R2Clmn6TBB = False 
 R2Clmn7TBB = False 
 R3Clmn1TBB = False 
 R3Clmn2TBB = False 
 R3Clmn3TBB = False 
 R3Clmn4TBB = False 
 R3Clmn5TBB = False 
 R3Clmn6TBB = False 
 R3Clmn7TBB = False 
 R4Clmn1TBB = False 
 R4Clmn2TBB = False 
 R4Clmn3TBB = False 
 R4Clmn4TBB = False 
 R4Clmn5TBB = False 
 R4Clmn6TBB = False 
 R4Clmn7TBB = False 
 R5Clmn1TBB = False 
 R5Clmn2TBB = False 
 R5Clmn3TBB = False 
 R5Clmn4TBB = False 
 R5Clmn5TBB = False 
 R5Clmn6TBB = False 
 R5Clmn7TBB = False 
 R6Clmn1TBB = False 
 R6Clmn2TBB = False 
 R6Clmn3TBB = False 
 R6Clmn4TBB = False 
 R6Clmn5TBB = False 
 R6Clmn6TBB = False 
 R6Clmn7TBB = False 
 while True:
  print('''
Choose your difficulty for Connect FOUR:''')
  time.sleep(0.5)
  print('''
1 - ''' + Blue + '''Easy (Bot has no brain)''' + reset)
  time.sleep(0.25)
  print('''
2 - ''' + yellow + '''Medium (Bot has brain) ''' + reset)
  time.sleep(0.25)
  print('''
3 - ''' + Red + '''Hard (Bot has big brain) ''' + reset)
  time.sleep(0.25)
  PNTC_function()
  try:
   DifficultyChoice = int(input(""))
  except:
   II_function()
   continue
  if DifficultyChoice == 1:
     print("Alright! Easy difficulty of Connect FOUR loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 2:
     print("Alright! Medium difficulty Connect FOUR loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 3:
     print("Alright! Hard difficulty Connect FOUR loading!")
     time.sleep(1.5)
     clearScreen()
     break
  else:
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
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   II_function()
 Connect4Board = '''6 | {35} | {36} | {37} | {38} | {39} | {40} | {41}
 -----------------------------
5 | {28} | {29} | {30} | {31} | {32} | {33} | {34}
 -----------------------------
4 | {21} | {22} | {23} | {24} | {25} | {26} | {27}
 -----------------------------
3 | {14} | {15} | {16} | {17} | {18} | {19} | {20}
 -----------------------------
2 | {7} | {8} | {9} | {10} | {11} | {12} | {13}
 -----------------------------
1 | {0} | {1} | {2} | {3} | {4} | {5} | {6}
    1 | 2 | 3 | 4 | 5 | 6 | 7'''
 while Yourpoints < 1 and Botpoints < 1: 
  if Yourshape == 1:
   YourSd = Red+"O"+reset
  elif Yourshape == 2:
   YourSd = Blue+"O"+reset
  if Botshape == 1:
   BotSd = Red+"O"+reset
  elif Botshape == 2:
   BotSd = Blue+"O"+reset
  Yourturn = True
  while Yourturn == True:
   print(Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42))
   print("It's your turn! Choose your Column")
   time.sleep(0.25)
   print("1 - 1st Column",end = '   ')
   print("2 - 2nd Column",end = '   ')
   print("3 - 3rd Column",end = '   ')
   print("4 - 4th Column")
   time.sleep(0.25)
   print("")
   print("5 - 5th Column",end = '   ')
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
   if Yourgo == 1:
    if R1Clmn1T == False:
     Sd1 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 1")
     R1Clmn1TBY = True
     R1Clmn1T = True
     time.sleep(1)
    elif R1Clmn1T == True:
     if R2Clmn1T == False:
      Sd8 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 1")
      R2Clmn1TBY = True
      R2Clmn1T = True
      time.sleep(1)
     elif R2Clmn1T == True:
      if R3Clmn1T == False:
       Sd15 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 1")
       R3Clmn1TBY = True
       R3Clmn1T = True
       time.sleep(1)
      elif R3Clmn1T == True:
       if R4Clmn1T == False:
        Sd22 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 1")
        R4Clmn1TBY = True
        R4Clmn1T = True
        time.sleep(1)
       elif R4Clmn1T == True:
        if R5Clmn1T == False:
         Sd29 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 1")
         R5Clmn1TBY = True
         R5Clmn1T = True
         time.sleep(1)
        elif R5Clmn1T == True:
         if R6Clmn1T == False:
          Sd36 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 1")
          R6Clmn1TBY = True
          R6Clmn1T = True
          time.sleep(1)
         elif R6Clmn1T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   elif Yourgo == 2:
    if R1Clmn2T == False:
     Sd2 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 2")
     R1Clmn2TBY = True
     R1Clmn2T = True
     time.sleep(1)
    elif R1Clmn2T == True:
     if R2Clmn2T == False:
      Sd9 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 2")
      R2Clmn2TBY = True
      R2Clmn2T = True
      time.sleep(1)
     elif R2Clmn2T == True:
      if R3Clmn2T == False:
       Sd16 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 2")
       R3Clmn2TBY = True
       R3Clmn2T = True
       time.sleep(1)
      elif R3Clmn2T == True:
       if R4Clmn2T == False:
        Sd23 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 2")
        R4Clmn2TBY = True
        R4Clmn2T = True
        time.sleep(1)
       elif R4Clmn2T == True:
        if R5Clmn2T == False:
         Sd30 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 2")
         R5Clmn2TBY = True
         R5Clmn2T = True
         time.sleep(1)
        elif R5Clmn2T == True:
         if R6Clmn2T == False:
          Sd37 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 2")
          R6Clmn2TBY = True
          R6Clmn2T = True
          time.sleep(1)
         elif R6Clmn2T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   elif Yourgo == 3:
    if R1Clmn3T == False:
     Sd3 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 3")
     R1Clmn3TBY = True
     R1Clmn3T = True
     time.sleep(1)
    elif R1Clmn3T == True:
     if R2Clmn3T == False:
      Sd10 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 3")
      R2Clmn3TBY = True
      R2Clmn3T = True
      time.sleep(1)
     elif R2Clmn3T == True:
      if R3Clmn3T == False:
       Sd17 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 3")
       R3Clmn3TBY = True
       R3Clmn3T = True
       time.sleep(1)
      elif R3Clmn3T == True:
       if R4Clmn3T == False:
        Sd24 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 3")
        R4Clmn3TBY = True
        R4Clmn3T = True
        time.sleep(1)
       elif R4Clmn3T == True:
        if R5Clmn3T == False:
         Sd31 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 3")
         R5Clmn3TBY = True
         R5Clmn3T = True
         time.sleep(1)
        elif R5Clmn3T == True:
         if R6Clmn3T == False:
          Sd38 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 3")
          R6Clmn3TBY = True
          R6Clmn3T = True
          time.sleep(1)
         elif R6Clmn3T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   elif Yourgo == 4:
    if R1Clmn4T == False:
     Sd4 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 4")
     R1Clmn4TBY = True
     R1Clmn4T = True
     time.sleep(1)
    elif R1Clmn4T == True:
     if R2Clmn4T == False:
      Sd11 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 4")
      R2Clmn4TBY = True
      R2Clmn4T = True
      time.sleep(1)
     elif R2Clmn4T == True:
      if R3Clmn4T == False:
       Sd18 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 4")
       R3Clmn4TBY = True
       R3Clmn4T = True
       time.sleep(1)
      elif R3Clmn4T == True:
       if R4Clmn4T == False:
        Sd25 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 4")
        R4Clmn4TBY = True
        R4Clmn4T = True
        time.sleep(1)
       elif R4Clmn4T == True:
        if R5Clmn4T == False:
         Sd32 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 4")
         R5Clmn4TBY = True
         R5Clmn4T = True
         time.sleep(1)
        elif R5Clmn4T == True:
         if R6Clmn4T == False:
          Sd39 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 4")
          R6Clmn4TBY = True
          R6Clmn4T = True
          time.sleep(1)
         elif R6Clmn4T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   elif Yourgo == 5:
    if R1Clmn5T == False:
     Sd5 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 5")
     R1Clmn5TBY = True
     R1Clmn5T = True
     time.sleep(1)
    elif R1Clmn5T == True:
     if R2Clmn5T == False:
      Sd12 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 5")
      R2Clmn5TBY = True
      R2Clmn5T = True
      time.sleep(1)
     elif R2Clmn5T == True:
      if R3Clmn5T == False:
       Sd19 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 5")
       R3Clmn5TBY = True
       R3Clmn5T = True
       time.sleep(1)
      elif R3Clmn5T == True:
       if R4Clmn5T == False:
        Sd26 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 5")
        R4Clmn5TBY = True
        R4Clmn5T = True
        time.sleep(1)
       elif R4Clmn5T == True:
        if R5Clmn5T == False:
         Sd33 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 5")
         R5Clmn5TBY = True
         R5Clmn5T = True
         time.sleep(1)
        elif R5Clmn5T == True:
         if R6Clmn5T == False:
          Sd40 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 5")
          R6Clmn5TBY = True
          R6Clmn5T = True
          time.sleep(1)
         elif R6Clmn5T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   elif Yourgo == 6:
    if R1Clmn6T == False:
     Sd6 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 6")
     R1Clmn6TBY = True
     R1Clmn6T = True
     time.sleep(1)
    elif R1Clmn6T == True:
     if R2Clmn6T == False:
      Sd13 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 6")
      R2Clmn6TBY = True
      R2Clmn6T = True
      time.sleep(1)
     elif R2Clmn6T == True:
      if R3Clmn6T == False:
       Sd20 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 6")
       R3Clmn6TBY = True
       R3Clmn6T = True
       time.sleep(1)
      elif R3Clmn6T == True:
       if R4Clmn6T == False:
        Sd27 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 6")
        R4Clmn6TBY = True
        R4Clmn6T = True
        time.sleep(1)
       elif R4Clmn6T == True:
        if R5Clmn6T == False:
         Sd34 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 6")
         R5Clmn6TBY = True
         R5Clmn6T = True
         time.sleep(1)
        elif R5Clmn6T == True:
         if R6Clmn6T == False:
          Sd41 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 6")
          R6Clmn6TBY = True
          R6Clmn6T = True
          time.sleep(1)
         elif R6Clmn6T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   elif Yourgo == 7:
    if R1Clmn7T == False:
     Sd7 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("You chose to fill in Row 1, Column 7")
     R1Clmn7TBY = True
     R1Clmn7T = True
     time.sleep(1)
    elif R1Clmn7T == True:
     if R2Clmn7T == False:
      Sd14 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("You chose to fill in Row 2, Column 7")
      R2Clmn7TBY = True
      R2Clmn7T = True
      time.sleep(1)
     elif R2Clmn7T == True:
      if R3Clmn7T == False:
       Sd21 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("You chose to fill in Row 3, Column 7")
       R3Clmn7TBY = True
       R3Clmn7T = True
       time.sleep(1)
      elif R3Clmn7T == True:
       if R4Clmn7T == False:
        Sd28 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("You chose to fill in Row 4, Column 7")
        R4Clmn7TBY = True
        R4Clmn7T = True
        time.sleep(1)
       elif R4Clmn7T == True:
        if R5Clmn7T == False:
         Sd35 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("You chose to fill in Row 5, Column 7")
         R5Clmn7TBY = True
         R5Clmn7T = True
         time.sleep(1)
        elif R5Clmn7T == True:
         if R6Clmn7T == False:
          Sd42 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("You chose to fill in Row 6, Column 7")
          R6Clmn7TBY = True
          R6Clmn7T = True
          time.sleep(1)
         elif R6Clmn7T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   else:
    II_function()
    continue
   clearScreen()
   if (R1Clmn1TBY == True and R2Clmn1TBY == True and R3Clmn1TBY == True and R4Clmn1TBY == True) or (R1Clmn1TBY == True and R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True) or (R1Clmn1TBY == True and R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4TBY == True) or (R1Clmn2TBY == True and R2Clmn2TBY == True and R3Clmn2TBY == True and R4Clmn2TBY == True) or (R1Clmn2TBY == True and R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True) or (R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5TBY == True) or (R1Clmn3TBY == True and R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3TBY == True) or (R1Clmn3TBY == True and R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True) or (R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5TBY == True and R1Clmn6TBY == True) or (R1Clmn4TBY == True and R2Clmn3TBY == True and R3Clmn2TBY == True and R4Clmn1TBY == True) or (R1Clmn4TBY == True and R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4TBY == True) or (R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2TBY == True and R1Clmn1TBY == True) or (R1Clmn5TBY == True and R2Clmn4TBY == True and R3Clmn3TBY == True and R4Clmn2TBY == True) or (R1Clmn5TBY == True and R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5TBY == True) or (R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2TBY == True) or (R1Clmn6TBY == True and R2Clmn5TBY == True and R3Clmn4TBY == True and R4Clmn3TBY == True) or (R1Clmn6TBY == True and R2Clmn6TBY == True and R3Clmn6TBY == True and R4Clmn6TBY == True) or (R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3TBY == True) or (R1Clmn7TBY == True and R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn7TBY == True and R3Clmn7TBY == True and R4Clmn7TBY == True) or (R2Clmn1TBY == True and R3Clmn1TBY == True and R4Clmn1TBY == True and R5Clmn1TBY == True) or (R2Clmn1TBY == True and R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True) or (R2Clmn1TBY == True and R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True) or (R2Clmn2TBY == True and R3Clmn2TBY == True and R4Clmn2TBY == True and R5Clmn2TBY == True) or (R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True) or (R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3TBY == True and R5Clmn3TBY == True) or (R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True) or (R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True) or (R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4TBY == True and R5Clmn4TBY == True) or (R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True and R2Clmn7TBY == True) or (R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True and R5Clmn7TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True) or (R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True) or (R2Clmn6TBY == True and R3Clmn6TBY == True and R4Clmn6TBY == True and R5Clmn6TBY == True) or (R2Clmn7TBY == True and R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True) or (R2Clmn7TBY == True and R3Clmn7TBY == True and R4Clmn7TBY == True and R5Clmn7TBY == True) or (R2Clmn7TBY == True and R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True) or (R3Clmn1TBY == True and R4Clmn1TBY == True and R5Clmn1TBY == True and R6Clmn1TBY == True) or (R3Clmn1TBY == True and R4Clmn2TBY == True and R5Clmn3TBY == True and R6Clmn4TBY == True) or (R3Clmn1TBY == True and R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True) or (R3Clmn2TBY == True and R4Clmn2TBY == True and R5Clmn2TBY == True and R6Clmn2TBY == True) or (R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True and R6Clmn5TBY == True) or (R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True) or (R3Clmn3TBY == True and R4Clmn3TBY == True and R5Clmn3TBY == True and R6Clmn3TBY == True) or (R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True and R6Clmn6TBY == True) or (R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True) or (R3Clmn4TBY == True and R4Clmn4TBY == True and R5Clmn4TBY == True and R6Clmn4TBY == True) or (R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True and R3Clmn7TBY == True) or (R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True and R6Clmn7TBY == True) or (R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True and R3Clmn2TBY == True) or (R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5TBY == True and R6Clmn5TBY == True) or (R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True and R6Clmn2TBY == True) or (R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True and R6Clmn3TBY == True) or (R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True) or (R3Clmn6TBY == True and R4Clmn6TBY == True and R5Clmn6TBY == True and R6Clmn6TBY == True) or (R3Clmn7TBY == True and R4Clmn6TBY == True and R5Clmn5TBY == True and R6Clmn4TBY == True) or (R3Clmn7TBY == True and R4Clmn7TBY == True and R5Clmn7TBY == True and R6Clmn7TBY == True) or (R3Clmn7TBY == True and R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True) or (R4Clmn1TBY == True and R3Clmn1TBY == True and R2Clmn1TBY == True and R1Clmn1TBY == True) or (R4Clmn1TBY == True and R3Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4TBY == True) or (R4Clmn1TBY == True and R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True) or (R4Clmn2TBY == True and R3Clmn2TBY == True and R2Clmn2TBY == True and R1Clmn2TBY == True) or (R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5TBY == True) or (R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True) or (R4Clmn3TBY == True and R3Clmn3TBY == True and R2Clmn3TBY == True and R1Clmn3TBY == True) or (R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6TBY == True) or (R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True) or (R4Clmn4TBY == True and R3Clmn4TBY == True and R2Clmn4TBY == True and R1Clmn4TBY == True) or (R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True and R4Clmn7TBY == True) or (R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True and R1Clmn7TBY == True) or (R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True and R4Clmn2TBY == True) or (R4Clmn5TBY == True and R3Clmn5TBY == True and R2Clmn5TBY == True and R1Clmn5TBY == True) or (R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2TBY == True) or (R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3TBY == True) or (R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True) or (R4Clmn6TBY == True and R3Clmn6TBY == True and R2Clmn6TBY == True and R1Clmn6TBY == True) or (R4Clmn7TBY == True and R3Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4TBY == True) or (R4Clmn7TBY == True and R3Clmn7TBY == True and R2Clmn7TBY == True and R1Clmn7TBY == True) or (R4Clmn7TBY == True and R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True) or (R5Clmn1TBY == True and R4Clmn1TBY == True and R3Clmn1TBY == True and R2Clmn1TBY == True) or (R5Clmn1TBY == True and R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True) or (R5Clmn1TBY == True and R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True) or (R5Clmn2TBY == True and R4Clmn2TBY == True and R3Clmn2TBY == True and R2Clmn2TBY == True) or (R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True) or (R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True) or (R5Clmn3TBY == True and R4Clmn3TBY == True and R3Clmn3TBY == True and R2Clmn3TBY == True) or (R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True) or (R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True) or (R5Clmn4TBY == True and R4Clmn4TBY == True and R3Clmn4TBY == True and R2Clmn4TBY == True) or (R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True and R5Clmn7TBY == True) or (R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True and R2Clmn7TBY == True) or (R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True and R5Clmn2TBY == True) or (R5Clmn5TBY == True and R4Clmn5TBY == True and R3Clmn5TBY == True and R2Clmn5TBY == True) or (R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True and R2Clmn2TBY == True) or (R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True) or (R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True) or (R5Clmn6TBY == True and R4Clmn6TBY == True and R3Clmn6TBY == True and R2Clmn6TBY == True) or (R5Clmn7TBY == True and R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True) or (R5Clmn7TBY == True and R4Clmn7TBY == True and R3Clmn7TBY == True and R2Clmn7TBY == True) or (R5Clmn7TBY == True and R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True) or (R6Clmn1TBY == True and R5Clmn1TBY == True and R4Clmn1TBY == True and R3Clmn1TBY == True) or (R6Clmn1TBY == True and R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True) or (R6Clmn1TBY == True and R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True) or (R6Clmn2TBY == True and R5Clmn2TBY == True and R4Clmn2TBY == True and R3Clmn2TBY == True) or (R6Clmn2TBY == True and R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True) or (R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True) or (R6Clmn3TBY == True and R5Clmn3TBY == True and R4Clmn3TBY == True and R3Clmn3TBY == True) or (R6Clmn3TBY == True and R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True) or (R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True) or (R6Clmn4TBY == True and R5Clmn4TBY == True and R4Clmn4TBY == True and R3Clmn4TBY == True) or (R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True and R6Clmn7TBY == True) or (R6Clmn4TBY == True and R5Clmn5TBY == True and R4Clmn6TBY == True and R3Clmn7TBY == True) or (R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True and R6Clmn2TBY == True) or (R6Clmn5TBY == True and R5Clmn5TBY == True and R4Clmn5TBY == True and R3Clmn5TBY == True) or (R6Clmn5TBY == True and R5Clmn4TBY == True and R4Clmn3TBY == True and R3Clmn2TBY == True) or (R6Clmn6TBY == True and R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True) or (R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True) or (R6Clmn6TBY == True and R5Clmn6TBY == True and R4Clmn6TBY == True and R3Clmn6TBY == True) or (R6Clmn7TBY == True and R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True) or (R6Clmn7TBY == True and R5Clmn7TBY == True and R4Clmn7TBY == True and R3Clmn7TBY == True) or (R6Clmn7TBY == True and R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True):  
    print(NewConnect4Board)
    print("")
    print(Blue+"You have connected four!"+reset)
    print("")
    Yourpoints = Yourpoints + 1
    PETC_function()
    Yourshape = 2
    Botshape = 1
    YourSd = Blue+"O"+reset
    BotSd = Red+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   elif R1Clmn1T == True and R1Clmn2T == True and R1Clmn3T == True and R1Clmn4T == True and R1Clmn5T == True and R1Clmn6T == True and R1Clmn7T == True and R2Clmn1T == True and R2Clmn2T == True and  R2Clmn3T == True and R2Clmn4T == True and R2Clmn5T == True and R2Clmn6T == True and R2Clmn7T == True and R3Clmn1T == True and R3Clmn2T == True and R3Clmn3T == True and R3Clmn4T == True and R3Clmn5T == True and R3Clmn6T == True and R3Clmn7T == True and R4Clmn1T == True and R4Clmn2T == True and R4Clmn3T == True and R4Clmn4T == True and R4Clmn5T == True and R4Clmn6T == True and R4Clmn7T == True and R5Clmn1T == True and R5Clmn2T == True and R5Clmn3T == True and R5Clmn4T == True and R5Clmn5T == True and R5Clmn6T == True and R5Clmn7T == True and R6Clmn1T == True and R6Clmn2T == True and R6Clmn3T == True and R6Clmn4T == True and R6Clmn5T == True and R6Clmn6T == True and R6Clmn7T == True:
    print(NewConnect4Board)
    print("")
    print("DRAW!")
    print("")
    PETC_function()
    Yourshape = 2
    Botshape = 1
    YourSd = Blue+"O"+reset
    BotSd = Red+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   Yourturn = False
  NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
  Botturn = True
  while Botturn == True and Yourpoints != 1:
   if (R6Clmn1T == False and R5Clmn1T == True and R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4TBB == True) or (R6Clmn1T == False and R5Clmn1T == True and R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4TBB == True) or (R5Clmn1T == False and R4Clmn1T == True and R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4TBB == True) or (R5Clmn1T == False and R4Clmn1T == True and R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4TBB == True) or (R4Clmn1T == False and R3Clmn1T == True and R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4TBB == True) or (R4Clmn1T == False and R3Clmn1T == True and R3Clmn2TBB == True and R2Clmn3TBB == True and R1Clmn4TBB == True) or (R3Clmn1T == False and R2Clmn1T == True and R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4TBB == True) or (R3Clmn1T == False and R2Clmn1T == True and R4Clmn2TBB == True and R5Clmn3TBB == True and R6Clmn4TBB == True) or (R2Clmn1T == False and R1Clmn1T == True and R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4TBB == True) or (R2Clmn1T == False and R1Clmn1T == True and R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4TBB == True) or (R1Clmn1T == False and R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4TBB == True) or (R1Clmn1T == False and R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4TBB == True) or (R2Clmn1TBB == True and R3Clmn1TBB == True and R4Clmn1TBB == True and R5Clmn1T == False and R4Clmn1T == True) or (R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2TBB == True and R1Clmn1T == False) or (R1Clmn4TBB == True and R2Clmn3TBB == True and R3Clmn2TBB == True and R4Clmn1T == False and R3Clmn1T == True) or (R1Clmn1TBB == True and R2Clmn1TBB == True and R3Clmn1TBB == True and R4Clmn1T == False and R3Clmn1T == True) or (R3Clmn1TBB == True and R4Clmn1TBB == True and R5Clmn1TBB == True and R6Clmn1T == False and R5Clmn1T == True) and DifficultyChoice == 3: 
    Botgo = 1
   elif (R6Clmn2T == False and R5Clmn2T == True and R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5TBB == True) or (R6Clmn2T == False and R5Clmn2T == True and R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5TBB == True) or (R5Clmn2T == False and R4Clmn2T == True and R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5TBB == True) or (R5Clmn2T == False and R4Clmn2T == True and R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5TBB == True) or (R1Clmn2TBB == True and R2Clmn2TBB == True and R3Clmn2TBB == True and R4Clmn2T == False and R3Clmn2T == True) or (R1Clmn5TBB == True and R2Clmn4TBB == True and R3Clmn3TBB == True and R4Clmn2T == False and R3Clmn2T == True) or (R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2T == False) or (R2Clmn2TBB == True and R3Clmn2TBB == True and R4Clmn2TBB == True and R5Clmn2T == False and R4Clmn2T == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2T == False and R1Clmn2T == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2T == False and R1Clmn2T == True) or (R3Clmn2TBB == True and R4Clmn2TBB == True and R5Clmn2TBB == True and R6Clmn2T == False and R5Clmn2T == True) or (R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3TBB == True and R3Clmn2T == False and R2Clmn2T == True) or (R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3TBB == True and R6Clmn2T == False and R5Clmn2T == True) or (R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3TBB == True and R4Clmn2T == False and R3Clmn2T == True) or (R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3TBB == True and R1Clmn2T == False) or (R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3TBB == True and R5Clmn2T == False and R4Clmn2T == True) or (R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3TBB == True and R2Clmn2T == False and R1Clmn2T == True) or (R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3TBB == True and R6Clmn2T == False and R5Clmn2T == True) or (R6Clmn5TBB == True and R5Clmn4TBB == True and R4Clmn3TBB == True and R3Clmn2T == False and R2Clmn2T == True) or (R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2T == False and R1Clmn1TBB == True) or (R1Clmn4TBB == True and R2Clmn3TBB == True and R3Clmn2T == False and R2Clmn2T == True and R4Clmn1TBB == True) or (R1Clmn1TBB == True and R2Clmn2T == False and R1Clmn2T == True and R3Clmn3TBB == True and R4Clmn4TBB == True) or (R1Clmn1TBB == True and R1Clmn2T == False and R1Clmn3TBB == True and R1Clmn4TBB == True) or (R2Clmn1TBB == True and R3Clmn2T == False and R2Clmn2T == True and R4Clmn3TBB == True and R5Clmn4TBB == True) or (R2Clmn1TBB == True and R2Clmn2T == False and R1Clmn2T == True and R2Clmn3TBB == True and R2Clmn4TBB == True) or (R3Clmn1TBB == True and R4Clmn2T == False and R3Clmn2T == True and R5Clmn3TBB == True and R6Clmn4TBB == True) or (R3Clmn1TBB == True and R3Clmn2T == False and R2Clmn2T == True and R3Clmn3TBB == True and R3Clmn4TBB == True) or (R4Clmn1TBB == True and R3Clmn2T == False and R2Clmn2T == True and R2Clmn3TBB == True and R1Clmn4TBB == True) or (R4Clmn1TBB == True and R4Clmn2T == False and R3Clmn2T == True and R4Clmn3TBB == True and R4Clmn4TBB == True) or (R5Clmn1TBB == True and R4Clmn2T == False and R3Clmn2T == True and R3Clmn3TBB == True and R2Clmn4TBB == True) or (R5Clmn1TBB == True and R5Clmn2T == False and R4Clmn2T == True and R5Clmn3TBB == True and R5Clmn4TBB == True) or (R6Clmn1TBB == True and R5Clmn2T == False and R4Clmn2T == True and R4Clmn3TBB == True and R3Clmn4TBB == True) or (R6Clmn1TBB == True and R6Clmn2T == False and R5Clmn2T == True and R6Clmn3TBB == True and R6Clmn4TBB == True) or (R1Clmn2T == False and R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5TBB == True) or (R1Clmn2T == False and R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5TBB == True) or (R2Clmn2T == False and R1Clmn2T == True and R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5TBB == True) or (R2Clmn2T == False and R1Clmn2T == True and R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5TBB == True) or (R3Clmn2T == False and R2Clmn2T == True and R4Clmn3TBB == True and R5Clmn4TBB == True and R6Clmn5TBB == True) or (R3Clmn2T == False and R2Clmn2T == True and R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5TBB == True) or (R4Clmn2T == False and R3Clmn2T == True and R3Clmn3TBB == True and R2Clmn4TBB == True and R1Clmn5TBB == True) or (R4Clmn2T == False and R3Clmn2T == True and R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5TBB == True) and DifficultyChoice == 3:
    Botgo = 2
   elif (R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6TBB == True) or (R5Clmn3T == False and R4Clmn3T == True and R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6TBB == True) or (R5Clmn3T == False and R4Clmn3T == True and R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6TBB == True) or (R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6TBB == True) or (R1Clmn3TBB == True and R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3T == False and R3Clmn3T == True) or (R1Clmn6TBB == True and R2Clmn5TBB == True and R3Clmn4TBB == True and R4Clmn3T == False and R3Clmn3T == True) or (R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3T == False) or (R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3TBB == True and R5Clmn3T == False and R4Clmn3T == True) or (R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3T == False and R4Clmn3T == True) or (R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3T == False and R1Clmn3T == True) or (R3Clmn3TBB == True and R4Clmn3TBB == True and R5Clmn3TBB == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True) or (R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4TBB == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True) or (R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3T == False and R2Clmn3T == True) or (R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4TBB == True and R1Clmn3T == False) or (R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3T == False and R3Clmn3T == True) or (R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3T == False and R1Clmn3T == True) or (R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3T == False and R4Clmn3T == True) or (R6Clmn6TBB == True and R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3T == False and R2Clmn3T == True) or (R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True) or (R1Clmn1TBB == True and R2Clmn2TBB == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn4TBB == True) or (R1Clmn1TBB == True and R1Clmn2TBB == True and R1Clmn3T == False and R1Clmn4TBB == True) or (R1Clmn3TBB == True and R2Clmn3TBB == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn3TBB == True) or (R1Clmn5TBB == True and R2Clmn4TBB == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn2TBB == True) or (R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3T == False and R1Clmn2TBB == True) or (R2Clmn1TBB == True and R3Clmn2TBB == True and R4Clmn3T == False and R3Clmn3T == True and R5Clmn4TBB == True) or (R2Clmn1TBB == True and R2Clmn2TBB == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn4TBB == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn2TBB == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn2TBB == True) or (R3Clmn1TBB == True and R4Clmn2TBB == True and R5Clmn3T == False and R4Clmn3T == True and R6Clmn4TBB == True) or (R3Clmn1TBB == True and R3Clmn2TBB == True and R3Clmn3T == False and R2Clmn3T == True and R3Clmn4TBB == True) or (R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3T == False and R2Clmn3T == True and R3Clmn2TBB == True) or (R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3T == False and R4Clmn3T == True and R6Clmn2TBB == True) or (R4Clmn1TBB == True and R3Clmn2TBB == True and R2Clmn3T == False and R1Clmn3T == True and R1Clmn4TBB == True) or (R4Clmn1TBB == True and R4Clmn2TBB == True and R4Clmn3T == False and R3Clmn3T == True and R4Clmn4TBB == True) or (R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3T == False and R3Clmn3T == True and R4Clmn2TBB == True) or (R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3T == False and R1Clmn3T == True and R1Clmn2TBB == True) or (R5Clmn1TBB == True and R4Clmn2TBB == True and R3Clmn3T == False and R2Clmn3T == True and R2Clmn4TBB == True) or (R5Clmn1TBB == True and R5Clmn2TBB == True and R5Clmn3T == False and R4Clmn3T == True and R5Clmn4TBB == True) or (R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3T == False and R4Clmn3T == True and R5Clmn2TBB == True) or (R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3T == False and R2Clmn3T == True and R2Clmn2TBB == True) or (R6Clmn1TBB == True and R5Clmn2TBB == True and R4Clmn3T == False and R3Clmn3T == True and R3Clmn4TBB == True) or (R6Clmn1TBB == True and R6Clmn2TBB == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn4TBB == True) or (R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn2TBB == True) or (R6Clmn5TBB == True and R5Clmn4TBB == True and R4Clmn3T == False and R3Clmn3T == True and R3Clmn2TBB == True) or (R1Clmn2TBB == True and R2Clmn3T == False and R1Clmn3T == True and R3Clmn4TBB == True and R4Clmn5TBB == True) or (R1Clmn2TBB == True and R1Clmn3T == False and R1Clmn4TBB == True and R1Clmn5TBB == True) or (R1Clmn3TBB == True and R2Clmn3T == False and R1Clmn3T == True and R3Clmn3TBB == True and R4Clmn3TBB == True) or (R1Clmn4TBB == True and R2Clmn3T == False and R1Clmn3T == True and R3Clmn2TBB == True and R4Clmn1TBB == True) or (R1Clmn4TBB == True and R1Clmn3T == False and R1Clmn2TBB == True and R1Clmn1TBB == True) or (R2Clmn2TBB == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn4TBB == True and R5Clmn5TBB == True) or (R2Clmn2TBB == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn4TBB == True and R2Clmn5TBB == True) or (R3Clmn2TBB == True and R4Clmn3T == False and R3Clmn3T == True and R5Clmn4TBB == True and R6Clmn5TBB == True) or (R3Clmn2TBB == True and R3Clmn3T == False and R2Clmn3T == True and R3Clmn4TBB == True and R3Clmn5TBB == True) or (R4Clmn2TBB == True and R3Clmn3T == False and R2Clmn3T == True and R2Clmn4TBB == True and R1Clmn5TBB == True) or (R4Clmn2TBB == True and R4Clmn3T == False and R3Clmn3T == True and R4Clmn4TBB == True and R4Clmn5TBB == True) or (R5Clmn2TBB == True and R4Clmn3T == False and R3Clmn3T == True and R3Clmn4TBB == True and R2Clmn5TBB == True) or (R5Clmn2TBB == True and R5Clmn3T == False and R4Clmn3T == True and R5Clmn4TBB == True and R5Clmn5TBB == True) or (R6Clmn2TBB == True and R5Clmn3T == False and R4Clmn3T == True and R4Clmn4TBB == True and R3Clmn5TBB == True) or (R6Clmn2TBB == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn4TBB == True and R6Clmn5TBB == True) or (R1Clmn3T == False and R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3TBB == True) or (R1Clmn3T == False and R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6TBB == True) or (R1Clmn3T == False and R1Clmn4TBB == True and R1Clmn5TBB == True and R1Clmn6TBB == True) or (R2Clmn3T == False and R1Clmn3T == True and R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6TBB == True) or (R2Clmn3T == False and R1Clmn3T == True and R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6TBB == True) or (R3Clmn3T == False and R2Clmn3T == True and R4Clmn4TBB == True and R5Clmn5TBB == True and R6Clmn6TBB == True) or (R3Clmn3T == False and R2Clmn3T == True and R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6TBB == True) or (R4Clmn3T == False and R3Clmn3T == True and R3Clmn4TBB == True and R2Clmn5TBB == True and R1Clmn6TBB == True) or (R4Clmn3T == False and R3Clmn3T == True and R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6TBB == True) and DifficultyChoice == 3: 
    Botgo = 3
   elif (R6Clmn4T == False and R5Clmn4T == True and R6Clmn5TBB == True and R6Clmn6TBB == True and R6Clmn7TBB == True) or (R6Clmn4T == False and R5Clmn4T == True and R5Clmn5TBB == True and R4Clmn6TBB == True and R3Clmn7TBB == True) or (R5Clmn4T == False and R4Clmn4T == True and R4Clmn5TBB == True and R3Clmn6TBB == True and R2Clmn7TBB == True) or (R5Clmn4T == False and R4Clmn4T == True and R5Clmn5TBB == True and R5Clmn6TBB == True and R5Clmn7TBB == True) or (R1Clmn1TBB == True and R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True) or (R1Clmn1TBB == True and R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4T == False) or (R1Clmn4TBB == True and R2Clmn4TBB == True and R3Clmn4TBB == True and R4Clmn4T == False and R3Clmn4T == True) or (R1Clmn7TBB == True and R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4T == False) or (R1Clmn7TBB == True and R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True) or (R2Clmn1TBB == True and R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4T == False and R4Clmn4T == True) or (R2Clmn1TBB == True and R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4T == False and R1Clmn4T == True) or (R2Clmn4TBB == True and R3Clmn4TBB == True and R4Clmn4TBB == True and R5Clmn4T == False and R4Clmn4T == True) or (R2Clmn7TBB == True and R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4T == False and R4Clmn4T == True) or (R2Clmn7TBB == True and R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4T == False and R1Clmn4T == True) or (R3Clmn1TBB == True and R4Clmn2TBB == True and R5Clmn3TBB == True and R6Clmn4T == False and R5Clmn4T == True) or (R3Clmn1TBB == True and R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True) or (R3Clmn4TBB == True and R4Clmn4TBB == True and R5Clmn4TBB == True and R6Clmn4T == False and R5Clmn4T == True) or (R3Clmn7TBB == True and R4Clmn6TBB == True and R5Clmn5TBB == True and R6Clmn4T == False and R5Clmn4T == True) or (R3Clmn7TBB == True and R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True) or (R4Clmn1TBB == True and R3Clmn2TBB == True and R2Clmn3TBB == True and R1Clmn4T == False) or (R4Clmn1TBB == True and R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True) or (R4Clmn7TBB == True and R3Clmn6TBB == True and R2Clmn5TBB == True and R1Clmn4T == False) or (R4Clmn7TBB == True and R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True) or (R5Clmn1TBB == True and R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4T == False and R1Clmn4T == True) or (R5Clmn1TBB == True and R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4T == False and R4Clmn4T == True) or (R5Clmn7TBB == True and R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4T == False and R1Clmn4T == True) or (R5Clmn7TBB == True and R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4T == False and R4Clmn4T == True) or (R6Clmn1TBB == True and R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True) or (R6Clmn1TBB == True and R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4T == False and R5Clmn4T == True) or (R6Clmn7TBB == True and R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True) or (R6Clmn7TBB == True and R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4T == False and R5Clmn4T == True) or (R1Clmn2TBB == True and R2Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn5TBB == True) or (R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4T == False and R1Clmn5TBB == True) or (R1Clmn6TBB == True and R2Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn3TBB == True) or (R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4T == False and R1Clmn3TBB == True) or (R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn5TBB == True) or (R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn5TBB == True) or (R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn3TBB == True) or (R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn3TBB == True) or (R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4T == False and R4Clmn4T == True and R6Clmn5TBB == True) or (R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn5TBB == True) or (R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4T == False and R4Clmn4T == True and R6Clmn3TBB == True) or (R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn3TBB == True) or (R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4T == False and R1Clmn4T == True and R1Clmn5TBB == True) or (R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn5TBB == True) or (R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4T == False and R1Clmn4T == True and R1Clmn3TBB == True) or (R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn3TBB == True) or (R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn5TBB == True) or (R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn5TBB == True) or (R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn3TBB == True) or (R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn3TBB == True) or (R6Clmn2TBB == True and R5Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn5TBB == True) or (R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn5TBB == True) or (R6Clmn6TBB == True and R5Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn3TBB == True) or (R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn3TBB == True) or (R1Clmn3TBB == True and R2Clmn4T == False and R1Clmn4T == True and R3Clmn5TBB == True and R4Clmn6TBB == True) or (R1Clmn3TBB == True and R1Clmn4T == False and R1Clmn5TBB == True and R1Clmn6TBB == True) or (R1Clmn5TBB == True and R2Clmn4T == False and R1Clmn4T == True and R3Clmn3TBB == True and R4Clmn2TBB == True) or (R1Clmn5TBB == True and R1Clmn4T == False and R1Clmn3TBB == True and R1Clmn2TBB == True) or (R2Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn5TBB == True and R5Clmn6TBB == True) or (R2Clmn3TBB == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn5TBB == True and R2Clmn6TBB == True) or (R2Clmn5TBB == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R2Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn3TBB == True and R5Clmn2TBB == True) or (R3Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn5TBB == True and R6Clmn6TBB == True) or (R3Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn5TBB == True and R3Clmn6TBB == True) or (R3Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn3TBB == True and R3Clmn2TBB == True) or (R3Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn3TBB == True and R6Clmn2TBB == True) or (R4Clmn3TBB == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn5TBB == True and R1Clmn6TBB == True) or (R4Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn5TBB == True and R4Clmn6TBB == True) or (R4Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn3TBB == True and R4Clmn2TBB == True) or (R4Clmn5TBB == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn3TBB == True and R1Clmn2TBB == True) or (R5Clmn3TBB == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn5TBB == True and R2Clmn6TBB == True) or (R5Clmn3TBB == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn5TBB == True and R5Clmn6TBB == True) or (R5Clmn5TBB == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn3TBB == True and R5Clmn2TBB == True) or (R5Clmn5TBB == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn3TBB == True and R2Clmn2TBB == True) or (R6Clmn3TBB == True and R5Clmn4T == False and R4Clmn4T == True and R4Clmn5TBB == True and R3Clmn6TBB == True) or (R6Clmn3TBB == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn5TBB == True and R6Clmn6TBB == True) or (R6Clmn5TBB == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn3TBB == True and R6Clmn2TBB == True) or (R6Clmn5TBB == True and R5Clmn4T == False and R4Clmn4T == True and R4Clmn3TBB == True and R3Clmn2TBB == True) or (R1Clmn4T == False and R2Clmn3TBB == True and R3Clmn2TBB == True and R4Clmn1TBB == True) or (R1Clmn4T == False and R1Clmn3TBB == True and R1Clmn2TBB == True and R1Clmn1TBB == True) or (R2Clmn4T == False and R1Clmn4T == True and R2Clmn5TBB == True and R2Clmn6TBB == True and R2Clmn7TBB == True) or (R2Clmn4T == False and R1Clmn4T == True and R3Clmn5TBB == True and R4Clmn6TBB == True and R5Clmn7TBB == True) or (R3Clmn4T == False and R2Clmn4T == True and R3Clmn5TBB == True and R3Clmn6TBB == True and R3Clmn7TBB == True) or (R3Clmn4T == False and R2Clmn4T == True and R4Clmn5TBB == True and R5Clmn6TBB == True and R6Clmn7TBB == True) or (R4Clmn4T == False and R3Clmn4T == True and R4Clmn5TBB == True and R4Clmn6TBB == True and R4Clmn7TBB == True) or (R4Clmn4T == False and R3Clmn4T == True and R3Clmn5TBB == True and R2Clmn6TBB == True and R1Clmn7TBB == True) and DifficultyChoice == 3: 
    Botgo = 4
   elif (R6Clmn5T == False and R5Clmn5T == True and R6Clmn4TBB == True and R6Clmn3TBB == True and R6Clmn2TBB == True) or (R5Clmn5T == False and R4Clmn5T == True and R4Clmn4TBB == True and R3Clmn3TBB == True and R2Clmn2TBB == True) or (R5Clmn5T == False and R4Clmn5T == True and R5Clmn4TBB == True and R5Clmn3TBB == True and R5Clmn2TBB == True) or (R6Clmn5T == False and R5Clmn5T == True and R5Clmn4TBB == True and R4Clmn3TBB == True and R3Clmn2TBB == True) or (R1Clmn2TBB == True and R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True) or (R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5T == False) or (R1Clmn5TBB == True and R2Clmn5TBB == True and R3Clmn5TBB == True and R4Clmn5T == False and R3Clmn5T == True) or (R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5T == False and R4Clmn5T == True) or (R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5T == False and R1Clmn5T == True) or (R2Clmn5TBB == True and R3Clmn5TBB == True and R4Clmn5TBB == True and R5Clmn5T == False and R4Clmn5T == True) or (R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4TBB == True and R6Clmn5T == False and R5Clmn5T == True) or (R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True) or (R3Clmn5TBB == True and R4Clmn5TBB == True and R5Clmn5TBB == True and R6Clmn5T == False and R5Clmn5T == True) or (R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4TBB == True and R1Clmn5T == False) or (R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True) or (R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5T == False and R1Clmn5T == True) or (R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5T == False and R4Clmn5T == True) or (R6Clmn2TBB == True and R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True) or (R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5T == False and R5Clmn5T == True) or (R1Clmn3TBB == True and R2Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn6TBB == True) or (R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5T == False and R1Clmn6TBB == True) or (R1Clmn7TBB == True and R1Clmn6TBB == True and R1Clmn5T == False and R1Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn6TBB == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn4TBB == True) or (R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn6TBB == True) or (R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn6TBB == True) or (R2Clmn7TBB == True and R3Clmn6TBB == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn4TBB == True) or (R2Clmn7TBB == True and R2Clmn6TBB == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBB == True) or (R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5T == False and R4Clmn5T == True and R6Clmn6TBB == True) or (R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn6TBB == True) or (R3Clmn7TBB == True and R4Clmn6TBB == True and R5Clmn5T == False and R4Clmn5T == True and R6Clmn4TBB == True) or (R3Clmn7TBB == True and R3Clmn6TBB == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn4TBB == True) or (R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5T == False and R1Clmn5T == True and R1Clmn6TBB == True) or (R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn6TBB == True) or (R4Clmn7TBB == True and R3Clmn6TBB == True and R2Clmn5T == False and R1Clmn5T == True and R1Clmn4TBB == True) or (R4Clmn7TBB == True and R4Clmn6TBB == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn4TBB == True) or (R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn6TBB == True) or (R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn6TBB == True) or (R5Clmn7TBB == True and R4Clmn6TBB == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn4TBB == True) or (R5Clmn7TBB == True and R5Clmn6TBB == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn4TBB == True) or (R6Clmn3TBB == True and R5Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn6TBB == True) or (R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn6TBB == True) or (R6Clmn7TBB == True and R5Clmn6TBB == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn4TBB == True) or (R6Clmn7TBB == True and R6Clmn6TBB == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn4TBB == True) or (R1Clmn6TBB == True and R2Clmn5T == False and R1Clmn5T == True and R3Clmn4TBB == True and R4Clmn3TBB == True) or (R1Clmn6TBB == True and R1Clmn5T == False and R1Clmn4TBB == True and R1Clmn3TBB == True) or (R2Clmn4TBB == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn6TBB == True and R2Clmn7TBB == True) or (R2Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn6TBB == True and R5Clmn7TBB == True) or (R2Clmn6TBB == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn4TBB == True and R5Clmn3TBB == True) or (R2Clmn6TBB == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBB == True and R2Clmn3TBB == True) or (R3Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn6TBB == True and R3Clmn7TBB == True) or (R3Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn6TBB == True and R6Clmn7TBB == True) or (R3Clmn6TBB == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn4TBB == True and R6Clmn3TBB == True) or (R3Clmn6TBB == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn4TBB == True and R3Clmn3TBB == True) or (R4Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn6TBB == True and R4Clmn7TBB == True) or (R4Clmn4TBB == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn6TBB == True and R1Clmn7TBB == True) or (R4Clmn6TBB == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn4TBB == True and R1Clmn3TBB == True) or (R4Clmn6TBB == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn4TBB == True and R4Clmn3TBB == True) or (R5Clmn4TBB == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn6TBB == True and R5Clmn7TBB == True) or (R5Clmn4TBB == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn6TBB == True and R2Clmn7TBB == True) or (R5Clmn6TBB == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn4TBB == True and R2Clmn3TBB == True) or (R5Clmn6TBB == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn4TBB == True and R5Clmn3TBB == True) or (R6Clmn4TBB == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn6TBB == True and R6Clmn7TBB == True) or (R6Clmn4TBB == True and R5Clmn5T == False and R4Clmn5T == True and R4Clmn6TBB == True and R3Clmn7TBB == True) or (R6Clmn6TBB == True and R5Clmn5T == False and R4Clmn5T == True and R4Clmn4TBB == True and R3Clmn3TBB == True) or (R6Clmn6TBB == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn4TBB == True and R6Clmn3TBB == True) or (R1Clmn5T == False and R2Clmn4TBB == True and R3Clmn3TBB == True and R4Clmn2TBB == True) or (R1Clmn5T == False and R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2TBB == True) or (R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R3Clmn5T == False and R2Clmn5T == True and R3Clmn4TBB == True and R3Clmn3TBB == True and R3Clmn2TBB == True) or (R3Clmn5T == False and R2Clmn5T == True and R4Clmn4TBB == True and R5Clmn3TBB == True and R6Clmn2TBB == True) or (R4Clmn5T == False and R3Clmn5T == True and R4Clmn4TBB == True and R4Clmn3TBB == True and R4Clmn2TBB == True) or (R4Clmn5T == False and R3Clmn5T == True and R3Clmn4TBB == True and R2Clmn3TBB == True and R1Clmn2TBB == True) and DifficultyChoice == 3: 
    Botgo = 5
   elif (R6Clmn6T == False and R5Clmn6T == True and R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3TBB == True) or (R6Clmn6T == False and R5Clmn6T == True and R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3TBB == True) or (R5Clmn6T == False and R4Clmn6T == True and R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3TBB == True) or (R5Clmn6T == False and R4Clmn6T == True and R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3TBB == True) or (R1Clmn3TBB == True and R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6T == False and R3Clmn6T == True) or (R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5TBB == True and R1Clmn6T == False) or (R1Clmn6TBB == True and R2Clmn6TBB == True and R3Clmn6TBB == True and R4Clmn6T == False and R3Clmn6T == True) or (R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6T == False and R4Clmn6T == True) or (R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6T == False and R1Clmn6T == True) or (R2Clmn6TBB == True and R3Clmn6TBB == True and R4Clmn6TBB == True and R5Clmn6T == False and R4Clmn6T == True) or (R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5TBB == True and R6Clmn6T == False and R5Clmn6T == True) or (R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6T == False and R2Clmn6T == True) or (R3Clmn6TBB == True and R4Clmn6TBB == True and R5Clmn6TBB == True and R6Clmn6T == False and R5Clmn6T == True) or (R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5TBB == True and R1Clmn6T == False) or (R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6T == False and R3Clmn6T == True) or (R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6T == False and R1Clmn6T == True) or (R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6T == False and R4Clmn6T == True) or (R6Clmn3TBB == True and R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6T == False and R2Clmn6T == True) or (R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6T == False and R5Clmn6T == True) or (R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6T == False and R1Clmn6T == True and R2Clmn7TBB == True) or (R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6T == False and R3Clmn6T == True and R5Clmn7TBB == True) or (R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6T == False and R2Clmn6T == True and R3Clmn7TBB == True) or (R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6T == False and R4Clmn6T == True and R6Clmn7TBB == True) or (R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6T == False and R3Clmn6T == True and R4Clmn7TBB == True) or (R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6T == False and R1Clmn6T == True and R1Clmn6T == True and R1Clmn7TBB == True) or (R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6T == False and R4Clmn6T == True and R5Clmn7TBB == True) or (R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6T == False and R2Clmn6T == True and R2Clmn7TBB == True) or (R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6T == False and R5Clmn6T == True and R6Clmn7TBB == True) or (R6Clmn4TBB == True and R5Clmn5TBB == True and R4Clmn6T == False and R3Clmn6T == True and R3Clmn7TBB == True) or (R1Clmn7TBB == True and R1Clmn6T == False and R1Clmn5TBB == True and R1Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn6T == False and R1Clmn6T == True and R3Clmn5TBB == True and R4Clmn4TBB == True) or (R2Clmn7TBB == True and R3Clmn6T == False and R2Clmn6T == True and R4Clmn5TBB == True and R5Clmn4TBB == True) or (R2Clmn7TBB == True and R2Clmn6T == False and R1Clmn6T == True and R2Clmn5TBB == True and R2Clmn4TBB == True) or (R3Clmn7TBB == True and R4Clmn6T == False and R3Clmn6T == True and R5Clmn5TBB == True and R6Clmn4TBB == True) or (R3Clmn7TBB == True and R3Clmn6T == False and R2Clmn6T == True and R3Clmn5TBB == True and R3Clmn4TBB == True) or (R4Clmn7TBB == True and R3Clmn6T == False and R2Clmn6T == True and R2Clmn5TBB == True and R1Clmn4TBB == True) or (R4Clmn7TBB == True and R4Clmn6T == False and R3Clmn6T == True and R4Clmn5TBB == True and R4Clmn4TBB == True) or (R5Clmn7TBB == True and R4Clmn6T == False and R3Clmn6T == True and R3Clmn5TBB == True and R2Clmn4TBB == True) or (R5Clmn7TBB == True and R5Clmn6T == False and R4Clmn6T == True and R5Clmn5TBB == True and R5Clmn4TBB == True) or (R6Clmn7TBB == True and R5Clmn6T == False and R4Clmn6T == True and R4Clmn5TBB == True and R3Clmn4TBB == True) or (R6Clmn7TBB == True and R6Clmn6T == False and R5Clmn6T == True and R6Clmn5TBB == True and R6Clmn4TBB == True) or (R1Clmn6T == False and R2Clmn5TBB == True and R3Clmn4TBB == True and R4Clmn3TBB == True) or (R1Clmn6T == False and R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3TBB == True) or (R2Clmn6T == False and R1Clmn6T == True and R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3TBB == True) or (R2Clmn6T == False and R1Clmn6T == True and R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True) or (R3Clmn6T == False and R2Clmn6T == True and R4Clmn5TBB == True and R5Clmn4TBB == True and R6Clmn3TBB == True) or (R3Clmn6T == False and R2Clmn6T == True and R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3TBB == True) or (R4Clmn6T == False and R3Clmn6T == True and R3Clmn5TBB == True and R2Clmn4TBB == True and R1Clmn3TBB == True) or (R4Clmn6T == False and R3Clmn6T == True and R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3TBB == True) and DifficultyChoice == 3: 
    Botgo = 6
   elif (R6Clmn7T == False and R5Clmn7T == True and R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4TBB == True) or (R6Clmn7T == False and R5Clmn7T == True and R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4TBB == True) or (R5Clmn7T == False and R4Clmn7T == True and R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4TBB == True) or (R5Clmn7T == False and R4Clmn7T == True and R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn7TBB == True and R3Clmn7TBB == True and R4Clmn7T == False and R3Clmn7T == True) or (R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6TBB == True and R2Clmn7T == False and R1Clmn7T == True) or (R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6TBB == True and R5Clmn7T == False and R4Clmn7T == True) or (R2Clmn7TBB == True and R3Clmn7TBB == True and R4Clmn7TBB == True and R5Clmn7T == False and R4Clmn7T == True) or (R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6TBB == True and R3Clmn7T == False and R2Clmn7T == True) or (R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6TBB == True and R6Clmn7T == False and R5Clmn7T == True) or (R3Clmn7TBB == True and R4Clmn7TBB == True and R5Clmn7TBB == True and R6Clmn7T == False and R5Clmn7T == True) or (R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6TBB == True and R4Clmn7T == False and R3Clmn7T == True) or (R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6TBB == True and R1Clmn7T == False) or (R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6TBB == True and R5Clmn7T == False and R4Clmn7T == True) or (R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6TBB == True and R2Clmn7T == False and R1Clmn7T == True) or (R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6TBB == True and R6Clmn7T == False and R5Clmn7T == True) or (R6Clmn4TBB == True and R5Clmn5TBB == True and R4Clmn6TBB == True and R3Clmn7T == False and R2Clmn7T == True) or (R1Clmn7T == False and R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4TBB == True) or (R1Clmn7T == False and R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4TBB == True) or (R2Clmn7T == False and R1Clmn7T == True and R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4TBB == True) or (R2Clmn7T == False and R1Clmn7T == True and R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4TBB == True) or (R3Clmn7T == False and R2Clmn7T == True and R4Clmn6TBB == True and R5Clmn5TBB == True and R6Clmn4TBB == True) or (R3Clmn7T == False and R2Clmn7T == True and R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4TBB == True) or (R4Clmn7T == False and R3Clmn7T == True and R3Clmn6TBB == True and R2Clmn5TBB == True and R1Clmn4TBB == True) or (R4Clmn7T == False and R3Clmn7T == True and R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4TBB == True) and DifficultyChoice == 3: 
    Botgo = 7
   elif (R6Clmn1T == False and R5Clmn1T == True and R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True) or (R6Clmn1T == False and R5Clmn1T == True and R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True) or (R5Clmn1T == False and R4Clmn1T == True and R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True) or (R5Clmn1T == False and R4Clmn1T == True and R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True) or (R4Clmn1T == False and R3Clmn1T == True and R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True) or (R4Clmn1T == False and R3Clmn1T == True and R3Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4TBY == True) or (R3Clmn1T == False and R2Clmn1T == True and R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True) or (R3Clmn1T == False and R2Clmn1T == True and R4Clmn2TBY == True and R5Clmn3TBY == True and R6Clmn4TBY == True) or (R2Clmn1T == False and R1Clmn1T == True and R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True) or (R2Clmn1T == False and R1Clmn1T == True and R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True) or (R1Clmn1T == False and R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4TBY == True) or (R1Clmn1T == False and R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True) or (R2Clmn1TBY == True and R3Clmn1TBY == True and R4Clmn1TBY == True and R5Clmn1T == False and R4Clmn1T == True) or (R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2TBY == True and R1Clmn1T == False) or (R1Clmn4TBY == True and R2Clmn3TBY == True and R3Clmn2TBY == True and R4Clmn1T == False and R3Clmn1T == True) or (R1Clmn1TBY == True and R2Clmn1TBY == True and R3Clmn1TBY == True and R4Clmn1T == False and R3Clmn1T == True) or (R3Clmn1TBY == True and R4Clmn1TBY == True and R5Clmn1TBY == True and R6Clmn1T == False and R5Clmn1T == True) and DifficultyChoice >= 2: 
    Botgo = 1
   elif (R6Clmn2T == False and R5Clmn2T == True and R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True) or (R6Clmn2T == False and R5Clmn2T == True and R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True) or (R5Clmn2T == False and R4Clmn2T == True and R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True) or (R5Clmn2T == False and R4Clmn2T == True and R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True) or (R1Clmn2TBY == True and R2Clmn2TBY == True and R3Clmn2TBY == True and R4Clmn2T == False and R3Clmn2T == True) or (R1Clmn5TBY == True and R2Clmn4TBY == True and R3Clmn3TBY == True and R4Clmn2T == False and R3Clmn2T == True) or (R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2T == False) or (R2Clmn2TBY == True and R3Clmn2TBY == True and R4Clmn2TBY == True and R5Clmn2T == False and R4Clmn2T == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2T == False and R1Clmn2T == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2T == False and R1Clmn2T == True) or (R3Clmn2TBY == True and R4Clmn2TBY == True and R5Clmn2TBY == True and R6Clmn2T == False and R5Clmn2T == True) or (R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True and R3Clmn2T == False and R2Clmn2T == True) or (R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True and R6Clmn2T == False and R5Clmn2T == True) or (R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True and R4Clmn2T == False and R3Clmn2T == True) or (R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2T == False) or (R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True and R5Clmn2T == False and R4Clmn2T == True) or (R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True and R2Clmn2T == False and R1Clmn2T == True) or (R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True and R6Clmn2T == False and R5Clmn2T == True) or (R6Clmn5TBY == True and R5Clmn4TBY == True and R4Clmn3TBY == True and R3Clmn2T == False and R2Clmn2T == True) or (R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2T == False and R1Clmn1TBY == True) or (R1Clmn4TBY == True and R2Clmn3TBY == True and R3Clmn2T == False and R2Clmn2T == True and R4Clmn1TBY == True) or (R1Clmn1TBY == True and R2Clmn2T == False and R1Clmn2T == True and R3Clmn3TBY == True and R4Clmn4TBY == True) or (R1Clmn1TBY == True and R1Clmn2T == False and R1Clmn3TBY == True and R1Clmn4TBY == True) or (R2Clmn1TBY == True and R3Clmn2T == False and R2Clmn2T == True and R4Clmn3TBY == True and R5Clmn4TBY == True) or (R2Clmn1TBY == True and R2Clmn2T == False and R1Clmn2T == True and R2Clmn3TBY == True and R2Clmn4TBY == True) or (R3Clmn1TBY == True and R4Clmn2T == False and R3Clmn2T == True and R5Clmn3TBY == True and R6Clmn4TBY == True) or (R3Clmn1TBY == True and R3Clmn2T == False and R2Clmn2T == True and R3Clmn3TBY == True and R3Clmn4TBY == True) or (R4Clmn1TBY == True and R3Clmn2T == False and R2Clmn2T == True and R2Clmn3TBY == True and R1Clmn4TBY == True) or (R4Clmn1TBY == True and R4Clmn2T == False and R3Clmn2T == True and R4Clmn3TBY == True and R4Clmn4TBY == True) or (R5Clmn1TBY == True and R4Clmn2T == False and R3Clmn2T == True and R3Clmn3TBY == True and R2Clmn4TBY == True) or (R5Clmn1TBY == True and R5Clmn2T == False and R4Clmn2T == True and R5Clmn3TBY == True and R5Clmn4TBY == True) or (R6Clmn1TBY == True and R5Clmn2T == False and R4Clmn2T == True and R4Clmn3TBY == True and R3Clmn4TBY == True) or (R6Clmn1TBY == True and R6Clmn2T == False and R5Clmn2T == True and R6Clmn3TBY == True and R6Clmn4TBY == True) or (R1Clmn2T == False and R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True) or (R1Clmn2T == False and R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5TBY == True) or (R2Clmn2T == False and R1Clmn2T == True and R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R2Clmn2T == False and R1Clmn2T == True and R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True) or (R3Clmn2T == False and R2Clmn2T == True and R4Clmn3TBY == True and R5Clmn4TBY == True and R6Clmn5TBY == True) or (R3Clmn2T == False and R2Clmn2T == True and R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True) or (R4Clmn2T == False and R3Clmn2T == True and R3Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5TBY == True) or (R4Clmn2T == False and R3Clmn2T == True and R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True) and DifficultyChoice >= 2:
    Botgo = 2
   elif (R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True) or (R5Clmn3T == False and R4Clmn3T == True and R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True) or (R5Clmn3T == False and R4Clmn3T == True and R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True) or (R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True) or (R1Clmn3TBY == True and R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3T == False and R3Clmn3T == True) or (R1Clmn6TBY == True and R2Clmn5TBY == True and R3Clmn4TBY == True and R4Clmn3T == False and R3Clmn3T == True) or (R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3T == False) or (R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3TBY == True and R5Clmn3T == False and R4Clmn3T == True) or (R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3T == False and R4Clmn3T == True) or (R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3T == False and R1Clmn3T == True) or (R3Clmn3TBY == True and R4Clmn3TBY == True and R5Clmn3TBY == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True) or (R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True) or (R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3T == False and R2Clmn3T == True) or (R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3T == False) or (R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3T == False and R3Clmn3T == True) or (R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3T == False and R1Clmn3T == True) or (R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3T == False and R4Clmn3T == True) or (R6Clmn6TBY == True and R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3T == False and R2Clmn3T == True) or (R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True) or (R1Clmn1TBY == True and R2Clmn2TBY == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn4TBY == True) or (R1Clmn1TBY == True and R1Clmn2TBY == True and R1Clmn3T == False and R1Clmn4TBY == True) or (R1Clmn3TBY == True and R2Clmn3TBY == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn3TBY == True) or (R1Clmn5TBY == True and R2Clmn4TBY == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn2TBY == True) or (R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3T == False and R1Clmn2TBY == True) or (R2Clmn1TBY == True and R3Clmn2TBY == True and R4Clmn3T == False and R3Clmn3T == True and R5Clmn4TBY == True) or (R2Clmn1TBY == True and R2Clmn2TBY == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn4TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn2TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn2TBY == True) or (R3Clmn1TBY == True and R4Clmn2TBY == True and R5Clmn3T == False and R4Clmn3T == True and R6Clmn4TBY == True) or (R3Clmn1TBY == True and R3Clmn2TBY == True and R3Clmn3T == False and R2Clmn3T == True and R3Clmn4TBY == True) or (R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3T == False and R2Clmn3T == True and R3Clmn2TBY == True) or (R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3T == False and R4Clmn3T == True and R6Clmn2TBY == True) or (R4Clmn1TBY == True and R3Clmn2TBY == True and R2Clmn3T == False and R1Clmn3T == True and R1Clmn4TBY == True) or (R4Clmn1TBY == True and R4Clmn2TBY == True and R4Clmn3T == False and R3Clmn3T == True and R4Clmn4TBY == True) or (R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3T == False and R3Clmn3T == True and R4Clmn2TBY == True) or (R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3T == False and R1Clmn3T == True and R1Clmn2TBY == True) or (R5Clmn1TBY == True and R4Clmn2TBY == True and R3Clmn3T == False and R2Clmn3T == True and R2Clmn4TBY == True) or (R5Clmn1TBY == True and R5Clmn2TBY == True and R5Clmn3T == False and R4Clmn3T == True and R5Clmn4TBY == True) or (R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3T == False and R4Clmn3T == True and R5Clmn2TBY == True) or (R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3T == False and R2Clmn3T == True and R2Clmn2TBY == True) or (R6Clmn1TBY == True and R5Clmn2TBY == True and R4Clmn3T == False and R3Clmn3T == True and R3Clmn4TBY == True) or (R6Clmn1TBY == True and R6Clmn2TBY == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn4TBY == True) or (R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn2TBY == True) or (R6Clmn5TBY == True and R5Clmn4TBY == True and R4Clmn3T == False and R3Clmn3T == True and R3Clmn2TBY == True) or (R1Clmn2TBY == True and R2Clmn3T == False and R1Clmn3T == True and R3Clmn4TBY == True and R4Clmn5TBY == True) or (R1Clmn2TBY == True and R1Clmn3T == False and R1Clmn4TBY == True and R1Clmn5TBY == True) or (R1Clmn3TBY == True and R2Clmn3T == False and R1Clmn3T == True and R3Clmn3TBY == True and R4Clmn3TBY == True) or (R1Clmn4TBY == True and R2Clmn3T == False and R1Clmn3T == True and R3Clmn2TBY == True and R4Clmn1TBY == True) or (R1Clmn4TBY == True and R1Clmn3T == False and R1Clmn2TBY == True and R1Clmn1TBY == True) or (R2Clmn2TBY == True and R3Clmn3T == False and R2Clmn3T == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R2Clmn2TBY == True and R2Clmn3T == False and R1Clmn3T == True and R2Clmn4TBY == True and R2Clmn5TBY == True) or (R3Clmn2TBY == True and R4Clmn3T == False and R3Clmn3T == True and R5Clmn4TBY == True and R6Clmn5TBY == True) or (R3Clmn2TBY == True and R3Clmn3T == False and R2Clmn3T == True and R3Clmn4TBY == True and R3Clmn5TBY == True) or (R4Clmn2TBY == True and R3Clmn3T == False and R2Clmn3T == True and R2Clmn4TBY == True and R1Clmn5TBY == True) or (R4Clmn2TBY == True and R4Clmn3T == False and R3Clmn3T == True and R4Clmn4TBY == True and R4Clmn5TBY == True) or (R5Clmn2TBY == True and R4Clmn3T == False and R3Clmn3T == True and R3Clmn4TBY == True and R2Clmn5TBY == True) or (R5Clmn2TBY == True and R5Clmn3T == False and R4Clmn3T == True and R5Clmn4TBY == True and R5Clmn5TBY == True) or (R6Clmn2TBY == True and R5Clmn3T == False and R4Clmn3T == True and R4Clmn4TBY == True and R3Clmn5TBY == True) or (R6Clmn2TBY == True and R6Clmn3T == False and R5Clmn3T == True and R5Clmn3T == True and R6Clmn4TBY == True and R6Clmn5TBY == True) or (R1Clmn3T == False and R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3TBY == True) or (R1Clmn3T == False and R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True) or (R1Clmn3T == False and R1Clmn4TBY == True and R1Clmn5TBY == True and R1Clmn6TBY == True) or (R2Clmn3T == False and R1Clmn3T == True and R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True) or (R2Clmn3T == False and R1Clmn3T == True and R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True) or (R3Clmn3T == False and R2Clmn3T == True and R4Clmn4TBY == True and R5Clmn5TBY == True and R6Clmn6TBY == True) or (R3Clmn3T == False and R2Clmn3T == True and R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True) or (R4Clmn3T == False and R3Clmn3T == True and R3Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6TBY == True) or (R4Clmn3T == False and R3Clmn3T == True and R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True) and DifficultyChoice >= 2: 
    Botgo = 3
   elif (R6Clmn4T == False and R5Clmn4T == True and R6Clmn5TBY == True and R6Clmn6TBY == True and R6Clmn7TBY == True) or (R6Clmn4T == False and R5Clmn4T == True and R5Clmn5TBY == True and R4Clmn6TBY == True and R3Clmn7TBY == True) or (R5Clmn4T == False and R4Clmn4T == True and R4Clmn5TBY == True and R3Clmn6TBY == True and R2Clmn7TBY == True) or (R5Clmn4T == False and R4Clmn4T == True and R5Clmn5TBY == True and R5Clmn6TBY == True and R5Clmn7TBY == True) or (R1Clmn1TBY == True and R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True) or (R1Clmn1TBY == True and R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4T == False) or (R1Clmn4TBY == True and R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4T == False and R3Clmn4T == True) or (R1Clmn7TBY == True and R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4T == False) or (R1Clmn7TBY == True and R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True) or (R2Clmn1TBY == True and R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4T == False and R4Clmn4T == True) or (R2Clmn1TBY == True and R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4T == False and R1Clmn4T == True) or (R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4TBY == True and R5Clmn4T == False and R4Clmn4T == True) or (R2Clmn7TBY == True and R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4T == False and R4Clmn4T == True) or (R2Clmn7TBY == True and R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4T == False and R1Clmn4T == True) or (R3Clmn1TBY == True and R4Clmn2TBY == True and R5Clmn3TBY == True and R6Clmn4T == False and R5Clmn4T == True) or (R3Clmn1TBY == True and R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True) or (R3Clmn4TBY == True and R4Clmn4TBY == True and R5Clmn4TBY == True and R6Clmn4T == False and R5Clmn4T == True) or (R3Clmn7TBY == True and R4Clmn6TBY == True and R5Clmn5TBY == True and R6Clmn4T == False and R5Clmn4T == True) or (R3Clmn7TBY == True and R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True) or (R4Clmn1TBY == True and R3Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4T == False) or (R4Clmn1TBY == True and R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True) or (R4Clmn7TBY == True and R3Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4T == False) or (R4Clmn7TBY == True and R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True) or (R5Clmn1TBY == True and R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4T == False and R1Clmn4T == True) or (R5Clmn1TBY == True and R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4T == False and R4Clmn4T == True) or (R5Clmn7TBY == True and R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4T == False and R1Clmn4T == True) or (R5Clmn7TBY == True and R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4T == False and R4Clmn4T == True) or (R6Clmn1TBY == True and R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True) or (R6Clmn1TBY == True and R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4T == False and R5Clmn4T == True) or (R6Clmn7TBY == True and R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True) or (R6Clmn7TBY == True and R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4T == False and R5Clmn4T == True) or (R1Clmn2TBY == True and R2Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn5TBY == True) or (R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4T == False and R1Clmn5TBY == True) or (R1Clmn6TBY == True and R2Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn3TBY == True) or (R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4T == False and R1Clmn3TBY == True) or (R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn5TBY == True) or (R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn5TBY == True) or (R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn3TBY == True) or (R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn3TBY == True) or (R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4T == False and R4Clmn4T == True and R6Clmn5TBY == True) or (R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn5TBY == True) or (R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4T == False and R4Clmn4T == True and R6Clmn3TBY == True) or (R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn3TBY == True) or (R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4T == False and R1Clmn4T == True and R1Clmn5TBY == True) or (R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn5TBY == True) or (R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4T == False and R1Clmn4T == True and R1Clmn3TBY == True) or (R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn3TBY == True) or (R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn5TBY == True) or (R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn5TBY == True) or (R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn3TBY == True) or (R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn3TBY == True) or (R6Clmn2TBY == True and R5Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn5TBY == True) or (R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn5TBY == True) or (R6Clmn6TBY == True and R5Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn3TBY == True) or (R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn3TBY == True) or (R1Clmn3TBY == True and R2Clmn4T == False and R1Clmn4T == True and R3Clmn5TBY == True and R4Clmn6TBY == True) or (R1Clmn3TBY == True and R1Clmn4T == False and R1Clmn5TBY == True and R1Clmn6TBY == True) or (R1Clmn5TBY == True and R2Clmn4T == False and R1Clmn4T == True and R3Clmn3TBY == True and R4Clmn2TBY == True) or (R1Clmn5TBY == True and R1Clmn4T == False and R1Clmn3TBY == True and R1Clmn2TBY == True) or (R2Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn5TBY == True and R5Clmn6TBY == True) or (R2Clmn3TBY == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn5TBY == True and R2Clmn6TBY == True) or (R2Clmn5TBY == True and R2Clmn4T == False and R1Clmn4T == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True and R4Clmn3TBY == True and R5Clmn2TBY == True) or (R3Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn5TBY == True and R6Clmn6TBY == True) or (R3Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn5TBY == True and R3Clmn6TBY == True) or (R3Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True and R3Clmn3TBY == True and R3Clmn2TBY == True) or (R3Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True and R5Clmn3TBY == True and R6Clmn2TBY == True) or (R4Clmn3TBY == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn5TBY == True and R1Clmn6TBY == True) or (R4Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn5TBY == True and R4Clmn6TBY == True) or (R4Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True and R4Clmn3TBY == True and R4Clmn2TBY == True) or (R4Clmn5TBY == True and R3Clmn4T == False and R2Clmn4T == True and R2Clmn3TBY == True and R1Clmn2TBY == True) or (R5Clmn3TBY == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn5TBY == True and R2Clmn6TBY == True) or (R5Clmn3TBY == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn5TBY == True and R5Clmn6TBY == True) or (R5Clmn5TBY == True and R5Clmn4T == False and R4Clmn4T == True and R5Clmn3TBY == True and R5Clmn2TBY == True) or (R5Clmn5TBY == True and R4Clmn4T == False and R3Clmn4T == True and R3Clmn3TBY == True and R2Clmn2TBY == True) or (R6Clmn3TBY == True and R5Clmn4T == False and R4Clmn4T == True and R4Clmn5TBY == True and R3Clmn6TBY == True) or (R6Clmn3TBY == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn5TBY == True and R6Clmn6TBY == True) or (R6Clmn5TBY == True and R6Clmn4T == False and R5Clmn4T == True and R6Clmn3TBY == True and R6Clmn2TBY == True) or (R6Clmn5TBY == True and R5Clmn4T == False and R4Clmn4T == True and R4Clmn3TBY == True and R3Clmn2TBY == True) or (R1Clmn4T == False and R2Clmn3TBY == True and R3Clmn2TBY == True and R4Clmn1TBY == True) or (R1Clmn4T == False and R1Clmn3TBY == True and R1Clmn2TBY == True and R1Clmn1TBY == True) or (R2Clmn4T == False and R1Clmn4T == True and R2Clmn5TBY == True and R2Clmn6TBY == True and R2Clmn7TBY == True) or (R2Clmn4T == False and R1Clmn4T == True and R3Clmn5TBY == True and R4Clmn6TBY == True and R5Clmn7TBY == True) or (R3Clmn4T == False and R2Clmn4T == True and R3Clmn5TBY == True and R3Clmn6TBY == True and R3Clmn7TBY == True) or (R3Clmn4T == False and R2Clmn4T == True and R4Clmn5TBY == True and R5Clmn6TBY == True and R6Clmn7TBY == True) or (R4Clmn4T == False and R3Clmn4T == True and R4Clmn5TBY == True and R4Clmn6TBY == True and R4Clmn7TBY == True) or (R4Clmn4T == False and R3Clmn4T == True and R3Clmn5TBY == True and R2Clmn6TBY == True and R1Clmn7TBY == True) and DifficultyChoice >= 2: 
    Botgo = 4
   elif (R6Clmn5T == False and R5Clmn5T == True and R6Clmn4TBY == True and R6Clmn3TBY == True and R6Clmn2TBY == True) or (R5Clmn5T == False and R4Clmn5T == True and R4Clmn4TBY == True and R3Clmn3TBY == True and R2Clmn2TBY == True) or (R5Clmn5T == False and R4Clmn5T == True and R5Clmn4TBY == True and R5Clmn3TBY == True and R5Clmn2TBY == True) or (R6Clmn5T == False and R5Clmn5T == True and R5Clmn4TBY == True and R4Clmn3TBY == True and R3Clmn2TBY == True) or (R1Clmn2TBY == True and R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True) or (R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5T == False) or (R1Clmn5TBY == True and R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5T == False and R3Clmn5T == True) or (R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5T == False and R4Clmn5T == True) or (R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5T == False and R1Clmn5T == True) or (R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5T == False and R4Clmn5T == True) or (R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True and R6Clmn5T == False and R5Clmn5T == True) or (R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True) or (R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5TBY == True and R6Clmn5T == False and R5Clmn5T == True) or (R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5T == False) or (R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True) or (R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5T == False and R1Clmn5T == True) or (R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5T == False and R4Clmn5T == True) or (R6Clmn2TBY == True and R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True) or (R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5T == False and R5Clmn5T == True) or (R1Clmn3TBY == True and R2Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn6TBY == True) or (R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5T == False and R1Clmn6TBY == True) or (R1Clmn7TBY == True and R1Clmn6TBY == True and R1Clmn5T == False and R1Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn6TBY == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn4TBY == True) or (R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn6TBY == True) or (R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn6TBY == True) or (R2Clmn7TBY == True and R3Clmn6TBY == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn4TBY == True) or (R2Clmn7TBY == True and R2Clmn6TBY == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBY == True) or (R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5T == False and R4Clmn5T == True and R6Clmn6TBY == True) or (R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn6TBY == True) or (R3Clmn7TBY == True and R4Clmn6TBY == True and R5Clmn5T == False and R4Clmn5T == True and R6Clmn4TBY == True) or (R3Clmn7TBY == True and R3Clmn6TBY == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn4TBY == True) or (R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5T == False and R1Clmn5T == True and R1Clmn6TBY == True) or (R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn6TBY == True) or (R4Clmn7TBY == True and R3Clmn6TBY == True and R2Clmn5T == False and R1Clmn5T == True and R1Clmn4TBY == True) or (R4Clmn7TBY == True and R4Clmn6TBY == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn4TBY == True) or (R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn6TBY == True) or (R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn6TBY == True) or (R5Clmn7TBY == True and R4Clmn6TBY == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn4TBY == True) or (R5Clmn7TBY == True and R5Clmn6TBY == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn4TBY == True) or (R6Clmn3TBY == True and R5Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn6TBY == True) or (R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn6TBY == True) or (R6Clmn7TBY == True and R5Clmn6TBY == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn4TBY == True) or (R6Clmn7TBY == True and R6Clmn6TBY == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn4TBY == True) or (R1Clmn6TBY == True and R2Clmn5T == False and R1Clmn5T == True and R3Clmn4TBY == True and R4Clmn3TBY == True) or (R1Clmn6TBY == True and R1Clmn5T == False and R1Clmn4TBY == True and R1Clmn3TBY == True) or (R2Clmn4TBY == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn6TBY == True and R2Clmn7TBY == True) or (R2Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn6TBY == True and R5Clmn7TBY == True) or (R2Clmn6TBY == True and R3Clmn5T == False and R2Clmn5T == True and R4Clmn4TBY == True and R5Clmn3TBY == True) or (R2Clmn6TBY == True and R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBY == True and R2Clmn3TBY == True) or (R3Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn6TBY == True and R3Clmn7TBY == True) or (R3Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn6TBY == True and R6Clmn7TBY == True) or (R3Clmn6TBY == True and R4Clmn5T == False and R3Clmn5T == True and R5Clmn4TBY == True and R6Clmn3TBY == True) or (R3Clmn6TBY == True and R3Clmn5T == False and R2Clmn5T == True and R3Clmn4TBY == True and R3Clmn3TBY == True) or (R4Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn6TBY == True and R4Clmn7TBY == True) or (R4Clmn4TBY == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn6TBY == True and R1Clmn7TBY == True) or (R4Clmn6TBY == True and R3Clmn5T == False and R2Clmn5T == True and R2Clmn4TBY == True and R1Clmn3TBY == True) or (R4Clmn6TBY == True and R4Clmn5T == False and R3Clmn5T == True and R4Clmn4TBY == True and R4Clmn3TBY == True) or (R5Clmn4TBY == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn6TBY == True and R5Clmn7TBY == True) or (R5Clmn4TBY == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn6TBY == True and R2Clmn7TBY == True) or (R5Clmn6TBY == True and R4Clmn5T == False and R3Clmn5T == True and R3Clmn4TBY == True and R2Clmn3TBY == True) or (R5Clmn6TBY == True and R5Clmn5T == False and R4Clmn5T == True and R5Clmn4TBY == True and R5Clmn3TBY == True) or (R6Clmn4TBY == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn6TBY == True and R6Clmn7TBY == True) or (R6Clmn4TBY == True and R5Clmn5T == False and R4Clmn5T == True and R4Clmn6TBY == True and R3Clmn7TBY == True) or (R6Clmn6TBY == True and R5Clmn5T == False and R4Clmn5T == True and R4Clmn4TBY == True and R3Clmn3TBY == True) or (R6Clmn6TBY == True and R6Clmn5T == False and R5Clmn5T == True and R6Clmn4TBY == True and R6Clmn3TBY == True) or (R1Clmn5T == False and R2Clmn4TBY == True and R3Clmn3TBY == True and R4Clmn2TBY == True) or (R1Clmn5T == False and R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2TBY == True) or (R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn5T == False and R1Clmn5T == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R3Clmn5T == False and R2Clmn5T == True and R3Clmn4TBY == True and R3Clmn3TBY == True and R3Clmn2TBY == True) or (R3Clmn5T == False and R2Clmn5T == True and R4Clmn4TBY == True and R5Clmn3TBY == True and R6Clmn2TBY == True) or (R4Clmn5T == False and R3Clmn5T == True and R4Clmn4TBY == True and R4Clmn3TBY == True and R4Clmn2TBY == True) or (R4Clmn5T == False and R3Clmn5T == True and R3Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2TBY == True) and DifficultyChoice >= 2: 
    Botgo = 5
   elif (R6Clmn6T == False and R5Clmn6T == True and R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True) or (R6Clmn6T == False and R5Clmn6T == True and R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True) or (R5Clmn6T == False and R4Clmn6T == True and R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True) or (R5Clmn6T == False and R4Clmn6T == True and R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True) or (R1Clmn3TBY == True and R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6T == False and R3Clmn6T == True) or (R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5TBY == True and R1Clmn6T == False) or (R1Clmn6TBY == True and R2Clmn6TBY == True and R3Clmn6TBY == True and R4Clmn6T == False and R3Clmn6T == True) or (R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6T == False and R4Clmn6T == True) or (R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6T == False and R1Clmn6T == True) or (R2Clmn6TBY == True and R3Clmn6TBY == True and R4Clmn6TBY == True and R5Clmn6T == False and R4Clmn6T == True) or (R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True and R6Clmn6T == False and R5Clmn6T == True) or (R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6T == False and R2Clmn6T == True) or (R3Clmn6TBY == True and R4Clmn6TBY == True and R5Clmn6TBY == True and R6Clmn6T == False and R5Clmn6T == True) or (R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6T == False) or (R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6T == False and R3Clmn6T == True) or (R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6T == False and R1Clmn6T == True) or (R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6T == False and R4Clmn6T == True) or (R6Clmn3TBY == True and R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6T == False and R2Clmn6T == True) or (R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6T == False and R5Clmn6T == True) or (R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6T == False and R1Clmn6T == True and R2Clmn7TBY == True) or (R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6T == False and R3Clmn6T == True and R5Clmn7TBY == True) or (R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6T == False and R2Clmn6T == True and R3Clmn7TBY == True) or (R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6T == False and R4Clmn6T == True and R6Clmn7TBY == True) or (R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6T == False and R3Clmn6T == True and R4Clmn7TBY == True) or (R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6T == False and R1Clmn6T == True and R1Clmn6T == True and R1Clmn7TBY == True) or (R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6T == False and R4Clmn6T == True and R5Clmn7TBY == True) or (R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6T == False and R2Clmn6T == True and R2Clmn7TBY == True) or (R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6T == False and R5Clmn6T == True and R6Clmn7TBY == True) or (R6Clmn4TBY == True and R5Clmn5TBY == True and R4Clmn6T == False and R3Clmn6T == True and R3Clmn7TBY == True) or (R1Clmn7TBY == True and R1Clmn6T == False and R1Clmn5TBY == True and R1Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn6T == False and R1Clmn6T == True and R3Clmn5TBY == True and R4Clmn4TBY == True) or (R2Clmn7TBY == True and R3Clmn6T == False and R2Clmn6T == True and R4Clmn5TBY == True and R5Clmn4TBY == True) or (R2Clmn7TBY == True and R2Clmn6T == False and R1Clmn6T == True and R2Clmn5TBY == True and R2Clmn4TBY == True) or (R3Clmn7TBY == True and R4Clmn6T == False and R3Clmn6T == True and R5Clmn5TBY == True and R6Clmn4TBY == True) or (R3Clmn7TBY == True and R3Clmn6T == False and R2Clmn6T == True and R3Clmn5TBY == True and R3Clmn4TBY == True) or (R4Clmn7TBY == True and R3Clmn6T == False and R2Clmn6T == True and R2Clmn5TBY == True and R1Clmn4TBY == True) or (R4Clmn7TBY == True and R4Clmn6T == False and R3Clmn6T == True and R4Clmn5TBY == True and R4Clmn4TBY == True) or (R5Clmn7TBY == True and R4Clmn6T == False and R3Clmn6T == True and R3Clmn5TBY == True and R2Clmn4TBY == True) or (R5Clmn7TBY == True and R5Clmn6T == False and R4Clmn6T == True and R5Clmn5TBY == True and R5Clmn4TBY == True) or (R6Clmn7TBY == True and R5Clmn6T == False and R4Clmn6T == True and R4Clmn5TBY == True and R3Clmn4TBY == True) or (R6Clmn7TBY == True and R6Clmn6T == False and R5Clmn6T == True and R6Clmn5TBY == True and R6Clmn4TBY == True) or (R1Clmn6T == False and R2Clmn5TBY == True and R3Clmn4TBY == True and R4Clmn3TBY == True) or (R1Clmn6T == False and R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3TBY == True) or (R2Clmn6T == False and R1Clmn6T == True and R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True) or (R2Clmn6T == False and R1Clmn6T == True and R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True) or (R3Clmn6T == False and R2Clmn6T == True and R4Clmn5TBY == True and R5Clmn4TBY == True and R6Clmn3TBY == True) or (R3Clmn6T == False and R2Clmn6T == True and R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True) or (R4Clmn6T == False and R3Clmn6T == True and R3Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3TBY == True) or (R4Clmn6T == False and R3Clmn6T == True and R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True) and DifficultyChoice >= 2: 
    Botgo = 6
   elif (R6Clmn7T == False and R5Clmn7T == True and R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True) or (R6Clmn7T == False and R5Clmn7T == True and R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True) or (R5Clmn7T == False and R4Clmn7T == True and R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True) or (R5Clmn7T == False and R4Clmn7T == True and R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn7TBY == True and R3Clmn7TBY == True and R4Clmn7T == False and R3Clmn7T == True) or (R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True and R2Clmn7T == False and R1Clmn7T == True) or (R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True and R5Clmn7T == False and R4Clmn7T == True) or (R2Clmn7TBY == True and R3Clmn7TBY == True and R4Clmn7TBY == True and R5Clmn7T == False and R4Clmn7T == True) or (R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True and R3Clmn7T == False and R2Clmn7T == True) or (R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True and R6Clmn7T == False and R5Clmn7T == True) or (R3Clmn7TBY == True and R4Clmn7TBY == True and R5Clmn7TBY == True and R6Clmn7T == False and R5Clmn7T == True) or (R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True and R4Clmn7T == False and R3Clmn7T == True) or (R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True and R1Clmn7T == False) or (R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True and R5Clmn7T == False and R4Clmn7T == True) or (R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True and R2Clmn7T == False and R1Clmn7T == True) or (R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True and R6Clmn7T == False and R5Clmn7T == True) or (R6Clmn4TBY == True and R5Clmn5TBY == True and R4Clmn6TBY == True and R3Clmn7T == False and R2Clmn7T == True) or (R1Clmn7T == False and R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4TBY == True) or (R1Clmn7T == False and R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True) or (R2Clmn7T == False and R1Clmn7T == True and R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True) or (R2Clmn7T == False and R1Clmn7T == True and R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True) or (R3Clmn7T == False and R2Clmn7T == True and R4Clmn6TBY == True and R5Clmn5TBY == True and R6Clmn4TBY == True) or (R3Clmn7T == False and R2Clmn7T == True and R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True) or (R4Clmn7T == False and R3Clmn7T == True and R3Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4TBY == True) or (R4Clmn7T == False and R3Clmn7T == True and R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True) and DifficultyChoice >= 2: 
    Botgo = 7
   elif (R4Clmn1T == True and R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True) or (R4Clmn1T == True and R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True) or (R3Clmn1T == True and R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True) or (R3Clmn1T == True and R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True) or (R2Clmn1T == True and R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True) or (R2Clmn1T == True and R3Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4TBY == True) or (R1Clmn1T == True and R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True) or (R1Clmn1T == True and R4Clmn2TBY == True and R5Clmn3TBY == True and R6Clmn4TBY == True) or (R1Clmn1T == False and R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True) or (R1Clmn1T == False and R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True) or (R1Clmn4TBY == True and R2Clmn3TBY == True and R3Clmn2TBY == True and R2Clmn1T == True) and DifficultyChoice == 3: 
    if R6Clmn2T and R6Clmn3T and R6Clmn4T and R6Clmn5T and R6Clmn6T and R6Clmn7T == True:
     Botgo = 1
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 1:
      Botgo = random.randrange(1,8)
   elif (R4Clmn2T == True and R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True) or (R4Clmn2T == True and R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True) or (R3Clmn2T == True and R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True) or (R3Clmn2T == True and R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True) or (R1Clmn5TBY == True and R2Clmn4TBY == True and R3Clmn3TBY == True and R2Clmn2T == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2T == False) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2T == False) or (R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True and R1Clmn2T == True) or (R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True and R4Clmn2T == True) or (R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True and R2Clmn2T == True) or (R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True and R3Clmn2T == True) or (R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True and R1Clmn2T == False) or (R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True and R4Clmn2T == True) or (R6Clmn5TBY == True and R5Clmn4TBY == True and R4Clmn3TBY == True and R1Clmn2T == True) or (R1Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2T == True and R4Clmn1TBY == True) or (R1Clmn1TBY == True and R1Clmn2T == False and R3Clmn3TBY == True and R4Clmn4TBY == True) or (R2Clmn1TBY == True and R1Clmn2T == True and R4Clmn3TBY == True and R5Clmn4TBY == True) or (R2Clmn1TBY == True and R1Clmn2T == False and R2Clmn3TBY == True and R2Clmn4TBY == True) or (R3Clmn1TBY == True and R2Clmn2T == True and R5Clmn3TBY == True and R6Clmn4TBY == True) or (R3Clmn1TBY == True and R1Clmn2T == True and R3Clmn3TBY == True and R3Clmn4TBY == True) or (R4Clmn1TBY == True and R1Clmn2T == True and R2Clmn3TBY == True and R1Clmn4TBY == True) or (R4Clmn1TBY == True and R2Clmn2T == True and R4Clmn3TBY == True and R4Clmn4TBY == True) or (R5Clmn1TBY == True and R2Clmn2T == True and R3Clmn3TBY == True and R2Clmn4TBY == True) or (R5Clmn1TBY == True and R3Clmn2T == True and R5Clmn3TBY == True and R5Clmn4TBY == True) or (R6Clmn1TBY == True and R3Clmn2T == True and R4Clmn3TBY == True and R3Clmn4TBY == True) or (R6Clmn1TBY == True and R4Clmn2T == True and R6Clmn3TBY == True and R6Clmn4TBY == True) or (R1Clmn2T == False and R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R1Clmn2T == False and R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True) or (R1Clmn2T == True and R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R1Clmn2T == True and R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True) or (R2Clmn2T == True and R3Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5TBY == True) or (R2Clmn2T == True and R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True) and DifficultyChoice == 3:
    if R6Clmn1T and R6Clmn3T and R6Clmn4T and R6Clmn5T and R6Clmn6T and R6Clmn7T == True:
     Botgo = 2
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 2:
      Botgo = random.randrange(1,8)
   elif (R4Clmn3T == True and R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True) or (R3Clmn3T == True and R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True) or (R3Clmn3T == True and R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True) or (R4Clmn3T == True and R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True) or (R1Clmn6TBY == True and R2Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3T == True) or (R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3T == True) or (R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3T == False) or (R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True and R4Clmn3T == True) or (R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True and R1Clmn3T == True) or (R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True and R2Clmn3T == True) or (R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True and R1Clmn3T == False) or (R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True and R3Clmn3T == True) or (R6Clmn6TBY == True and R5Clmn5TBY == True and R4Clmn4TBY == True and R1Clmn3T == True) or (R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True and R4Clmn3T == True) or (R1Clmn1TBY == True and R2Clmn2TBY == True and R1Clmn3T == True and R4Clmn4TBY == True) or (R1Clmn3TBY == True and R2Clmn3TBY == True and R1Clmn3T == True and R4Clmn3TBY == True) or (R1Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3T == True and R4Clmn2TBY == True) or (R2Clmn1TBY == True and R3Clmn2TBY == True and R2Clmn3T == True and R5Clmn4TBY == True) or (R2Clmn1TBY == True and R2Clmn2TBY == True and R1Clmn3T == False and R2Clmn4TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3T == False and R2Clmn2TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3T == False and R2Clmn2TBY == True) or (R3Clmn1TBY == True and R4Clmn2TBY == True and R3Clmn3T == True and R6Clmn4TBY == True) or (R3Clmn1TBY == True and R3Clmn2TBY == True and R1Clmn3T == True and R3Clmn4TBY == True) or (R3Clmn5TBY == True and R3Clmn4TBY == True and R1Clmn3T == True and R3Clmn2TBY == True) or (R3Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3T == True and R6Clmn2TBY == True) or (R4Clmn1TBY == True and R3Clmn2TBY == True and R1Clmn3T == False and R1Clmn4TBY == True) or (R4Clmn1TBY == True and R4Clmn2TBY == True and R2Clmn3T == True and R4Clmn4TBY == True) or (R4Clmn5TBY == True and R4Clmn4TBY == True and R2Clmn3T == True and R4Clmn2TBY == True) or (R4Clmn5TBY == True and R3Clmn4TBY == True and R1Clmn3T == False and R1Clmn2TBY == True) or (R5Clmn1TBY == True and R4Clmn2TBY == True and R1Clmn3T == True and R2Clmn4TBY == True) or (R5Clmn1TBY == True and R5Clmn2TBY == True and R3Clmn3T == True and R5Clmn4TBY == True) or (R5Clmn5TBY == True and R5Clmn4TBY == True and R3Clmn3T == True and R5Clmn2TBY == True) or (R5Clmn5TBY == True and R4Clmn4TBY == True and R1Clmn3T == True and R2Clmn2TBY == True) or (R6Clmn1TBY == True and R5Clmn2TBY == True and R2Clmn3T == True and R3Clmn4TBY == True) or (R6Clmn1TBY == True and R6Clmn2TBY == True and R4Clmn3T == True and R6Clmn4TBY == True) or (R6Clmn5TBY == True and R6Clmn4TBY == True and R4Clmn3T == True and R6Clmn2TBY == True) or (R6Clmn5TBY == True and R5Clmn4TBY == True and R2Clmn3T == True and R3Clmn2TBY == True) or (R1Clmn2TBY == True and R1Clmn3T == False and R3Clmn4TBY == True and R4Clmn5TBY == True) or (R1Clmn3TBY == True and R1Clmn3T == False and R3Clmn3TBY == True and R4Clmn3TBY == True) or (R1Clmn4TBY == True and R1Clmn3T == False and R3Clmn2TBY == True and R4Clmn1TBY == True) or (R2Clmn2TBY == True and R1Clmn3T == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R2Clmn2TBY == True and R1Clmn3T == False and R2Clmn4TBY == True and R2Clmn5TBY == True) or (R3Clmn2TBY == True and R2Clmn3T == True and R5Clmn4TBY == True and R6Clmn5TBY == True) or (R3Clmn2TBY == True and R1Clmn3T == True and R3Clmn4TBY == True and R3Clmn5TBY == True) or (R4Clmn2TBY == True and R2Clmn3T == True and R2Clmn4TBY == True and R1Clmn5TBY == True) or (R4Clmn2TBY == True and R2Clmn3T == True and R4Clmn4TBY == True and R4Clmn5TBY == True) or (R5Clmn2TBY == True and R2Clmn3T == True and R3Clmn4TBY == True and R2Clmn5TBY == True) or (R5Clmn2TBY == True and R3Clmn3T == True and R5Clmn4TBY == True and R5Clmn5TBY == True) or (R6Clmn2TBY == True and R3Clmn3T == True and R4Clmn4TBY == True and R3Clmn5TBY == True) or (R6Clmn2TBY == True and R4Clmn3T == True and R6Clmn4TBY == True and R6Clmn5TBY == True) or (R1Clmn3T == False and R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True) or (R1Clmn3T == False and R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True) or (R1Clmn3T == True and R4Clmn4TBY == True and R5Clmn5TBY == True and R6Clmn6TBY == True) or (R1Clmn3T == True and R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True) or (R2Clmn3T == True and R3Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6TBY == True) or (R2Clmn3T == True and R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True) and DifficultyChoice == 3: 
    if R6Clmn1T and R6Clmn2T and R6Clmn4T and R6Clmn5T and R6Clmn6T and R6Clmn7T == True:
     Botgo = 3
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 3:
      Botgo = random.randrange(1,8)
   elif (R4Clmn4T == True and R6Clmn5TBY == True and R6Clmn6TBY == True and R6Clmn7TBY == True) or (R4Clmn4T == True and R5Clmn5TBY == True and R4Clmn6TBY == True and R3Clmn7TBY == True) or (R3Clmn4T == True and R4Clmn5TBY == True and R3Clmn6TBY == True and R2Clmn7TBY == True) or (R3Clmn4T == True and R5Clmn5TBY == True and R5Clmn6TBY == True and R5Clmn7TBY == True) or (R1Clmn1TBY == True and R2Clmn2TBY == True and R3Clmn3TBY == True) or (R1Clmn7TBY == True and R2Clmn6TBY == True and R3Clmn5TBY == True) or (R2Clmn1TBY == True and R3Clmn2TBY == True and R4Clmn3TBY == True) or (R2Clmn1TBY == True and R2Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4T == False) or (R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4TBY == True and R3Clmn4T == True) or (R2Clmn7TBY == True and R3Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4T == True) or (R2Clmn7TBY == True and R2Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4T == False) or (R3Clmn1TBY == True and R4Clmn2TBY == True and R5Clmn3TBY == True and R4Clmn4T == True) or (R3Clmn1TBY == True and R3Clmn2TBY == True and R3Clmn3TBY == True and R1Clmn4T == True) or (R3Clmn7TBY == True and R4Clmn6TBY == True and R5Clmn5TBY == True and R4Clmn4T == True) or (R3Clmn7TBY == True and R3Clmn6TBY == True and R3Clmn5TBY == True and R1Clmn4T == True) or (R4Clmn1TBY == True and R4Clmn2TBY == True and R4Clmn3TBY == True and R2Clmn4T == True) or (R4Clmn7TBY == True and R4Clmn6TBY == True and R4Clmn5TBY == True and R2Clmn4T == True) or (R5Clmn1TBY == True and R4Clmn2TBY == True and R3Clmn3TBY == True and R1Clmn4T == False) or (R5Clmn1TBY == True and R5Clmn2TBY == True and R5Clmn3TBY == True and R3Clmn4T == True) or (R5Clmn7TBY == True and R4Clmn6TBY == True and R3Clmn5TBY == True and R1Clmn4T == False) or (R5Clmn7TBY == True and R5Clmn6TBY == True and R5Clmn5TBY == True and R3Clmn4T == True) or (R6Clmn1TBY == True and R5Clmn2TBY == True and R4Clmn3TBY == True and R1Clmn4T == True) or (R6Clmn1TBY == True and R6Clmn2TBY == True and R6Clmn3TBY == True and R4Clmn4T == True) or (R6Clmn7TBY == True and R5Clmn6TBY == True and R4Clmn5TBY == True and R1Clmn4T == True) or (R6Clmn7TBY == True and R6Clmn6TBY == True and R6Clmn5TBY == True and R4Clmn4T == True) or (R1Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4T == True and R4Clmn5TBY == True) or (R1Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4T == True and R4Clmn3TBY == True) or (R2Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4T == True and R5Clmn5TBY == True) or (R2Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4T == False and R2Clmn5TBY == True) or (R2Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4T == True and R5Clmn3TBY == True) or (R2Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4T == False and R2Clmn3TBY == True) or (R3Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4T == True and R6Clmn5TBY == True) or (R3Clmn2TBY == True and R3Clmn3TBY == True and R1Clmn4T == True and R3Clmn5TBY == True) or (R3Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4T == True and R6Clmn3TBY == True) or (R3Clmn6TBY == True and R3Clmn5TBY == True and R1Clmn4T == True and R3Clmn3TBY == True) or (R4Clmn2TBY == True and R3Clmn3TBY == True and R1Clmn4T == False and R1Clmn5TBY == True) or (R4Clmn2TBY == True and R4Clmn3TBY == True and R2Clmn4T == True and R4Clmn5TBY == True) or (R4Clmn6TBY == True and R3Clmn5TBY == True and R1Clmn4T == False and R1Clmn3TBY == True) or (R4Clmn6TBY == True and R4Clmn5TBY == True and R2Clmn4T == True and R4Clmn3TBY == True) or (R5Clmn2TBY == True and R4Clmn3TBY == True and R1Clmn4T == True and R2Clmn5TBY == True) or (R5Clmn2TBY == True and R5Clmn3TBY == True and R3Clmn4T == True and R5Clmn5TBY == True) or (R5Clmn6TBY == True and R4Clmn5TBY == True and R1Clmn4T == True and R2Clmn3TBY == True) or (R5Clmn6TBY == True and R5Clmn5TBY == True and R3Clmn4T == True and R5Clmn3TBY == True) or (R6Clmn2TBY == True and R5Clmn3TBY == True and R2Clmn4T == True and R3Clmn5TBY == True) or (R6Clmn2TBY == True and R6Clmn3TBY == True and R4Clmn4T == True and R6Clmn5TBY == True) or (R6Clmn6TBY == True and R5Clmn5TBY == True and R2Clmn4T == True and R3Clmn3TBY == True) or (R6Clmn6TBY == True and R6Clmn5TBY == True and R4Clmn4T == True and R6Clmn3TBY == True) or (R1Clmn3TBY == True and R1Clmn4T == False and R3Clmn5TBY == True and R4Clmn6TBY == True) or (R1Clmn5TBY == True and R1Clmn4T == False and R3Clmn3TBY == True and R4Clmn2TBY == True) or (R2Clmn3TBY == True and R1Clmn4T == True and R4Clmn5TBY == True and R5Clmn6TBY == True) or (R2Clmn3TBY == True and R1Clmn4T == False and R2Clmn5TBY == True and R2Clmn6TBY == True) or (R2Clmn5TBY == True and R1Clmn4T == False and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn5TBY == True and R1Clmn4T == True and R4Clmn3TBY == True and R5Clmn2TBY == True) or (R3Clmn3TBY == True and R2Clmn4T == True and R5Clmn5TBY == True and R6Clmn6TBY == True) or (R3Clmn3TBY == True and R1Clmn4T == True and R3Clmn5TBY == True and R3Clmn6TBY == True) or (R3Clmn5TBY == True and R1Clmn4T == True and R3Clmn3TBY == True and R3Clmn2TBY == True) or (R3Clmn5TBY == True and R2Clmn4T == True and R5Clmn3TBY == True and R6Clmn2TBY == True) or (R4Clmn3TBY == True and R1Clmn4T == True and R2Clmn5TBY == True and R1Clmn6TBY == True) or (R4Clmn3TBY == True and R2Clmn4T == True and R4Clmn5TBY == True and R4Clmn6TBY == True) or (R4Clmn5TBY == True and R2Clmn4T == True and R4Clmn3TBY == True and R4Clmn2TBY == True) or (R4Clmn5TBY == True and R1Clmn4T == True and R2Clmn3TBY == True and R1Clmn2TBY == True) or (R5Clmn3TBY == True and R2Clmn4T == True and R3Clmn5TBY == True and R2Clmn6TBY == True) or (R5Clmn3TBY == True and R3Clmn4T == True and R5Clmn5TBY == True and R5Clmn6TBY == True) or (R5Clmn5TBY == True and R3Clmn4T == True and R5Clmn3TBY == True and R5Clmn2TBY == True) or (R5Clmn5TBY == True and R2Clmn4T == True and R3Clmn3TBY == True and R2Clmn2TBY == True) or (R6Clmn3TBY == True and R3Clmn4T == True and R4Clmn5TBY == True and R3Clmn6TBY == True) or (R6Clmn3TBY == True and R4Clmn4T == True and R6Clmn5TBY == True and R6Clmn6TBY == True) or (R6Clmn5TBY == True and R4Clmn4T == True and R6Clmn3TBY == True and R6Clmn2TBY == True) or (R6Clmn5TBY == True and R3Clmn4T == True and R4Clmn3TBY == True and R3Clmn2TBY == True) or (R1Clmn4T == False and R2Clmn5TBY == True and R2Clmn6TBY == True and R2Clmn7TBY == True) or (R1Clmn4T == False and R3Clmn5TBY == True and R4Clmn6TBY == True and R5Clmn7TBY == True) or (R1Clmn4T == True and R3Clmn5TBY == True and R3Clmn6TBY == True and R3Clmn7TBY == True) or (R1Clmn4T == True and R4Clmn5TBY == True and R5Clmn6TBY == True and R6Clmn7TBY == True) or (R2Clmn4T == True and R4Clmn5TBY == True and R4Clmn6TBY == True and R4Clmn7TBY == True) or (R2Clmn4T == True and R3Clmn5TBY == True and R2Clmn6TBY == True and R1Clmn7TBY == True) and DifficultyChoice == 3: 
    if R6Clmn1T and R6Clmn2T and R6Clmn3T and R6Clmn5T and R6Clmn6T and R6Clmn7T == True:
     Botgo = 4
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 4:
      Botgo = random.randrange(1,8)
   elif (R4Clmn5T == True and R6Clmn4TBY == True and R6Clmn3TBY == True and R6Clmn2TBY == True) or (R3Clmn5T == True and R4Clmn4TBY == True and R3Clmn3TBY == True and R2Clmn2TBY == True) or (R3Clmn5T == True and R5Clmn4TBY == True and R5Clmn3TBY == True and R5Clmn2TBY == True) or (R4Clmn5T == True and R5Clmn4TBY == True and R4Clmn3TBY == True and R3Clmn2TBY == True) or (R1Clmn2TBY == True and R2Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5T == True) or (R1Clmn5TBY == True and R2Clmn5TBY == True and R3Clmn5TBY == True and R2Clmn5T == True) or (R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5T == True) or (R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5T == False) or (R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5TBY == True and R3Clmn5T == True) or (R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True and R4Clmn5T == True) or (R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True and R1Clmn5T == True) or (R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5TBY == True and R4Clmn5T == True) or (R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True and R2Clmn5T == True) or (R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True and R1Clmn5T == False) or (R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True and R3Clmn5T == True) or (R6Clmn2TBY == True and R5Clmn3TBY == True and R4Clmn4TBY == True and R1Clmn5T == True) or (R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True and R4Clmn5T == True) or (R1Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5T == True and R4Clmn6TBY == True) or (R1Clmn7TBY == True and R2Clmn6TBY == True and R1Clmn5T == True and R4Clmn4TBY == True) or (R2Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5T == True and R5Clmn6TBY == True) or (R2Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5T == False and R2Clmn6TBY == True) or (R2Clmn7TBY == True and R3Clmn6TBY == True and R2Clmn5T == True and R5Clmn4TBY == True) or (R2Clmn7TBY == True and R2Clmn6TBY == True and R1Clmn5T == False and R2Clmn4TBY == True) or (R3Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5T == True and R6Clmn6TBY == True) or (R3Clmn3TBY == True and R3Clmn4TBY == True and R1Clmn5T == True and R3Clmn6TBY == True) or (R3Clmn7TBY == True and R4Clmn6TBY == True and R3Clmn5T == True and R6Clmn4TBY == True) or (R3Clmn7TBY == True and R3Clmn6TBY == True and R1Clmn5T == True and R3Clmn4TBY == True) or (R4Clmn3TBY == True and R3Clmn4TBY == True and R1Clmn5T == False and R1Clmn6TBY == True) or (R4Clmn3TBY == True and R4Clmn4TBY == True and R2Clmn5T == True and R4Clmn6TBY == True) or (R4Clmn7TBY == True and R3Clmn6TBY == True and R1Clmn5T == False and R1Clmn4TBY == True) or (R4Clmn7TBY == True and R4Clmn6TBY == True and R2Clmn5T == True and R4Clmn4TBY == True) or (R5Clmn3TBY == True and R4Clmn4TBY == True and R1Clmn5T == True and R2Clmn6TBY == True) or (R5Clmn3TBY == True and R5Clmn4TBY == True and R3Clmn5T == True and R5Clmn6TBY == True) or (R5Clmn7TBY == True and R4Clmn6TBY == True and R1Clmn5T == True and R2Clmn4TBY == True) or (R5Clmn7TBY == True and R5Clmn6TBY == True and R3Clmn5T == True and R5Clmn4TBY == True) or (R6Clmn3TBY == True and R5Clmn4TBY == True and R2Clmn5T == True and R3Clmn6TBY == True) or (R6Clmn3TBY == True and R6Clmn4TBY == True and R4Clmn5T == True and R6Clmn6TBY == True) or (R6Clmn7TBY == True and R5Clmn6TBY == True and R2Clmn5T == True and R3Clmn4TBY == True) or (R6Clmn7TBY == True and R6Clmn6TBY == True and R4Clmn5T == True and R6Clmn4TBY == True) or (R1Clmn6TBY == True and R1Clmn5T == False and R3Clmn4TBY == True and R4Clmn3TBY == True) or (R2Clmn4TBY == True and R1Clmn5T == False and R2Clmn6TBY == True and R2Clmn7TBY == True) or (R2Clmn4TBY == True and R1Clmn5T == True and R4Clmn6TBY == True and R5Clmn7TBY == True) or (R2Clmn6TBY == True and R1Clmn5T == True and R4Clmn4TBY == True and R5Clmn3TBY == True) or (R2Clmn6TBY == True and R1Clmn5T == False and R2Clmn4TBY == True and R2Clmn3TBY == True) or (R3Clmn4TBY == True and R1Clmn5T == True and R3Clmn6TBY == True and R3Clmn7TBY == True) or (R3Clmn4TBY == True and R2Clmn5T == True and R5Clmn6TBY == True and R6Clmn7TBY == True) or (R3Clmn6TBY == True and R2Clmn5T == True and R5Clmn4TBY == True and R6Clmn3TBY == True) or (R3Clmn6TBY == True and R1Clmn5T == True and R3Clmn4TBY == True and R3Clmn3TBY == True) or (R4Clmn4TBY == True and R2Clmn5T == True and R4Clmn6TBY == True and R4Clmn7TBY == True) or (R4Clmn4TBY == True and R1Clmn5T == True and R2Clmn6TBY == True and R1Clmn7TBY == True) or (R4Clmn6TBY == True and R1Clmn5T == True and R2Clmn4TBY == True and R1Clmn3TBY == True) or (R4Clmn6TBY == True and R2Clmn5T == True and R4Clmn4TBY == True and R4Clmn3TBY == True) or (R5Clmn4TBY == True and R3Clmn5T == True and R5Clmn6TBY == True and R5Clmn7TBY == True) or (R5Clmn4TBY == True and R2Clmn5T == True and R3Clmn6TBY == True and R2Clmn7TBY == True) or (R5Clmn6TBY == True and R2Clmn5T == True and R3Clmn4TBY == True and R2Clmn3TBY == True) or (R5Clmn6TBY == True and R3Clmn5T == True and R5Clmn4TBY == True and R5Clmn3TBY == True) or (R6Clmn4TBY == True and R4Clmn5T == True and R6Clmn6TBY == True and R6Clmn7TBY == True) or (R6Clmn4TBY == True and R3Clmn5T == True and R4Clmn6TBY == True and R3Clmn7TBY == True) or (R6Clmn6TBY == True and R3Clmn5T == True and R4Clmn4TBY == True and R3Clmn3TBY == True) or (R6Clmn6TBY == True and R4Clmn5T == True and R6Clmn4TBY == True and R6Clmn3TBY == True) or (R1Clmn5T == False and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R1Clmn5T == False and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R1Clmn5T == True and R3Clmn4TBY == True and R3Clmn3TBY == True and R3Clmn2TBY == True) or (R1Clmn5T == True and R4Clmn4TBY == True and R5Clmn3TBY == True and R6Clmn2TBY == True) or (R2Clmn5T == True and R4Clmn4TBY == True and R4Clmn3TBY == True and R4Clmn2TBY == True) or (R2Clmn5T == True and R3Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2TBY == True) and DifficultyChoice == 3: 
    if R6Clmn1T and R6Clmn2T and R6Clmn3T and R6Clmn4T and R6Clmn6T and R6Clmn7T == True:
     Botgo = 5
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 5:
      Botgo = random.randrange(1,8)
   elif (R4Clmn6T == True and R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True) or (R4Clmn6T == True and R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True) or (R3Clmn6T == True and R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True) or (R3Clmn6T == True and R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True) or (R1Clmn3TBY == True and R2Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6T == True) or (R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6T == True) or (R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6T == False) or (R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True and R4Clmn6T == True) or (R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True and R1Clmn6T == True) or (R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True and R2Clmn6T == True) or (R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True and R1Clmn6T == False) or (R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True and R3Clmn6T == True) or (R6Clmn3TBY == True and R5Clmn4TBY == True and R4Clmn5TBY == True and R1Clmn6T == True) or (R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True and R4Clmn6T == True) or (R2Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6T == False and R2Clmn7TBY == True) or (R2Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6T == True and R5Clmn7TBY == True) or (R3Clmn4TBY == True and R3Clmn5TBY == True and R1Clmn6T == True and R3Clmn7TBY == True) or (R3Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6T == True and R6Clmn7TBY == True) or (R4Clmn4TBY == True and R4Clmn5TBY == True and R2Clmn6T == True and R4Clmn7TBY == True) or (R4Clmn4TBY == True and R3Clmn5TBY == True and R1Clmn6T == False and R1Clmn7TBY == True) or (R5Clmn4TBY == True and R5Clmn5TBY == True and R3Clmn6T == True and R5Clmn7TBY == True) or (R5Clmn4TBY == True and R4Clmn5TBY == True and R1Clmn6T == True and R2Clmn7TBY == True) or (R6Clmn4TBY == True and R6Clmn5TBY == True and R4Clmn6T == True and R6Clmn7TBY == True) or (R6Clmn4TBY == True and R5Clmn5TBY == True and R2Clmn6T == True and R3Clmn7TBY == True) or (R1Clmn7TBY == True and R1Clmn6T == False and R3Clmn5TBY == True and R4Clmn4TBY == True) or (R2Clmn7TBY == True and R1Clmn6T == True and R4Clmn5TBY == True and R5Clmn4TBY == True) or (R2Clmn7TBY == True and R1Clmn6T == False and R2Clmn5TBY == True and R2Clmn4TBY == True) or (R3Clmn7TBY == True and R2Clmn6T == True and R5Clmn5TBY == True and R6Clmn4TBY == True) or (R3Clmn7TBY == True and R1Clmn6T == True and R3Clmn5TBY == True and R3Clmn4TBY == True) or (R4Clmn7TBY == True and R1Clmn6T == True and R2Clmn5TBY == True and R1Clmn4TBY == True) or (R4Clmn7TBY == True and R2Clmn6T == True and R4Clmn5TBY == True and R4Clmn4TBY == True) or (R5Clmn7TBY == True and R2Clmn6T == True and R3Clmn5TBY == True and R2Clmn4TBY == True) or (R5Clmn7TBY == True and R3Clmn6T == True and R5Clmn5TBY == True and R5Clmn4TBY == True) or (R6Clmn7TBY == True and R3Clmn6T == True and R4Clmn5TBY == True and R3Clmn4TBY == True) or (R6Clmn7TBY == True and R4Clmn6T == True and R6Clmn5TBY == True and R6Clmn4TBY == True) or (R1Clmn6T == False and R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True) or (R1Clmn6T == False and R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True) or (R1Clmn6T == True and R4Clmn5TBY == True and R5Clmn4TBY == True and R6Clmn3TBY == True) or (R1Clmn6T == True and R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True) or (R2Clmn6T == True and R3Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3TBY == True) or (R2Clmn6T == True and R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True) and DifficultyChoice == 3: 
    if R6Clmn1T and R6Clmn2T and R6Clmn3T and R6Clmn4T and R6Clmn5T and R6Clmn7T == True:
     Botgo = 6
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 6:
      Botgo = random.randrange(1,8)
   elif (R4Clmn7T == True and R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True) or (R4Clmn7T == True and R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True) or (R3Clmn7T == True and R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True) or (R3Clmn7T == True and R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True) or (R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True and R1Clmn7T == False) or (R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True and R3Clmn7T == True) or (R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True and R1Clmn7T == True) or (R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True and R4Clmn7T == True) or (R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True and R2Clmn7T == True) or (R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True and R3Clmn7T == True) or (R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True and R1Clmn7T == False) or (R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True and R4Clmn7T == True) or (R6Clmn4TBY == True and R5Clmn5TBY == True and R4Clmn6TBY == True and R1Clmn7T == True) or (R1Clmn7T == False and R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True) or (R1Clmn7T == False and R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True) or (R1Clmn7T == True and R4Clmn6TBY == True and R5Clmn5TBY == True and R6Clmn4TBY == True) or (R1Clmn7T == True and R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True) or (R2Clmn7T == True and R3Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4TBY == True) or (R2Clmn7T == True and R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True) and DifficultyChoice == 3: 
    if R6Clmn1T and R6Clmn2T and R6Clmn3T and R6Clmn4T and R6Clmn5T and R6Clmn6T == True:
     Botgo = 7
    else:
     Botgo = random.randrange(1,8)
     while Botgo == 7:
      Botgo = random.randrange(1,8)
   else:
    Botgo = random.randrange(1,8)
   if Botgo == 1:
    if R1Clmn1T == False:
     Sd1 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 1")
     R1Clmn1TBB = True
     R1Clmn1T = True
     time.sleep(1)
    elif R1Clmn1T == True:
     if R2Clmn1T == False:
      Sd8 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 1")
      R2Clmn1TBB = True
      R2Clmn1T = True
      time.sleep(1)
     elif R2Clmn1T == True:
      if R3Clmn1T == False:
       Sd15 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 1")
       R3Clmn1TBB = True
       R3Clmn1T = True
       time.sleep(1)
      elif R3Clmn1T == True:
       if R4Clmn1T == False:
        Sd22 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 1")
        R4Clmn1TBB = True
        R4Clmn1T = True
        time.sleep(1)
       elif R4Clmn1T == True:
        if R5Clmn1T == False:
         Sd29 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 1")
         R5Clmn1TBB = True
         R5Clmn1T = True
         time.sleep(1)
        elif R5Clmn1T == True:
         if R6Clmn1T == False:
          Sd36 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 1")
          R6Clmn1TBB = True
          R6Clmn1T = True
          time.sleep(1)
         elif R6Clmn1T == True:
          continue
   if Botgo == 2:
    if R1Clmn2T == False:
     Sd2 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 2")
     R1Clmn2TBB = True
     R1Clmn2T = True
     time.sleep(1)
    elif R1Clmn2T == True:
     if R2Clmn2T == False:
      Sd9 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 2")
      R2Clmn2TBB = True
      R2Clmn2T = True
      time.sleep(1)
     elif R2Clmn2T == True:
      if R3Clmn2T == False:
       Sd16 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 2")
       R3Clmn2TBB = True
       R3Clmn2T = True
       time.sleep(1)
      elif R3Clmn2T == True:
       if R4Clmn2T == False:
        Sd23 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 2")
        R4Clmn2TBB = True
        R4Clmn2T = True
        time.sleep(1)
       elif R4Clmn2T == True:
        if R5Clmn2T == False:
         Sd30 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 2")
         R5Clmn2TBB = True
         R5Clmn2T = True
         time.sleep(1)
        elif R5Clmn2T == True:
         if R6Clmn2T == False:
          Sd37 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 2")
          R6Clmn2TBB = True
          R6Clmn2T = True
          time.sleep(1)
         elif R6Clmn2T == True:
          continue
   if Botgo == 3:
    if R1Clmn3T == False:
     Sd3 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 3")
     R1Clmn3TBB = True
     R1Clmn3T = True
     time.sleep(1)
    elif R1Clmn3T == True:
     if R2Clmn3T == False:
      Sd10 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 3")
      R2Clmn3TBB = True
      R2Clmn3T = True
      time.sleep(1)
     elif R2Clmn3T == True:
      if R3Clmn3T == False:
       Sd17 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 3")
       R3Clmn3TBB = True
       R3Clmn3T = True
       time.sleep(1)
      elif R3Clmn3T == True:
       if R4Clmn3T == False:
        Sd24 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 3")
        R4Clmn3TBB = True
        R4Clmn3T = True
        time.sleep(1)
       elif R4Clmn3T == True:
        if R5Clmn3T == False:
         Sd31 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 3")
         R5Clmn3TBB = True
         R5Clmn3T = True
         time.sleep(1)
        elif R5Clmn3T == True:
         if R6Clmn3T == False:
          Sd38 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 3")
          R6Clmn3TBB = True
          R6Clmn3T = True
          time.sleep(1)
         elif R6Clmn3T == True:
          continue
   if Botgo == 4:
    if R1Clmn4T == False:
     Sd4 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 4")
     R1Clmn4TBB = True
     R1Clmn4T = True
     time.sleep(1)
    elif R1Clmn4T == True:
     if R2Clmn4T == False:
      Sd11 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 4")
      R2Clmn4TBB = True
      R2Clmn4T = True
      time.sleep(1)
     elif R2Clmn4T == True:
      if R3Clmn4T == False:
       Sd18 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 4")
       R3Clmn4TBB = True
       R3Clmn4T = True
       time.sleep(1)
      elif R3Clmn4T == True:
       if R4Clmn4T == False:
        Sd25 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 4")
        R4Clmn4TBB = True
        R4Clmn4T = True
        time.sleep(1)
       elif R4Clmn4T == True:
        if R5Clmn4T == False:
         Sd32 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 4")
         R5Clmn4TBB = True
         R5Clmn4T = True
         time.sleep(1)
        elif R5Clmn4T == True:
         if R6Clmn4T == False:
          Sd39 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 4")
          R6Clmn4TBB = True
          R6Clmn4T = True
          time.sleep(1)
         elif R6Clmn4T == True:
          continue
   if Botgo == 5:
    if R1Clmn5T == False:
     Sd5 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 5")
     R1Clmn5TBB = True
     R1Clmn5T = True
     time.sleep(1)
    elif R1Clmn5T == True:
     if R2Clmn5T == False:
      Sd12 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 5")
      R2Clmn5TBB = True
      R2Clmn5T = True
      time.sleep(1)
     elif R2Clmn5T == True:
      if R3Clmn5T == False:
       Sd19 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 5")
       R3Clmn5TBB = True
       R3Clmn5T = True
       time.sleep(1)
      elif R3Clmn5T == True:
       if R4Clmn5T == False:
        Sd26 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 5")
        R4Clmn5TBB = True
        R4Clmn5T = True
        time.sleep(1)
       elif R4Clmn5T == True:
        if R5Clmn5T == False:
         Sd33 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 5")
         R5Clmn5TBB = True
         R5Clmn5T = True
         time.sleep(1)
        elif R5Clmn5T == True:
         if R6Clmn5T == False:
          Sd40 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 5")
          R6Clmn5TBB = True
          R6Clmn5T = True
          time.sleep(1)
         elif R6Clmn5T == True:
          continue
   if Botgo == 6:
    if R1Clmn6T == False:
     Sd6 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 6")
     R1Clmn6TBB = True
     R1Clmn6T = True
     time.sleep(1)
    elif R1Clmn6T == True:
     if R2Clmn6T == False:
      Sd13 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 6")
      R2Clmn6TBB = True
      R2Clmn6T = True
      time.sleep(1)
     elif R2Clmn6T == True:
      if R3Clmn6T == False:
       Sd20 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 6")
       R3Clmn6TBB = True
       R3Clmn6T = True
       time.sleep(1)
      elif R3Clmn6T == True:
       if R4Clmn6T == False:
        Sd27 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 6")
        R4Clmn6TBB = True
        R4Clmn6T = True
        time.sleep(1)
       elif R4Clmn6T == True:
        if R5Clmn6T == False:
         Sd34 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 6")
         R5Clmn6TBB = True
         R5Clmn6T = True
         time.sleep(1)
        elif R5Clmn6T == True:
         if R6Clmn6T == False:
          Sd41 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 6")
          R6Clmn6TBB = True
          R6Clmn6T = True
          time.sleep(1)
         elif R6Clmn6T == True:
          continue
   if Botgo == 7:
    if R1Clmn7T == False:
     Sd7 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("Your opponent chose to fill in Row 1, Clmn 7")
     R1Clmn7TBB = True
     R1Clmn7T = True
     time.sleep(1)
    elif R1Clmn7T == True:
     if R2Clmn7T == False:
      Sd14 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("Your opponent chose to fill in Row 2, Clmn 7")
      R2Clmn7TBB = True
      R2Clmn7T = True
      time.sleep(1)
     elif R2Clmn7T == True:
      if R3Clmn7T == False:
       Sd21 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("Your opponent chose to fill in Row 3, Clmn 7")
       R3Clmn7TBB = True
       R3Clmn7T = True
       time.sleep(1)
      elif R3Clmn7T == True:
       if R4Clmn7T == False:
        Sd28 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("Your opponent chose to fill in Row 4, Clmn 7")
        R4Clmn7TBB = True
        R4Clmn7T = True
        time.sleep(1)
       elif R4Clmn7T == True:
        if R5Clmn7T == False:
         Sd35 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("Your opponent chose to fill in Row 5, Clmn 7")
         R5Clmn7TBB = True
         R5Clmn7T = True
         time.sleep(1)
        elif R5Clmn7T == True:
         if R6Clmn7T == False:
          Sd42 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("Your opponent chose to fill in Row 6, Clmn 7")
          R6Clmn7TBB = True
          R6Clmn7T = True
          time.sleep(1)
         elif R6Clmn7T == True:
          continue
   clearScreen()
   if (R1Clmn1TBB == True and R2Clmn1TBB == True and R3Clmn1TBB == True and R4Clmn1TBB == True) or (R1Clmn1TBB == True and R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4TBB == True) or (R1Clmn1TBB == True and R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4TBB == True) or (R1Clmn2TBB == True and R2Clmn2TBB == True and R3Clmn2TBB == True and R4Clmn2TBB == True) or (R1Clmn2TBB == True and R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5TBB == True) or (R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5TBB == True) or (R1Clmn3TBB == True and R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3TBB == True) or (R1Clmn3TBB == True and R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6TBB == True) or (R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5TBB == True and R1Clmn6TBB == True) or (R1Clmn4TBB == True and R2Clmn3TBB == True and R3Clmn2TBB == True and R4Clmn1TBB == True) or (R1Clmn4TBB == True and R2Clmn4TBB == True and R3Clmn4TBB == True and R4Clmn4TBB == True) or (R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2TBB == True and R1Clmn1TBB == True) or (R1Clmn5TBB == True and R2Clmn4TBB == True and R3Clmn3TBB == True and R4Clmn2TBB == True) or (R1Clmn5TBB == True and R2Clmn5TBB == True and R3Clmn5TBB == True and R4Clmn5TBB == True) or (R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2TBB == True) or (R1Clmn6TBB == True and R2Clmn5TBB == True and R3Clmn4TBB == True and R4Clmn3TBB == True) or (R1Clmn6TBB == True and R2Clmn6TBB == True and R3Clmn6TBB == True and R4Clmn6TBB == True) or (R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3TBB == True) or (R1Clmn7TBB == True and R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn7TBB == True and R3Clmn7TBB == True and R4Clmn7TBB == True) or (R2Clmn1TBB == True and R3Clmn1TBB == True and R4Clmn1TBB == True and R5Clmn1TBB == True) or (R2Clmn1TBB == True and R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4TBB == True) or (R2Clmn1TBB == True and R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4TBB == True) or (R2Clmn2TBB == True and R3Clmn2TBB == True and R4Clmn2TBB == True and R5Clmn2TBB == True) or (R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5TBB == True) or (R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5TBB == True) or (R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3TBB == True and R5Clmn3TBB == True) or (R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6TBB == True) or (R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6TBB == True) or (R2Clmn4TBB == True and R3Clmn4TBB == True and R4Clmn4TBB == True and R5Clmn4TBB == True) or (R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6TBB == True and R2Clmn7TBB == True) or (R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6TBB == True and R5Clmn7TBB == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R2Clmn5TBB == True and R3Clmn5TBB == True and R4Clmn5TBB == True and R5Clmn5TBB == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3TBB == True) or (R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True) or (R2Clmn6TBB == True and R3Clmn6TBB == True and R4Clmn6TBB == True and R5Clmn6TBB == True) or (R2Clmn7TBB == True and R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4TBB == True) or (R2Clmn7TBB == True and R3Clmn7TBB == True and R4Clmn7TBB == True and R5Clmn7TBB == True) or (R2Clmn7TBB == True and R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4TBB == True) or (R3Clmn1TBB == True and R4Clmn1TBB == True and R5Clmn1TBB == True and R6Clmn1TBB == True) or (R3Clmn1TBB == True and R4Clmn2TBB == True and R5Clmn3TBB == True and R6Clmn4TBB == True) or (R3Clmn1TBB == True and R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4TBB == True) or (R3Clmn2TBB == True and R4Clmn2TBB == True and R5Clmn2TBB == True and R6Clmn2TBB == True) or (R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4TBB == True and R6Clmn5TBB == True) or (R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5TBB == True) or (R3Clmn3TBB == True and R4Clmn3TBB == True and R5Clmn3TBB == True and R6Clmn3TBB == True) or (R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5TBB == True and R6Clmn6TBB == True) or (R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6TBB == True) or (R3Clmn4TBB == True and R4Clmn4TBB == True and R5Clmn4TBB == True and R6Clmn4TBB == True) or (R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6TBB == True and R3Clmn7TBB == True) or (R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6TBB == True and R6Clmn7TBB == True) or (R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3TBB == True and R3Clmn2TBB == True) or (R3Clmn5TBB == True and R4Clmn5TBB == True and R5Clmn5TBB == True and R6Clmn5TBB == True) or (R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3TBB == True and R6Clmn2TBB == True) or (R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4TBB == True and R6Clmn3TBB == True) or (R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3TBB == True) or (R3Clmn6TBB == True and R4Clmn6TBB == True and R5Clmn6TBB == True and R6Clmn6TBB == True) or (R3Clmn7TBB == True and R4Clmn6TBB == True and R5Clmn5TBB == True and R6Clmn4TBB == True) or (R3Clmn7TBB == True and R4Clmn7TBB == True and R5Clmn7TBB == True and R6Clmn7TBB == True) or (R3Clmn7TBB == True and R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4TBB == True) or (R4Clmn1TBB == True and R3Clmn1TBB == True and R2Clmn1TBB == True and R1Clmn1TBB == True) or (R4Clmn1TBB == True and R3Clmn2TBB == True and R2Clmn3TBB == True and R1Clmn4TBB == True) or (R4Clmn1TBB == True and R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4TBB == True) or (R4Clmn2TBB == True and R3Clmn2TBB == True and R2Clmn2TBB == True and R1Clmn2TBB == True) or (R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4TBB == True and R1Clmn5TBB == True) or (R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5TBB == True) or (R4Clmn3TBB == True and R3Clmn3TBB == True and R2Clmn3TBB == True and R1Clmn3TBB == True) or (R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5TBB == True and R1Clmn6TBB == True) or (R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6TBB == True) or (R4Clmn4TBB == True and R3Clmn4TBB == True and R2Clmn4TBB == True and R1Clmn4TBB == True) or (R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6TBB == True and R4Clmn7TBB == True) or (R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6TBB == True and R1Clmn7TBB == True) or (R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3TBB == True and R4Clmn2TBB == True) or (R4Clmn5TBB == True and R3Clmn5TBB == True and R2Clmn5TBB == True and R1Clmn5TBB == True) or (R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3TBB == True and R1Clmn2TBB == True) or (R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4TBB == True and R1Clmn3TBB == True) or (R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3TBB == True) or (R4Clmn6TBB == True and R3Clmn6TBB == True and R2Clmn6TBB == True and R1Clmn6TBB == True) or (R4Clmn7TBB == True and R3Clmn6TBB == True and R2Clmn5TBB == True and R1Clmn4TBB == True) or (R4Clmn7TBB == True and R3Clmn7TBB == True and R2Clmn7TBB == True and R1Clmn7TBB == True) or (R4Clmn7TBB == True and R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4TBB == True) or (R5Clmn1TBB == True and R4Clmn1TBB == True and R3Clmn1TBB == True and R2Clmn1TBB == True) or (R5Clmn1TBB == True and R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4TBB == True) or (R5Clmn1TBB == True and R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4TBB == True) or (R5Clmn2TBB == True and R4Clmn2TBB == True and R3Clmn2TBB == True and R2Clmn2TBB == True) or (R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5TBB == True) or (R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5TBB == True) or (R5Clmn3TBB == True and R4Clmn3TBB == True and R3Clmn3TBB == True and R2Clmn3TBB == True) or (R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6TBB == True) or (R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6TBB == True) or (R5Clmn4TBB == True and R4Clmn4TBB == True and R3Clmn4TBB == True and R2Clmn4TBB == True) or (R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6TBB == True and R5Clmn7TBB == True) or (R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6TBB == True and R2Clmn7TBB == True) or (R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3TBB == True and R5Clmn2TBB == True) or (R5Clmn5TBB == True and R4Clmn5TBB == True and R3Clmn5TBB == True and R2Clmn5TBB == True) or (R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3TBB == True and R2Clmn2TBB == True) or (R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3TBB == True) or (R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3TBB == True) or (R5Clmn6TBB == True and R4Clmn6TBB == True and R3Clmn6TBB == True and R2Clmn6TBB == True) or (R5Clmn7TBB == True and R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4TBB == True) or (R5Clmn7TBB == True and R4Clmn7TBB == True and R3Clmn7TBB == True and R2Clmn7TBB == True) or (R5Clmn7TBB == True and R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4TBB == True) or (R6Clmn1TBB == True and R5Clmn1TBB == True and R4Clmn1TBB == True and R3Clmn1TBB == True) or (R6Clmn1TBB == True and R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4TBB == True) or (R6Clmn1TBB == True and R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4TBB == True) or (R6Clmn2TBB == True and R5Clmn2TBB == True and R4Clmn2TBB == True and R3Clmn2TBB == True) or (R6Clmn2TBB == True and R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5TBB == True) or (R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5TBB == True) or (R6Clmn3TBB == True and R5Clmn3TBB == True and R4Clmn3TBB == True and R3Clmn3TBB == True) or (R6Clmn3TBB == True and R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6TBB == True) or (R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6TBB == True) or (R6Clmn4TBB == True and R5Clmn4TBB == True and R4Clmn4TBB == True and R3Clmn4TBB == True) or (R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6TBB == True and R6Clmn7TBB == True) or (R6Clmn4TBB == True and R5Clmn5TBB == True and R4Clmn6TBB == True and R3Clmn7TBB == True) or (R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3TBB == True and R6Clmn2TBB == True) or (R6Clmn5TBB == True and R5Clmn5TBB == True and R4Clmn5TBB == True and R3Clmn5TBB == True) or (R6Clmn5TBB == True and R5Clmn4TBB == True and R4Clmn3TBB == True and R3Clmn2TBB == True) or (R6Clmn6TBB == True and R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3TBB == True) or (R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3TBB == True) or (R6Clmn6TBB == True and R5Clmn6TBB == True and R4Clmn6TBB == True and R3Clmn6TBB == True) or (R6Clmn7TBB == True and R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4TBB == True) or (R6Clmn7TBB == True and R5Clmn7TBB == True and R4Clmn7TBB == True and R3Clmn7TBB == True) or (R6Clmn7TBB == True and R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4TBB == True):
    print(NewConnect4Board)
    print("")
    print(Red+"Your opponent has connected four!"+reset)
    print("")
    Botpoints = Botpoints + 1
    PETC_function()
    Yourshape = 1
    Botshape = 2
    YourSd = Red+"O"+reset
    BotSd = Blue+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   elif R1Clmn1T == True and R1Clmn2T == True and R1Clmn3T == True and R1Clmn4T == True and R1Clmn5T == True and R1Clmn6T == True and R1Clmn7T == True and R2Clmn1T == True and R2Clmn2T == True and  R2Clmn3T == True and R2Clmn4T == True and R2Clmn5T == True and R2Clmn6T == True and R2Clmn7T == True and R3Clmn1T == True and R3Clmn2T == True and R3Clmn3T == True and R3Clmn4T == True and R3Clmn5T == True and R3Clmn6T == True and R3Clmn7T == True and R4Clmn1T == True and R4Clmn2T == True and R4Clmn3T == True and R4Clmn4T == True and R4Clmn5T == True and R4Clmn6T == True and R4Clmn7T == True and R5Clmn1T == True and R5Clmn2T == True and R5Clmn3T == True and R5Clmn4T == True and R5Clmn5T == True and R5Clmn6T == True and R5Clmn7T == True and R6Clmn1T == True and R6Clmn2T == True and R6Clmn3T == True and R6Clmn4T == True and R6Clmn5T == True and R6Clmn6T == True and R6Clmn7T == True:
    print(NewConnect4Board)
    print("")
    print("DRAW!")
    print("")
    PETC_function()
    Yourshape = 1
    Botshape = 2
    YourSd = Red+"O"+reset
    BotSd = Blue+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   Botturn = False
   clearScreen()
 if Yourpoints == 1 and DifficultyChoice == 1:
  return "EW"
 if Yourpoints == 1 and DifficultyChoice == 2:
  return "MW"
 elif Yourpoints == 1 and DifficultyChoice == 3:
  return "HW"
 elif Botpoints == 1 and DifficultyChoice == 1:
  return "EL"
 elif Botpoints == 1 and DifficultyChoice == 2:
  return "ML"
 elif Botpoints == 1 and DifficultyChoice == 3:
  return "HL"
   
def pvplevel10_function(OnePlayerName,TwoPlayerName):
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
 Sd10 = "_"
 Sd11 = "_"
 Sd12 = "_"
 Sd13 = "_"
 Sd14 = "_"
 Sd15 = "_"
 Sd16 = "_"
 Sd17 = "_"
 Sd18 = "_"
 Sd19 = "_"
 Sd20 = "_"
 Sd21 = "_"
 Sd22 = "_"
 Sd23 = "_"
 Sd24 = "_"
 Sd25 = "_"
 Sd26 = "_"
 Sd27 = "_"
 Sd28 = "_"
 Sd29 = "_"
 Sd30 = "_"
 Sd31 = "_"
 Sd32 = "_"
 Sd33 = "_"
 Sd34 = "_"
 Sd35 = "_"
 Sd36 = "_"
 Sd37 = "_"
 Sd38 = "_"
 Sd39 = "_"
 Sd40 = "_"
 Sd41 = "_"
 Sd42 = "_"
 R1Clmn1T = False 
 R1Clmn2T = False 
 R1Clmn3T = False 
 R1Clmn4T = False 
 R1Clmn5T = False 
 R1Clmn6T = False 
 R1Clmn7T = False 
 R2Clmn1T = False 
 R2Clmn2T = False 
 R2Clmn3T = False 
 R2Clmn4T = False 
 R2Clmn5T = False 
 R2Clmn6T = False 
 R2Clmn7T = False 
 R3Clmn1T = False 
 R3Clmn2T = False 
 R3Clmn3T = False 
 R3Clmn4T = False 
 R3Clmn5T = False 
 R3Clmn6T = False 
 R3Clmn7T = False 
 R4Clmn1T = False 
 R4Clmn2T = False 
 R4Clmn3T = False 
 R4Clmn4T = False 
 R4Clmn5T = False 
 R4Clmn6T = False 
 R4Clmn7T = False 
 R5Clmn1T = False 
 R5Clmn2T = False 
 R5Clmn3T = False 
 R5Clmn4T = False 
 R5Clmn5T = False 
 R5Clmn6T = False 
 R5Clmn7T = False 
 R6Clmn1T = False 
 R6Clmn2T = False 
 R6Clmn3T = False 
 R6Clmn4T = False 
 R6Clmn5T = False 
 R6Clmn6T = False 
 R6Clmn7T = False 
 R1Clmn1TBY = False 
 R1Clmn2TBY = False 
 R1Clmn3TBY = False 
 R1Clmn4TBY = False 
 R1Clmn5TBY = False 
 R1Clmn6TBY = False 
 R1Clmn7TBY = False 
 R2Clmn1TBY = False 
 R2Clmn2TBY = False 
 R2Clmn3TBY = False 
 R2Clmn4TBY = False 
 R2Clmn5TBY = False 
 R2Clmn6TBY = False 
 R2Clmn7TBY = False 
 R3Clmn1TBY = False 
 R3Clmn2TBY = False 
 R3Clmn3TBY = False 
 R3Clmn4TBY = False 
 R3Clmn5TBY = False 
 R3Clmn6TBY = False 
 R3Clmn7TBY = False 
 R4Clmn1TBY = False 
 R4Clmn2TBY = False 
 R4Clmn3TBY = False 
 R4Clmn4TBY = False 
 R4Clmn5TBY = False 
 R4Clmn6TBY = False 
 R4Clmn7TBY = False 
 R5Clmn1TBY = False 
 R5Clmn2TBY = False 
 R5Clmn3TBY = False 
 R5Clmn4TBY = False 
 R5Clmn5TBY = False 
 R5Clmn6TBY = False 
 R5Clmn7TBY = False 
 R6Clmn1TBY = False 
 R6Clmn2TBY = False 
 R6Clmn3TBY = False 
 R6Clmn4TBY = False 
 R6Clmn5TBY = False 
 R6Clmn6TBY = False
 R6Clmn7TBY = False 
 R1Clmn1TBB = False 
 R1Clmn2TBB = False 
 R1Clmn3TBB = False 
 R1Clmn4TBB = False 
 R1Clmn5TBB = False 
 R1Clmn6TBB = False 
 R1Clmn7TBB = False 
 R2Clmn1TBB = False 
 R2Clmn2TBB = False 
 R2Clmn3TBB = False 
 R2Clmn4TBB = False 
 R2Clmn5TBB = False 
 R2Clmn6TBB = False 
 R2Clmn7TBB = False 
 R3Clmn1TBB = False 
 R3Clmn2TBB = False 
 R3Clmn3TBB = False 
 R3Clmn4TBB = False 
 R3Clmn5TBB = False 
 R3Clmn6TBB = False 
 R3Clmn7TBB = False 
 R4Clmn1TBB = False 
 R4Clmn2TBB = False 
 R4Clmn3TBB = False 
 R4Clmn4TBB = False 
 R4Clmn5TBB = False 
 R4Clmn6TBB = False 
 R4Clmn7TBB = False 
 R5Clmn1TBB = False 
 R5Clmn2TBB = False 
 R5Clmn3TBB = False 
 R5Clmn4TBB = False 
 R5Clmn5TBB = False 
 R5Clmn6TBB = False 
 R5Clmn7TBB = False 
 R6Clmn1TBB = False 
 R6Clmn2TBB = False 
 R6Clmn3TBB = False 
 R6Clmn4TBB = False 
 R6Clmn5TBB = False 
 R6Clmn6TBB = False 
 R6Clmn7TBB = False 
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
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   II_function()
 Connect4Board = '''6 | {35} | {36} | {37} | {38} | {39} | {40} | {41}
 -----------------------------
5 | {28} | {29} | {30} | {31} | {32} | {33} | {34}
 -----------------------------
4 | {21} | {22} | {23} | {24} | {25} | {26} | {27}
 -----------------------------
3 | {14} | {15} | {16} | {17} | {18} | {19} | {20}
 -----------------------------
2 | {7} | {8} | {9} | {10} | {11} | {12} | {13}
 -----------------------------
1 | {0} | {1} | {2} | {3} | {4} | {5} | {6}
    1 | 2 | 3 | 4 | 5 | 6 | 7'''
 while Yourpoints < 1 and Botpoints < 1: 
  if Yourshape == 1:
   YourSd = Red+"O"+reset
  elif Yourshape == 2:
   YourSd = Blue+"O"+reset
  if Botshape == 1:
   BotSd = Red+"O"+reset
  elif Botshape == 2:
   BotSd = Blue+"O"+reset
  Yourturn = True
   
  while Yourturn == True:
   print(Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42))
   print("It's {}'s turn! Choose your Column".format(OnePlayerName))
   time.sleep(0.25)
   print("1 - 1st Column",end = '   ')
   print("2 - 2nd Column",end = '   ')
   print("3 - 3rd Column",end = '   ')
   print("4 - 4th Column")
   time.sleep(0.25)
   print("")
   print("5 - 5th Column",end = '   ')
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
   if Yourgo == 1:
    if R1Clmn1T == False:
     Sd1 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 1".format(OnePlayerName))
     R1Clmn1TBY = True
     R1Clmn1T = True
     time.sleep(1)
    elif R1Clmn1T == True:
     if R2Clmn1T == False:
      Sd8 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 1".format(OnePlayerName))
      R2Clmn1TBY = True
      R2Clmn1T = True
      time.sleep(1)
     elif R2Clmn1T == True:
      if R3Clmn1T == False:
       Sd15 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 1".format(OnePlayerName))
       R3Clmn1TBY = True
       R3Clmn1T = True
       time.sleep(1)
      elif R3Clmn1T == True:
       if R4Clmn1T == False:
        Sd22 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 1".format(OnePlayerName))
        R4Clmn1TBY = True
        R4Clmn1T = True
        time.sleep(1)
       elif R4Clmn1T == True:
        if R5Clmn1T == False:
         Sd29 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 1".format(OnePlayerName))
         R5Clmn1TBY = True
         R5Clmn1T = True
         time.sleep(1)
        elif R5Clmn1T == True:
         if R6Clmn1T == False:
          Sd36 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 1".format(OnePlayerName))
          R6Clmn1TBY = True
          R6Clmn1T = True
          time.sleep(1)
         elif R6Clmn1T == True:
          print(Red+"Column is filled".format(OnePlayerName)+reset)
          PETC_function()
          continue
   elif Yourgo == 2:
    if R1Clmn2T == False:
     Sd2 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 2".format(OnePlayerName))
     R1Clmn2TBY = True
     R1Clmn2T = True
     time.sleep(1)
    elif R1Clmn2T == True:
     if R2Clmn2T == False:
      Sd9 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 2".format(OnePlayerName))
      R2Clmn2TBY = True
      R2Clmn2T = True
      time.sleep(1)
     elif R2Clmn2T == True:
      if R3Clmn2T == False:
       Sd16 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 2".format(OnePlayerName))
       R3Clmn2TBY = True
       R3Clmn2T = True
       time.sleep(1)
      elif R3Clmn2T == True:
       if R4Clmn2T == False:
        Sd23 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 2".format(OnePlayerName))
        R4Clmn2TBY = True
        R4Clmn2T = True
        time.sleep(1)
       elif R4Clmn2T == True:
        if R5Clmn2T == False:
         Sd30 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 2".format(OnePlayerName))
         R5Clmn2TBY = True
         R5Clmn2T = True
         time.sleep(1)
        elif R5Clmn2T == True:
         if R6Clmn2T == False:
          Sd37 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 2".format(OnePlayerName))
          R6Clmn2TBY = True
          R6Clmn2T = True
          time.sleep(1)
         elif R6Clmn2T == True:
          print(Red+"Column is filled".format(OnePlayerName)+reset)
          PETC_function()
          continue
   elif Yourgo == 3:
    if R1Clmn3T == False:
     Sd3 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 3".format(OnePlayerName))
     R1Clmn3TBY = True
     R1Clmn3T = True
     time.sleep(1)
    elif R1Clmn3T == True:
     if R2Clmn3T == False:
      Sd10 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 3".format(OnePlayerName))
      R2Clmn3TBY = True
      R2Clmn3T = True
      time.sleep(1)
     elif R2Clmn3T == True:
      if R3Clmn3T == False:
       Sd17 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 3".format(OnePlayerName))
       R3Clmn3TBY = True
       R3Clmn3T = True
       time.sleep(1)
      elif R3Clmn3T == True:
       if R4Clmn3T == False:
        Sd24 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 3".format(OnePlayerName))
        R4Clmn3TBY = True
        R4Clmn3T = True
        time.sleep(1)
       elif R4Clmn3T == True:
        if R5Clmn3T == False:
         Sd31 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 3".format(OnePlayerName))
         R5Clmn3TBY = True
         R5Clmn3T = True
         time.sleep(1)
        elif R5Clmn3T == True:
         if R6Clmn3T == False:
          Sd38 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 3".format(OnePlayerName))
          R6Clmn3TBY = True
          R6Clmn3T = True
          time.sleep(1)
         elif R6Clmn3T == True:
          print(Red+"Column is filled".format(OnePlayerName)+reset)
          PETC_function()
          continue
   elif Yourgo == 4:
    if R1Clmn4T == False:
     Sd4 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 4".format(OnePlayerName))
     R1Clmn4TBY = True
     R1Clmn4T = True
     time.sleep(1)
    elif R1Clmn4T == True:
     if R2Clmn4T == False:
      Sd11 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 4".format(OnePlayerName))
      R2Clmn4TBY = True
      R2Clmn4T = True
      time.sleep(1)
     elif R2Clmn4T == True:
      if R3Clmn4T == False:
       Sd18 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 4".format(OnePlayerName))
       R3Clmn4TBY = True
       R3Clmn4T = True
       time.sleep(1)
      elif R3Clmn4T == True:
       if R4Clmn4T == False:
        Sd25 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 4".format(OnePlayerName))
        R4Clmn4TBY = True
        R4Clmn4T = True
        time.sleep(1)
       elif R4Clmn4T == True:
        if R5Clmn4T == False:
         Sd32 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 4".format(OnePlayerName))
         R5Clmn4TBY = True
         R5Clmn4T = True
         time.sleep(1)
        elif R5Clmn4T == True:
         if R6Clmn4T == False:
          Sd39 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 4".format(OnePlayerName))
          R6Clmn4TBY = True
          R6Clmn4T = True
          time.sleep(1)
         elif R6Clmn4T == True:
          print(Red+"Column is filled".format(OnePlayerName)+reset)
          PETC_function()
          continue
   elif Yourgo == 5:
    if R1Clmn5T == False:
     Sd5 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 5".format(OnePlayerName))
     R1Clmn5TBY = True
     R1Clmn5T = True
     time.sleep(1)
    elif R1Clmn5T == True:
     if R2Clmn5T == False:
      Sd12 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 5".format(OnePlayerName))
      R2Clmn5TBY = True
      R2Clmn5T = True
      time.sleep(1)
     elif R2Clmn5T == True:
      if R3Clmn5T == False:
       Sd19 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 5".format(OnePlayerName))
       R3Clmn5TBY = True
       R3Clmn5T = True
       time.sleep(1)
      elif R3Clmn5T == True:
       if R4Clmn5T == False:
        Sd26 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 5".format(OnePlayerName))
        R4Clmn5TBY = True
        R4Clmn5T = True
        time.sleep(1)
       elif R4Clmn5T == True:
        if R5Clmn5T == False:
         Sd33 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 5".format(OnePlayerName))
         R5Clmn5TBY = True
         R5Clmn5T = True
         time.sleep(1)
        elif R5Clmn5T == True:
         if R6Clmn5T == False:
          Sd40 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 5".format(OnePlayerName))
          R6Clmn5TBY = True
          R6Clmn5T = True
          time.sleep(1)
         elif R6Clmn5T == True:
          print(Red+"Column is filled".format(OnePlayerName)+reset)
          PETC_function()
          continue
   elif Yourgo == 6:
    if R1Clmn6T == False:
     Sd6 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 6".format(OnePlayerName))
     R1Clmn6TBY = True
     R1Clmn6T = True
     time.sleep(1)
    elif R1Clmn6T == True:
     if R2Clmn6T == False:
      Sd13 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 6".format(OnePlayerName))
      R2Clmn6TBY = True
      R2Clmn6T = True
      time.sleep(1)
     elif R2Clmn6T == True:
      if R3Clmn6T == False:
       Sd20 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 6".format(OnePlayerName))
       R3Clmn6TBY = True
       R3Clmn6T = True
       time.sleep(1)
      elif R3Clmn6T == True:
       if R4Clmn6T == False:
        Sd27 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 6".format(OnePlayerName))
        R4Clmn6TBY = True
        R4Clmn6T = True
        time.sleep(1)
       elif R4Clmn6T == True:
        if R5Clmn6T == False:
         Sd34 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 6".format(OnePlayerName))
         R5Clmn6TBY = True
         R5Clmn6T = True
         time.sleep(1)
        elif R5Clmn6T == True:
         if R6Clmn6T == False:
          Sd41 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 6".format(OnePlayerName))
          R6Clmn6TBY = True
          R6Clmn6T = True
          time.sleep(1)
         elif R6Clmn6T == True:
          print(Red+"Column is filled".format(OnePlayerName)+reset)
          PETC_function()
          continue
   elif Yourgo == 7:
    if R1Clmn7T == False:
     Sd7 = YourSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Column 7".format(OnePlayerName))
     R1Clmn7TBY = True
     R1Clmn7T = True
     time.sleep(1)
    elif R1Clmn7T == True:
     if R2Clmn7T == False:
      Sd14 = YourSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Column 7".format(OnePlayerName))
      R2Clmn7TBY = True
      R2Clmn7T = True
      time.sleep(1)
     elif R2Clmn7T == True:
      if R3Clmn7T == False:
       Sd21 = YourSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Column 7".format(OnePlayerName))
       R3Clmn7TBY = True
       R3Clmn7T = True
       time.sleep(1)
      elif R3Clmn7T == True:
       if R4Clmn7T == False:
        Sd28 = YourSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Column 7".format(OnePlayerName))
        R4Clmn7TBY = True
        R4Clmn7T = True
        time.sleep(1)
       elif R4Clmn7T == True:
        if R5Clmn7T == False:
         Sd35 = YourSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Column 7".format(OnePlayerName))
         R5Clmn7TBY = True
         R5Clmn7T = True
         time.sleep(1)
        elif R5Clmn7T == True:
         if R6Clmn7T == False:
          Sd42 = YourSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Column 7".format(OnePlayerName))
          R6Clmn7TBY = True
          R6Clmn7T = True
          time.sleep(1)
         elif R6Clmn7T == True:
          print(Red+"Column is filled"+reset)
          PETC_function()
          continue
   else:
    II_function()
    continue
   clearScreen()
   if (R1Clmn1TBY == True and R2Clmn1TBY == True and R3Clmn1TBY == True and R4Clmn1TBY == True) or (R1Clmn1TBY == True and R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True) or (R1Clmn1TBY == True and R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4TBY == True) or (R1Clmn2TBY == True and R2Clmn2TBY == True and R3Clmn2TBY == True and R4Clmn2TBY == True) or (R1Clmn2TBY == True and R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True) or (R1Clmn2TBY == True and R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5TBY == True) or (R1Clmn3TBY == True and R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3TBY == True) or (R1Clmn3TBY == True and R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True) or (R1Clmn3TBY == True and R1Clmn4TBY == True and R1Clmn5TBY == True and R1Clmn6TBY == True) or (R1Clmn4TBY == True and R2Clmn3TBY == True and R3Clmn2TBY == True and R4Clmn1TBY == True) or (R1Clmn4TBY == True and R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4TBY == True) or (R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2TBY == True and R1Clmn1TBY == True) or (R1Clmn5TBY == True and R2Clmn4TBY == True and R3Clmn3TBY == True and R4Clmn2TBY == True) or (R1Clmn5TBY == True and R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5TBY == True) or (R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3TBY == True and R1Clmn2TBY == True) or (R1Clmn6TBY == True and R2Clmn5TBY == True and R3Clmn4TBY == True and R4Clmn3TBY == True) or (R1Clmn6TBY == True and R2Clmn6TBY == True and R3Clmn6TBY == True and R4Clmn6TBY == True) or (R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4TBY == True and R1Clmn3TBY == True) or (R1Clmn7TBY == True and R1Clmn6TBY == True and R1Clmn5TBY == True and R1Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True) or (R1Clmn7TBY == True and R2Clmn7TBY == True and R3Clmn7TBY == True and R4Clmn7TBY == True) or (R2Clmn1TBY == True and R3Clmn1TBY == True and R4Clmn1TBY == True and R5Clmn1TBY == True) or (R2Clmn1TBY == True and R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True) or (R2Clmn1TBY == True and R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True) or (R2Clmn2TBY == True and R3Clmn2TBY == True and R4Clmn2TBY == True and R5Clmn2TBY == True) or (R2Clmn2TBY == True and R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True) or (R2Clmn2TBY == True and R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True) or (R2Clmn3TBY == True and R3Clmn3TBY == True and R4Clmn3TBY == True and R5Clmn3TBY == True) or (R2Clmn3TBY == True and R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True) or (R2Clmn3TBY == True and R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True) or (R2Clmn4TBY == True and R3Clmn4TBY == True and R4Clmn4TBY == True and R5Clmn4TBY == True) or (R2Clmn4TBY == True and R2Clmn5TBY == True and R2Clmn6TBY == True and R2Clmn7TBY == True) or (R2Clmn4TBY == True and R3Clmn5TBY == True and R4Clmn6TBY == True and R5Clmn7TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn5TBY == True and R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5TBY == True) or (R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True and R2Clmn2TBY == True) or (R2Clmn6TBY == True and R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True) or (R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True and R2Clmn3TBY == True) or (R2Clmn6TBY == True and R3Clmn6TBY == True and R4Clmn6TBY == True and R5Clmn6TBY == True) or (R2Clmn7TBY == True and R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True) or (R2Clmn7TBY == True and R3Clmn7TBY == True and R4Clmn7TBY == True and R5Clmn7TBY == True) or (R2Clmn7TBY == True and R2Clmn6TBY == True and R2Clmn5TBY == True and R2Clmn4TBY == True) or (R3Clmn1TBY == True and R4Clmn1TBY == True and R5Clmn1TBY == True and R6Clmn1TBY == True) or (R3Clmn1TBY == True and R4Clmn2TBY == True and R5Clmn3TBY == True and R6Clmn4TBY == True) or (R3Clmn1TBY == True and R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True) or (R3Clmn2TBY == True and R4Clmn2TBY == True and R5Clmn2TBY == True and R6Clmn2TBY == True) or (R3Clmn2TBY == True and R4Clmn3TBY == True and R5Clmn4TBY == True and R6Clmn5TBY == True) or (R3Clmn2TBY == True and R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True) or (R3Clmn3TBY == True and R4Clmn3TBY == True and R5Clmn3TBY == True and R6Clmn3TBY == True) or (R3Clmn3TBY == True and R4Clmn4TBY == True and R5Clmn5TBY == True and R6Clmn6TBY == True) or (R3Clmn3TBY == True and R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True) or (R3Clmn4TBY == True and R4Clmn4TBY == True and R5Clmn4TBY == True and R6Clmn4TBY == True) or (R3Clmn4TBY == True and R3Clmn5TBY == True and R3Clmn6TBY == True and R3Clmn7TBY == True) or (R3Clmn4TBY == True and R4Clmn5TBY == True and R5Clmn6TBY == True and R6Clmn7TBY == True) or (R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True and R3Clmn2TBY == True) or (R3Clmn5TBY == True and R4Clmn5TBY == True and R5Clmn5TBY == True and R6Clmn5TBY == True) or (R3Clmn5TBY == True and R4Clmn4TBY == True and R5Clmn3TBY == True and R6Clmn2TBY == True) or (R3Clmn6TBY == True and R4Clmn5TBY == True and R5Clmn4TBY == True and R6Clmn3TBY == True) or (R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True and R3Clmn3TBY == True) or (R3Clmn6TBY == True and R4Clmn6TBY == True and R5Clmn6TBY == True and R6Clmn6TBY == True) or (R3Clmn7TBY == True and R4Clmn6TBY == True and R5Clmn5TBY == True and R6Clmn4TBY == True) or (R3Clmn7TBY == True and R4Clmn7TBY == True and R5Clmn7TBY == True and R6Clmn7TBY == True) or (R3Clmn7TBY == True and R3Clmn6TBY == True and R3Clmn5TBY == True and R3Clmn4TBY == True) or (R4Clmn1TBY == True and R3Clmn1TBY == True and R2Clmn1TBY == True and R1Clmn1TBY == True) or (R4Clmn1TBY == True and R3Clmn2TBY == True and R2Clmn3TBY == True and R1Clmn4TBY == True) or (R4Clmn1TBY == True and R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True) or (R4Clmn2TBY == True and R3Clmn2TBY == True and R2Clmn2TBY == True and R1Clmn2TBY == True) or (R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True and R1Clmn5TBY == True) or (R4Clmn2TBY == True and R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True) or (R4Clmn3TBY == True and R3Clmn3TBY == True and R2Clmn3TBY == True and R1Clmn3TBY == True) or (R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True and R1Clmn6TBY == True) or (R4Clmn3TBY == True and R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True) or (R4Clmn4TBY == True and R3Clmn4TBY == True and R2Clmn4TBY == True and R1Clmn4TBY == True) or (R4Clmn4TBY == True and R4Clmn5TBY == True and R4Clmn6TBY == True and R4Clmn7TBY == True) or (R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True and R1Clmn7TBY == True) or (R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True and R4Clmn2TBY == True) or (R4Clmn5TBY == True and R3Clmn5TBY == True and R2Clmn5TBY == True and R1Clmn5TBY == True) or (R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True and R1Clmn2TBY == True) or (R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True and R1Clmn3TBY == True) or (R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True and R4Clmn3TBY == True) or (R4Clmn6TBY == True and R3Clmn6TBY == True and R2Clmn6TBY == True and R1Clmn6TBY == True) or (R4Clmn7TBY == True and R3Clmn6TBY == True and R2Clmn5TBY == True and R1Clmn4TBY == True) or (R4Clmn7TBY == True and R3Clmn7TBY == True and R2Clmn7TBY == True and R1Clmn7TBY == True) or (R4Clmn7TBY == True and R4Clmn6TBY == True and R4Clmn5TBY == True and R4Clmn4TBY == True) or (R5Clmn1TBY == True and R4Clmn1TBY == True and R3Clmn1TBY == True and R2Clmn1TBY == True) or (R5Clmn1TBY == True and R4Clmn2TBY == True and R3Clmn3TBY == True and R2Clmn4TBY == True) or (R5Clmn1TBY == True and R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True) or (R5Clmn2TBY == True and R4Clmn2TBY == True and R3Clmn2TBY == True and R2Clmn2TBY == True) or (R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True and R2Clmn5TBY == True) or (R5Clmn2TBY == True and R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True) or (R5Clmn3TBY == True and R4Clmn3TBY == True and R3Clmn3TBY == True and R2Clmn3TBY == True) or (R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True and R2Clmn6TBY == True) or (R5Clmn3TBY == True and R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True) or (R5Clmn4TBY == True and R4Clmn4TBY == True and R3Clmn4TBY == True and R2Clmn4TBY == True) or (R5Clmn4TBY == True and R5Clmn5TBY == True and R5Clmn6TBY == True and R5Clmn7TBY == True) or (R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True and R2Clmn7TBY == True) or (R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True and R5Clmn2TBY == True) or (R5Clmn5TBY == True and R4Clmn5TBY == True and R3Clmn5TBY == True and R2Clmn5TBY == True) or (R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True and R2Clmn2TBY == True) or (R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True and R2Clmn3TBY == True) or (R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True and R5Clmn3TBY == True) or (R5Clmn6TBY == True and R4Clmn6TBY == True and R3Clmn6TBY == True and R2Clmn6TBY == True) or (R5Clmn7TBY == True and R4Clmn6TBY == True and R3Clmn5TBY == True and R2Clmn4TBY == True) or (R5Clmn7TBY == True and R4Clmn7TBY == True and R3Clmn7TBY == True and R2Clmn7TBY == True) or (R5Clmn7TBY == True and R5Clmn6TBY == True and R5Clmn5TBY == True and R5Clmn4TBY == True) or (R6Clmn1TBY == True and R5Clmn1TBY == True and R4Clmn1TBY == True and R3Clmn1TBY == True) or (R6Clmn1TBY == True and R5Clmn2TBY == True and R4Clmn3TBY == True and R3Clmn4TBY == True) or (R6Clmn1TBY == True and R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True) or (R6Clmn2TBY == True and R5Clmn2TBY == True and R4Clmn2TBY == True and R3Clmn2TBY == True) or (R6Clmn2TBY == True and R5Clmn3TBY == True and R4Clmn4TBY == True and R3Clmn5TBY == True) or (R6Clmn2TBY == True and R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True) or (R6Clmn3TBY == True and R5Clmn3TBY == True and R4Clmn3TBY == True and R3Clmn3TBY == True) or (R6Clmn3TBY == True and R5Clmn4TBY == True and R4Clmn5TBY == True and R3Clmn6TBY == True) or (R6Clmn3TBY == True and R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True) or (R6Clmn4TBY == True and R5Clmn4TBY == True and R4Clmn4TBY == True and R3Clmn4TBY == True) or (R6Clmn4TBY == True and R6Clmn5TBY == True and R6Clmn6TBY == True and R6Clmn7TBY == True) or (R6Clmn4TBY == True and R5Clmn5TBY == True and R4Clmn6TBY == True and R3Clmn7TBY == True) or (R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True and R6Clmn2TBY == True) or (R6Clmn5TBY == True and R5Clmn5TBY == True and R4Clmn5TBY == True and R3Clmn5TBY == True) or (R6Clmn5TBY == True and R5Clmn4TBY == True and R4Clmn3TBY == True and R3Clmn2TBY == True) or (R6Clmn6TBY == True and R5Clmn5TBY == True and R4Clmn4TBY == True and R3Clmn3TBY == True) or (R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True and R6Clmn3TBY == True) or (R6Clmn6TBY == True and R5Clmn6TBY == True and R4Clmn6TBY == True and R3Clmn6TBY == True) or (R6Clmn7TBY == True and R5Clmn6TBY == True and R4Clmn5TBY == True and R3Clmn4TBY == True) or (R6Clmn7TBY == True and R5Clmn7TBY == True and R4Clmn7TBY == True and R3Clmn7TBY == True) or (R6Clmn7TBY == True and R6Clmn6TBY == True and R6Clmn5TBY == True and R6Clmn4TBY == True):  
    print(NewConnect4Board)
    print("")
    print("{} ".format(OnePlayerName)+Blue+"has connected four!"+reset)
    print("")
    Yourpoints = Yourpoints + 1
    PETC_function()
    Yourshape = 2
    Botshape = 1
    YourSd = Blue+"O"+reset
    BotSd = Red+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   elif R1Clmn1T == True and R1Clmn2T == True and R1Clmn3T == True and R1Clmn4T == True and R1Clmn5T == True and R1Clmn6T == True and R1Clmn7T == True and R2Clmn1T == True and R2Clmn2T == True and  R2Clmn3T == True and R2Clmn4T == True and R2Clmn5T == True and R2Clmn6T == True and R2Clmn7T == True and R3Clmn1T == True and R3Clmn2T == True and R3Clmn3T == True and R3Clmn4T == True and R3Clmn5T == True and R3Clmn6T == True and R3Clmn7T == True and R4Clmn1T == True and R4Clmn2T == True and R4Clmn3T == True and R4Clmn4T == True and R4Clmn5T == True and R4Clmn6T == True and R4Clmn7T == True and R5Clmn1T == True and R5Clmn2T == True and R5Clmn3T == True and R5Clmn4T == True and R5Clmn5T == True and R5Clmn6T == True and R5Clmn7T == True and R6Clmn1T == True and R6Clmn2T == True and R6Clmn3T == True and R6Clmn4T == True and R6Clmn5T == True and R6Clmn6T == True and R6Clmn7T == True:
    print(NewConnect4Board)
    print("")
    print("DRAW!")
    print("")
    PETC_function()
    Yourshape = 2
    Botshape = 1
    YourSd = Blue+"O"+reset
    BotSd = Red+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   Yourturn = False
  NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
  Botturn = True
  while Botturn == True and Yourpoints != 1:
   print(Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42))
   print("It's {}'s turn!".format(TwoPlayerName))
   time.sleep(0.25)
   print("1 - 1st Column",end = '   ')
   print("2 - 2nd Column",end = '   ')
   print("3 - 3rd Column",end = '   ')
   print("4 - 4th Column")
   time.sleep(0.25)
   print("")
   print("5 - 5th Column",end = '   ')
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
   Quitchoice = 0
   while Botgo == 0:
    print("Are you sure you want to "+Red+"quit"+reset+"?")
    YOR_function()
    try:
     Quitchoice = int(input(""))
    except:
     II_function()
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
   if Botgo == 1:
    if R1Clmn1T == False:
     Sd1 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 1".format(TwoPlayerName))
     R1Clmn1TBB = True
     R1Clmn1T = True
     time.sleep(1)
    elif R1Clmn1T == True:
     if R2Clmn1T == False:
      Sd8 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 1".format(TwoPlayerName))
      R2Clmn1TBB = True
      R2Clmn1T = True
      time.sleep(1)
     elif R2Clmn1T == True:
      if R3Clmn1T == False:
       Sd15 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 1".format(TwoPlayerName))
       R3Clmn1TBB = True
       R3Clmn1T = True
       time.sleep(1)
      elif R3Clmn1T == True:
       if R4Clmn1T == False:
        Sd22 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 1".format(TwoPlayerName))
        R4Clmn1TBB = True
        R4Clmn1T = True
        time.sleep(1)
       elif R4Clmn1T == True:
        if R5Clmn1T == False:
         Sd29 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 1".format(TwoPlayerName))
         R5Clmn1TBB = True
         R5Clmn1T = True
         time.sleep(1)
        elif R5Clmn1T == True:
         if R6Clmn1T == False:
          Sd36 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 1".format(TwoPlayerName))
          R6Clmn1TBB = True
          R6Clmn1T = True
          time.sleep(1)
         elif R6Clmn1T == True:
          continue
   if Botgo == 2:
    if R1Clmn2T == False:
     Sd2 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 2".format(TwoPlayerName))
     R1Clmn2TBB = True
     R1Clmn2T = True
     time.sleep(1)
    elif R1Clmn2T == True:
     if R2Clmn2T == False:
      Sd9 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 2".format(TwoPlayerName))
      R2Clmn2TBB = True
      R2Clmn2T = True
      time.sleep(1)
     elif R2Clmn2T == True:
      if R3Clmn2T == False:
       Sd16 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 2".format(TwoPlayerName))
       R3Clmn2TBB = True
       R3Clmn2T = True
       time.sleep(1)
      elif R3Clmn2T == True:
       if R4Clmn2T == False:
        Sd23 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 2".format(TwoPlayerName))
        R4Clmn2TBB = True
        R4Clmn2T = True
        time.sleep(1)
       elif R4Clmn2T == True:
        if R5Clmn2T == False:
         Sd30 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 2".format(TwoPlayerName))
         R5Clmn2TBB = True
         R5Clmn2T = True
         time.sleep(1)
        elif R5Clmn2T == True:
         if R6Clmn2T == False:
          Sd37 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 2".format(TwoPlayerName))
          R6Clmn2TBB = True
          R6Clmn2T = True
          time.sleep(1)
         elif R6Clmn2T == True:
          continue
   if Botgo == 3:
    if R1Clmn3T == False:
     Sd3 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 3".format(TwoPlayerName))
     R1Clmn3TBB = True
     R1Clmn3T = True
     time.sleep(1)
    elif R1Clmn3T == True:
     if R2Clmn3T == False:
      Sd10 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 3".format(TwoPlayerName))
      R2Clmn3TBB = True
      R2Clmn3T = True
      time.sleep(1)
     elif R2Clmn3T == True:
      if R3Clmn3T == False:
       Sd17 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 3".format(TwoPlayerName))
       R3Clmn3TBB = True
       R3Clmn3T = True
       time.sleep(1)
      elif R3Clmn3T == True:
       if R4Clmn3T == False:
        Sd24 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 3".format(TwoPlayerName))
        R4Clmn3TBB = True
        R4Clmn3T = True
        time.sleep(1)
       elif R4Clmn3T == True:
        if R5Clmn3T == False:
         Sd31 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 3".format(TwoPlayerName))
         R5Clmn3TBB = True
         R5Clmn3T = True
         time.sleep(1)
        elif R5Clmn3T == True:
         if R6Clmn3T == False:
          Sd38 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 3".format(TwoPlayerName))
          R6Clmn3TBB = True
          R6Clmn3T = True
          time.sleep(1)
         elif R6Clmn3T == True:
          continue
   if Botgo == 4:
    if R1Clmn4T == False:
     Sd4 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 4".format(TwoPlayerName))
     R1Clmn4TBB = True
     R1Clmn4T = True
     time.sleep(1)
    elif R1Clmn4T == True:
     if R2Clmn4T == False:
      Sd11 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 4".format(TwoPlayerName))
      R2Clmn4TBB = True
      R2Clmn4T = True
      time.sleep(1)
     elif R2Clmn4T == True:
      if R3Clmn4T == False:
       Sd18 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 4".format(TwoPlayerName))
       R3Clmn4TBB = True
       R3Clmn4T = True
       time.sleep(1)
      elif R3Clmn4T == True:
       if R4Clmn4T == False:
        Sd25 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 4".format(TwoPlayerName))
        R4Clmn4TBB = True
        R4Clmn4T = True
        time.sleep(1)
       elif R4Clmn4T == True:
        if R5Clmn4T == False:
         Sd32 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 4".format(TwoPlayerName))
         R5Clmn4TBB = True
         R5Clmn4T = True
         time.sleep(1)
        elif R5Clmn4T == True:
         if R6Clmn4T == False:
          Sd39 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 4".format(TwoPlayerName))
          R6Clmn4TBB = True
          R6Clmn4T = True
          time.sleep(1)
         elif R6Clmn4T == True:
          continue
   if Botgo == 5:
    if R1Clmn5T == False:
     Sd5 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 5".format(TwoPlayerName))
     R1Clmn5TBB = True
     R1Clmn5T = True
     time.sleep(1)
    elif R1Clmn5T == True:
     if R2Clmn5T == False:
      Sd12 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 5".format(TwoPlayerName))
      R2Clmn5TBB = True
      R2Clmn5T = True
      time.sleep(1)
     elif R2Clmn5T == True:
      if R3Clmn5T == False:
       Sd19 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 5".format(TwoPlayerName))
       R3Clmn5TBB = True
       R3Clmn5T = True
       time.sleep(1)
      elif R3Clmn5T == True:
       if R4Clmn5T == False:
        Sd26 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 5".format(TwoPlayerName))
        R4Clmn5TBB = True
        R4Clmn5T = True
        time.sleep(1)
       elif R4Clmn5T == True:
        if R5Clmn5T == False:
         Sd33 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 5".format(TwoPlayerName))
         R5Clmn5TBB = True
         R5Clmn5T = True
         time.sleep(1)
        elif R5Clmn5T == True:
         if R6Clmn5T == False:
          Sd40 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 5".format(TwoPlayerName))
          R6Clmn5TBB = True
          R6Clmn5T = True
          time.sleep(1)
         elif R6Clmn5T == True:
          continue
   if Botgo == 6:
    if R1Clmn6T == False:
     Sd6 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 6".format(TwoPlayerName))
     R1Clmn6TBB = True
     R1Clmn6T = True
     time.sleep(1)
    elif R1Clmn6T == True:
     if R2Clmn6T == False:
      Sd13 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 6".format(TwoPlayerName))
      R2Clmn6TBB = True
      R2Clmn6T = True
      time.sleep(1)
     elif R2Clmn6T == True:
      if R3Clmn6T == False:
       Sd20 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 6".format(TwoPlayerName))
       R3Clmn6TBB = True
       R3Clmn6T = True
       time.sleep(1)
      elif R3Clmn6T == True:
       if R4Clmn6T == False:
        Sd27 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 6".format(TwoPlayerName))
        R4Clmn6TBB = True
        R4Clmn6T = True
        time.sleep(1)
       elif R4Clmn6T == True:
        if R5Clmn6T == False:
         Sd34 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 6".format(TwoPlayerName))
         R5Clmn6TBB = True
         R5Clmn6T = True
         time.sleep(1)
        elif R5Clmn6T == True:
         if R6Clmn6T == False:
          Sd41 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 6".format(TwoPlayerName))
          R6Clmn6TBB = True
          R6Clmn6T = True
          time.sleep(1)
         elif R6Clmn6T == True:
          continue
   if Botgo == 7:
    if R1Clmn7T == False:
     Sd7 = BotSd
     NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
     print(NewConnect4Board)
     print("{} chose to fill in Row 1, Clmn 7".format(TwoPlayerName))
     R1Clmn7TBB = True
     R1Clmn7T = True
     time.sleep(1)
    elif R1Clmn7T == True:
     if R2Clmn7T == False:
      Sd14 = BotSd
      NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
      print(NewConnect4Board)
      print("{} chose to fill in Row 2, Clmn 7".format(TwoPlayerName))
      R2Clmn7TBB = True
      R2Clmn7T = True
      time.sleep(1)
     elif R2Clmn7T == True:
      if R3Clmn7T == False:
       Sd21 = BotSd
       NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
       print(NewConnect4Board)
       print("{} chose to fill in Row 3, Clmn 7".format(TwoPlayerName))
       R3Clmn7TBB = True
       R3Clmn7T = True
       time.sleep(1)
      elif R3Clmn7T == True:
       if R4Clmn7T == False:
        Sd28 = BotSd
        NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
        print(NewConnect4Board)
        print("{} chose to fill in Row 4, Clmn 7".format(TwoPlayerName))
        R4Clmn7TBB = True
        R4Clmn7T = True
        time.sleep(1)
       elif R4Clmn7T == True:
        if R5Clmn7T == False:
         Sd35 = BotSd
         NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
         print(NewConnect4Board)
         print("{} chose to fill in Row 5, Clmn 7".format(TwoPlayerName))
         R5Clmn7TBB = True
         R5Clmn7T = True
         time.sleep(1)
        elif R5Clmn7T == True:
         if R6Clmn7T == False:
          Sd42 = BotSd
          NewConnect4Board = Connect4Board.format(Sd1,Sd2,Sd3,Sd4,Sd5,Sd6,Sd7,Sd8,Sd9,Sd10,Sd11,Sd12,Sd13,Sd14,Sd15,Sd16,Sd17,Sd18,Sd19,Sd20,Sd21,Sd22,Sd23,Sd24,Sd25,Sd26,Sd27,Sd28,Sd29,Sd30,Sd31,Sd32,Sd33,Sd34,Sd35,Sd36,Sd37,Sd38,Sd39,Sd40,Sd41,Sd42)
          print(NewConnect4Board)
          print("{} chose to fill in Row 6, Clmn 7".format(TwoPlayerName))
          R6Clmn7TBB = True
          R6Clmn7T = True
          time.sleep(1)
         elif R6Clmn7T == True:
          continue
   clearScreen()
   if (R1Clmn1TBB == True and R2Clmn1TBB == True and R3Clmn1TBB == True and R4Clmn1TBB == True) or (R1Clmn1TBB == True and R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4TBB == True) or (R1Clmn1TBB == True and R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4TBB == True) or (R1Clmn2TBB == True and R2Clmn2TBB == True and R3Clmn2TBB == True and R4Clmn2TBB == True) or (R1Clmn2TBB == True and R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5TBB == True) or (R1Clmn2TBB == True and R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5TBB == True) or (R1Clmn3TBB == True and R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3TBB == True) or (R1Clmn3TBB == True and R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6TBB == True) or (R1Clmn3TBB == True and R1Clmn4TBB == True and R1Clmn5TBB == True and R1Clmn6TBB == True) or (R1Clmn4TBB == True and R2Clmn3TBB == True and R3Clmn2TBB == True and R4Clmn1TBB == True) or (R1Clmn4TBB == True and R2Clmn4TBB == True and R3Clmn4TBB == True and R4Clmn4TBB == True) or (R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2TBB == True and R1Clmn1TBB == True) or (R1Clmn5TBB == True and R2Clmn4TBB == True and R3Clmn3TBB == True and R4Clmn2TBB == True) or (R1Clmn5TBB == True and R2Clmn5TBB == True and R3Clmn5TBB == True and R4Clmn5TBB == True) or (R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3TBB == True and R1Clmn2TBB == True) or (R1Clmn6TBB == True and R2Clmn5TBB == True and R3Clmn4TBB == True and R4Clmn3TBB == True) or (R1Clmn6TBB == True and R2Clmn6TBB == True and R3Clmn6TBB == True and R4Clmn6TBB == True) or (R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4TBB == True and R1Clmn3TBB == True) or (R1Clmn7TBB == True and R1Clmn6TBB == True and R1Clmn5TBB == True and R1Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4TBB == True) or (R1Clmn7TBB == True and R2Clmn7TBB == True and R3Clmn7TBB == True and R4Clmn7TBB == True) or (R2Clmn1TBB == True and R3Clmn1TBB == True and R4Clmn1TBB == True and R5Clmn1TBB == True) or (R2Clmn1TBB == True and R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4TBB == True) or (R2Clmn1TBB == True and R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4TBB == True) or (R2Clmn2TBB == True and R3Clmn2TBB == True and R4Clmn2TBB == True and R5Clmn2TBB == True) or (R2Clmn2TBB == True and R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5TBB == True) or (R2Clmn2TBB == True and R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5TBB == True) or (R2Clmn3TBB == True and R3Clmn3TBB == True and R4Clmn3TBB == True and R5Clmn3TBB == True) or (R2Clmn3TBB == True and R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6TBB == True) or (R2Clmn3TBB == True and R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6TBB == True) or (R2Clmn4TBB == True and R3Clmn4TBB == True and R4Clmn4TBB == True and R5Clmn4TBB == True) or (R2Clmn4TBB == True and R2Clmn5TBB == True and R2Clmn6TBB == True and R2Clmn7TBB == True) or (R2Clmn4TBB == True and R3Clmn5TBB == True and R4Clmn6TBB == True and R5Clmn7TBB == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R2Clmn5TBB == True and R3Clmn5TBB == True and R4Clmn5TBB == True and R5Clmn5TBB == True) or (R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True and R2Clmn2TBB == True) or (R2Clmn6TBB == True and R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3TBB == True) or (R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4TBB == True and R2Clmn3TBB == True) or (R2Clmn6TBB == True and R3Clmn6TBB == True and R4Clmn6TBB == True and R5Clmn6TBB == True) or (R2Clmn7TBB == True and R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4TBB == True) or (R2Clmn7TBB == True and R3Clmn7TBB == True and R4Clmn7TBB == True and R5Clmn7TBB == True) or (R2Clmn7TBB == True and R2Clmn6TBB == True and R2Clmn5TBB == True and R2Clmn4TBB == True) or (R3Clmn1TBB == True and R4Clmn1TBB == True and R5Clmn1TBB == True and R6Clmn1TBB == True) or (R3Clmn1TBB == True and R4Clmn2TBB == True and R5Clmn3TBB == True and R6Clmn4TBB == True) or (R3Clmn1TBB == True and R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4TBB == True) or (R3Clmn2TBB == True and R4Clmn2TBB == True and R5Clmn2TBB == True and R6Clmn2TBB == True) or (R3Clmn2TBB == True and R4Clmn3TBB == True and R5Clmn4TBB == True and R6Clmn5TBB == True) or (R3Clmn2TBB == True and R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5TBB == True) or (R3Clmn3TBB == True and R4Clmn3TBB == True and R5Clmn3TBB == True and R6Clmn3TBB == True) or (R3Clmn3TBB == True and R4Clmn4TBB == True and R5Clmn5TBB == True and R6Clmn6TBB == True) or (R3Clmn3TBB == True and R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6TBB == True) or (R3Clmn4TBB == True and R4Clmn4TBB == True and R5Clmn4TBB == True and R6Clmn4TBB == True) or (R3Clmn4TBB == True and R3Clmn5TBB == True and R3Clmn6TBB == True and R3Clmn7TBB == True) or (R3Clmn4TBB == True and R4Clmn5TBB == True and R5Clmn6TBB == True and R6Clmn7TBB == True) or (R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3TBB == True and R3Clmn2TBB == True) or (R3Clmn5TBB == True and R4Clmn5TBB == True and R5Clmn5TBB == True and R6Clmn5TBB == True) or (R3Clmn5TBB == True and R4Clmn4TBB == True and R5Clmn3TBB == True and R6Clmn2TBB == True) or (R3Clmn6TBB == True and R4Clmn5TBB == True and R5Clmn4TBB == True and R6Clmn3TBB == True) or (R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4TBB == True and R3Clmn3TBB == True) or (R3Clmn6TBB == True and R4Clmn6TBB == True and R5Clmn6TBB == True and R6Clmn6TBB == True) or (R3Clmn7TBB == True and R4Clmn6TBB == True and R5Clmn5TBB == True and R6Clmn4TBB == True) or (R3Clmn7TBB == True and R4Clmn7TBB == True and R5Clmn7TBB == True and R6Clmn7TBB == True) or (R3Clmn7TBB == True and R3Clmn6TBB == True and R3Clmn5TBB == True and R3Clmn4TBB == True) or (R4Clmn1TBB == True and R3Clmn1TBB == True and R2Clmn1TBB == True and R1Clmn1TBB == True) or (R4Clmn1TBB == True and R3Clmn2TBB == True and R2Clmn3TBB == True and R1Clmn4TBB == True) or (R4Clmn1TBB == True and R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4TBB == True) or (R4Clmn2TBB == True and R3Clmn2TBB == True and R2Clmn2TBB == True and R1Clmn2TBB == True) or (R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4TBB == True and R1Clmn5TBB == True) or (R4Clmn2TBB == True and R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5TBB == True) or (R4Clmn3TBB == True and R3Clmn3TBB == True and R2Clmn3TBB == True and R1Clmn3TBB == True) or (R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5TBB == True and R1Clmn6TBB == True) or (R4Clmn3TBB == True and R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6TBB == True) or (R4Clmn4TBB == True and R3Clmn4TBB == True and R2Clmn4TBB == True and R1Clmn4TBB == True) or (R4Clmn4TBB == True and R4Clmn5TBB == True and R4Clmn6TBB == True and R4Clmn7TBB == True) or (R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6TBB == True and R1Clmn7TBB == True) or (R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3TBB == True and R4Clmn2TBB == True) or (R4Clmn5TBB == True and R3Clmn5TBB == True and R2Clmn5TBB == True and R1Clmn5TBB == True) or (R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3TBB == True and R1Clmn2TBB == True) or (R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4TBB == True and R1Clmn3TBB == True) or (R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4TBB == True and R4Clmn3TBB == True) or (R4Clmn6TBB == True and R3Clmn6TBB == True and R2Clmn6TBB == True and R1Clmn6TBB == True) or (R4Clmn7TBB == True and R3Clmn6TBB == True and R2Clmn5TBB == True and R1Clmn4TBB == True) or (R4Clmn7TBB == True and R3Clmn7TBB == True and R2Clmn7TBB == True and R1Clmn7TBB == True) or (R4Clmn7TBB == True and R4Clmn6TBB == True and R4Clmn5TBB == True and R4Clmn4TBB == True) or (R5Clmn1TBB == True and R4Clmn1TBB == True and R3Clmn1TBB == True and R2Clmn1TBB == True) or (R5Clmn1TBB == True and R4Clmn2TBB == True and R3Clmn3TBB == True and R2Clmn4TBB == True) or (R5Clmn1TBB == True and R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4TBB == True) or (R5Clmn2TBB == True and R4Clmn2TBB == True and R3Clmn2TBB == True and R2Clmn2TBB == True) or (R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4TBB == True and R2Clmn5TBB == True) or (R5Clmn2TBB == True and R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5TBB == True) or (R5Clmn3TBB == True and R4Clmn3TBB == True and R3Clmn3TBB == True and R2Clmn3TBB == True) or (R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5TBB == True and R2Clmn6TBB == True) or (R5Clmn3TBB == True and R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6TBB == True) or (R5Clmn4TBB == True and R4Clmn4TBB == True and R3Clmn4TBB == True and R2Clmn4TBB == True) or (R5Clmn4TBB == True and R5Clmn5TBB == True and R5Clmn6TBB == True and R5Clmn7TBB == True) or (R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6TBB == True and R2Clmn7TBB == True) or (R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3TBB == True and R5Clmn2TBB == True) or (R5Clmn5TBB == True and R4Clmn5TBB == True and R3Clmn5TBB == True and R2Clmn5TBB == True) or (R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3TBB == True and R2Clmn2TBB == True) or (R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4TBB == True and R2Clmn3TBB == True) or (R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4TBB == True and R5Clmn3TBB == True) or (R5Clmn6TBB == True and R4Clmn6TBB == True and R3Clmn6TBB == True and R2Clmn6TBB == True) or (R5Clmn7TBB == True and R4Clmn6TBB == True and R3Clmn5TBB == True and R2Clmn4TBB == True) or (R5Clmn7TBB == True and R4Clmn7TBB == True and R3Clmn7TBB == True and R2Clmn7TBB == True) or (R5Clmn7TBB == True and R5Clmn6TBB == True and R5Clmn5TBB == True and R5Clmn4TBB == True) or (R6Clmn1TBB == True and R5Clmn1TBB == True and R4Clmn1TBB == True and R3Clmn1TBB == True) or (R6Clmn1TBB == True and R5Clmn2TBB == True and R4Clmn3TBB == True and R3Clmn4TBB == True) or (R6Clmn1TBB == True and R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4TBB == True) or (R6Clmn2TBB == True and R5Clmn2TBB == True and R4Clmn2TBB == True and R3Clmn2TBB == True) or (R6Clmn2TBB == True and R5Clmn3TBB == True and R4Clmn4TBB == True and R3Clmn5TBB == True) or (R6Clmn2TBB == True and R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5TBB == True) or (R6Clmn3TBB == True and R5Clmn3TBB == True and R4Clmn3TBB == True and R3Clmn3TBB == True) or (R6Clmn3TBB == True and R5Clmn4TBB == True and R4Clmn5TBB == True and R3Clmn6TBB == True) or (R6Clmn3TBB == True and R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6TBB == True) or (R6Clmn4TBB == True and R5Clmn4TBB == True and R4Clmn4TBB == True and R3Clmn4TBB == True) or (R6Clmn4TBB == True and R6Clmn5TBB == True and R6Clmn6TBB == True and R6Clmn7TBB == True) or (R6Clmn4TBB == True and R5Clmn5TBB == True and R4Clmn6TBB == True and R3Clmn7TBB == True) or (R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3TBB == True and R6Clmn2TBB == True) or (R6Clmn5TBB == True and R5Clmn5TBB == True and R4Clmn5TBB == True and R3Clmn5TBB == True) or (R6Clmn5TBB == True and R5Clmn4TBB == True and R4Clmn3TBB == True and R3Clmn2TBB == True) or (R6Clmn6TBB == True and R5Clmn5TBB == True and R4Clmn4TBB == True and R3Clmn3TBB == True) or (R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4TBB == True and R6Clmn3TBB == True) or (R6Clmn6TBB == True and R5Clmn6TBB == True and R4Clmn6TBB == True and R3Clmn6TBB == True) or (R6Clmn7TBB == True and R5Clmn6TBB == True and R4Clmn5TBB == True and R3Clmn4TBB == True) or (R6Clmn7TBB == True and R5Clmn7TBB == True and R4Clmn7TBB == True and R3Clmn7TBB == True) or (R6Clmn7TBB == True and R6Clmn6TBB == True and R6Clmn5TBB == True and R6Clmn4TBB == True):
    print(NewConnect4Board)
    print("")
    print("{} ".format(TwoPlayerName)+Blue+"has connected four!"+reset)
    print("")
    Botpoints = Botpoints + 1
    PETC_function()
    Yourshape = 1
    Botshape = 2
    YourSd = Red+"O"+reset
    BotSd = Blue+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   elif R1Clmn1T == True and R1Clmn2T == True and R1Clmn3T == True and R1Clmn4T == True and R1Clmn5T == True and R1Clmn6T == True and R1Clmn7T == True and R2Clmn1T == True and R2Clmn2T == True and  R2Clmn3T == True and R2Clmn4T == True and R2Clmn5T == True and R2Clmn6T == True and R2Clmn7T == True and R3Clmn1T == True and R3Clmn2T == True and R3Clmn3T == True and R3Clmn4T == True and R3Clmn5T == True and R3Clmn6T == True and R3Clmn7T == True and R4Clmn1T == True and R4Clmn2T == True and R4Clmn3T == True and R4Clmn4T == True and R4Clmn5T == True and R4Clmn6T == True and R4Clmn7T == True and R5Clmn1T == True and R5Clmn2T == True and R5Clmn3T == True and R5Clmn4T == True and R5Clmn5T == True and R5Clmn6T == True and R5Clmn7T == True and R6Clmn1T == True and R6Clmn2T == True and R6Clmn3T == True and R6Clmn4T == True and R6Clmn5T == True and R6Clmn6T == True and R6Clmn7T == True:
    print(NewConnect4Board)
    print("")
    print("DRAW!")
    print("")
    PETC_function()
    Yourshape = 1
    Botshape = 2
    YourSd = Red+"O"+reset
    BotSd = Blue+"O"+reset
    Sd1 = "_"
    Sd2 = "_"
    Sd3 = "_"
    Sd4 = "_"
    Sd5 = "_"
    Sd6 = "_"
    Sd7 = "_"
    Sd8 = "_"
    Sd9 = "_"
    Sd10 = "_"
    Sd11 = "_"
    Sd12 = "_"
    Sd13 = "_"
    Sd14 = "_"
    Sd15 = "_"
    Sd16 = "_"
    Sd17 = "_"
    Sd18 = "_"
    Sd19 = "_"
    Sd20 = "_"
    Sd21 = "_"
    Sd22 = "_"
    Sd23 = "_"
    Sd24 = "_"
    Sd25 = "_"
    Sd26 = "_"
    Sd27 = "_"
    Sd28 = "_"
    Sd29 = "_"
    Sd30 = "_"
    Sd31 = "_"
    Sd32 = "_"
    Sd33 = "_"
    Sd34 = "_"
    Sd35 = "_"
    Sd36 = "_"
    Sd37 = "_"
    Sd38 = "_"
    Sd39 = "_"
    Sd40 = "_"
    Sd41 = "_"
    Sd42 = "_"
    R1Clmn1T = False
    R1Clmn2T = False
    R1Clmn3T = False
    R1Clmn4T = False
    R1Clmn5T = False
    R1Clmn6T = False
    R1Clmn7T = False
    R2Clmn1T = False
    R2Clmn2T = False 
    R2Clmn3T = False
    R2Clmn4T = False
    R2Clmn5T = False
    R2Clmn6T = False
    R2Clmn7T = False
    R3Clmn1T = False
    R3Clmn2T = False
    R3Clmn3T = False
    R3Clmn4T = False
    R3Clmn5T = False
    R3Clmn6T = False
    R3Clmn7T = False
    R4Clmn1T = False
    R4Clmn2T = False
    R4Clmn3T = False
    R4Clmn4T = False
    R4Clmn5T = False
    R4Clmn6T = False
    R4Clmn7T = False
    R5Clmn1T = False
    R5Clmn2T = False
    R5Clmn3T = False
    R5Clmn4T = False
    R5Clmn5T = False
    R5Clmn6T = False
    R5Clmn7T = False
    R6Clmn1T = False
    R6Clmn2T = False
    R6Clmn3T = False
    R6Clmn4T = False
    R6Clmn5T = False
    R6Clmn6T = False
    R6Clmn7T = False
    R1Clmn1TBY = False
    R1Clmn2TBY = False
    R1Clmn3TBY = False
    R1Clmn4TBY = False
    R1Clmn5TBY = False
    R1Clmn6TBY = False
    R1Clmn7TBY = False
    R2Clmn1TBY = False
    R2Clmn2TBY = False 
    R2Clmn3TBY = False
    R2Clmn4TBY = False
    R2Clmn5TBY = False
    R2Clmn6TBY = False
    R2Clmn7TBY = False
    R3Clmn1TBY = False
    R3Clmn2TBY = False
    R3Clmn3TBY = False
    R3Clmn4TBY = False
    R3Clmn5TBY = False
    R3Clmn6TBY = False
    R3Clmn7TBY = False
    R4Clmn1TBY = False
    R4Clmn2TBY = False
    R4Clmn3TBY = False
    R4Clmn4TBY = False
    R4Clmn5TBY = False
    R4Clmn6TBY = False
    R4Clmn7TBY = False
    R5Clmn1TBY = False
    R5Clmn2TBY = False
    R5Clmn3TBY = False
    R5Clmn4TBY = False
    R5Clmn5TBY = False
    R5Clmn6TBY = False
    R5Clmn7TBY = False
    R6Clmn1TBY = False
    R6Clmn2TBY = False
    R6Clmn3TBY = False
    R6Clmn4TBY = False
    R6Clmn5TBY = False
    R6Clmn6TBY = False
    R6Clmn7TBY = False
    R1Clmn1TBB = False
    R1Clmn2TBB = False
    R1Clmn3TBB = False
    R1Clmn4TBB = False
    R1Clmn5TBB = False
    R1Clmn6TBB = False
    R1Clmn7TBB = False
    R2Clmn1TBB = False
    R2Clmn2TBB = False 
    R2Clmn3TBB = False
    R2Clmn4TBB = False
    R2Clmn5TBB = False
    R2Clmn6TBB = False
    R2Clmn7TBB = False
    R3Clmn1TBB = False
    R3Clmn2TBB = False
    R3Clmn3TBB = False
    R3Clmn4TBB = False
    R3Clmn5TBB = False
    R3Clmn6TBB = False
    R3Clmn7TBB = False
    R4Clmn1TBB = False
    R4Clmn2TBB = False
    R4Clmn3TBB = False
    R4Clmn4TBB = False
    R4Clmn5TBB = False
    R4Clmn6TBB = False
    R4Clmn7TBB = False
    R5Clmn1TBB = False
    R5Clmn2TBB = False
    R5Clmn3TBB = False
    R5Clmn4TBB = False
    R5Clmn5TBB = False
    R5Clmn6TBB = False
    R5Clmn7TBB = False
    R6Clmn1TBB = False
    R6Clmn2TBB = False
    R6Clmn3TBB = False
    R6Clmn4TBB = False
    R6Clmn5TBB = False
    R6Clmn6TBB = False
    R6Clmn7TBB = False
   Botturn = False
   clearScreen()
 if Yourpoints == 1:
  return "W"
 elif Botpoints == 1:
  return "L"
#CONNECT FOUR