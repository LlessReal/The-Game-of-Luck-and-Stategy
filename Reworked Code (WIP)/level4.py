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

def level4_function():
 RPSLoses = 0
 RPSWins = 0
 RPSList = ["","rock","paper","scissors"]
 Scorebrd = '''Scoreboard:

You - {} pts.

Bot - {} pts'''
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
   print('''1 - You choose rock, paper, or scissors to be your weapon.''') 
   PETC_function()
   print('''2 - Your opponent will do the same and you both will clash''')
   PETC_function()
   print('''3 - Rock beats scissors, 
paper beats rock, 
and scissors beats paper.''')
   PETC_function()
   print('''4 - If you and your opponent choose the same weapon,
then the clash will be a draw.''')
   PETC_function()
   print('''5 - Whenever you win a clash, you gain a point ''')
   PETC_function()
   print('''6 - Whoever gets 3 points between you and your opponent will win!''')
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
 while RPSLoses != 3 and RPSWins != 3:
  RPSBot = random.randrange(1,4)
  try:
   print("Choose your weapon:")
   time.sleep(0.5)
   print('''
1 - Rock''')
   time.sleep(0.1)
   print('''
2 - Paper''')
   time.sleep(0.1)
   print('''
3 - Scissors''')
   time.sleep(0.1)
   print('''
4 - Random''')
   time.sleep(0.1)
   PNTCOQ_function()
   RPSChoice = int(input(""))
  except:
   II_function()
   continue
  Quitchoice = 0
  while RPSChoice == 0:
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
  if Quitchoice == 2:
   continue
  RPSBot = random.randrange(1,4)
  clearScreen()
  if RPSChoice == 1:
   print("You chose rock.")
  elif RPSChoice == 2:
   print("You chose paper.")
  elif RPSChoice == 3: 
   print("You chose scissors.")
  elif RPSChoice == 4:
   RPSChoice = random.randrange(1,4)
   print("You decided to randomly choose a weapon.")
   time.sleep(1)
   RPW = "You randomly chose {}."
   print(RPW.format(RPSList[RPSChoice]))
  else:
   II_function()
   continue
  time.sleep(1)
  print("")
  if RPSBot == 1:
   print("Your opponent chose rock.")
  elif RPSBot == 2:
   print("Your opponent chose paper")
  elif RPSBot == 3: 
   print("Your opponent chose scissors")
  time.sleep(1)
  print("")
  if RPSChoice == RPSBot:
   print("Draw!")
  elif (RPSChoice == 1 and RPSBot == 2) or (RPSChoice == 3 and RPSBot == 1) or (RPSChoice == 2 and RPSBot == 3):
   print("You opponent gains one point.")
   RPSLoses = RPSLoses + 1
  elif (RPSChoice == 2 and RPSBot == 1) or (RPSChoice == 1 and RPSBot == 3) or (RPSChoice == 3 and RPSBot == 2):
   print("You gain one point.")
   RPSWins = RPSWins + 1
  print("")
  print(Scorebrd.format(RPSWins,RPSLoses))
  PETC_function()
 if RPSWins == 3:
  print('''You are the first to gain 3 points.''')
  time.sleep(1)
  print('''
Therefore, '''+Blue+'''YOU WON A GAME OF ROCK PAPER SCISSORS!'''+reset)
  PETC_function()
  return "W"
 elif RPSLoses == 3:
  print('''Your opponent was the first to gain 3 points.''')
  time.sleep(1)
  print('''
Therefore, '''+Red+'''you lost a game of Rock Paper Scissors'''+reset)
  PETC_function()
  return "L"
   
def pvplevel4_function():
 RPSLoses = 0
 RPSWins = 0
 RPSList = ["","rock","paper","scissors"]
 Scorebrd = '''Scoreboard:

You - {} pts.

Bot - {} pts'''
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
   print('''1 - You choose rock, paper, or scissors to be your weapon.''') 
   PETC_function()
   print('''2 - Your opponent will do the same and you both will clash''')
   PETC_function()
   print('''3 - Rock beats scissors, 
paper beats rock, 
and scissors beats paper.''')
   PETC_function()
   print('''4 - If you and your opponent choose the same weapon,
then the clash will be a draw.''')
   PETC_function()
   print('''5 - Whenever you win a clash, you gain a point ''')
   PETC_function()
   print('''6 - Whoever gets 3 points between you and your opponent will win!''')
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
 while RPSLoses != 3 and RPSWins != 3:
  RPSBot = random.randrange(1,4)
  try:
   print("Choose your weapon:")
   time.sleep(0.5)
   print('''
1 - Rock''')
   time.sleep(0.1)
   print('''
2 - Paper''')
   time.sleep(0.1)
   print('''
3 - Scissors''')
   time.sleep(0.1)
   print('''
4 - Random''')
   time.sleep(0.1)
   PNTCOQ_function()
   RPSChoice = int(input(""))
  except:
   II_function()
   continue
  Quitchoice = 0
  while RPSChoice == 0:
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
  if Quitchoice == 2:
   continue
  RPSBot = random.randrange(1,4)
  clearScreen()
  if RPSChoice == 1:
   print("You chose rock.")
  elif RPSChoice == 2:
   print("You chose paper.")
  elif RPSChoice == 3: 
   print("You chose scissors.")
  elif RPSChoice == 4:
   RPSChoice = random.randrange(1,4)
   print("You decided to randomly choose a weapon.")
   time.sleep(1)
   RPW = "You randomly chose {}."
   print(RPW.format(RPSList[RPSChoice]))
  else:
   II_function()
   continue
  time.sleep(1)
  print("")
  if RPSBot == 1:
   print("Your opponent chose rock.")
  elif RPSBot == 2:
   print("Your opponent chose paper")
  elif RPSBot == 3: 
   print("Your opponent chose scissors")
  time.sleep(1)
  print("")
  if RPSChoice == RPSBot:
   print("Draw!")
  elif (RPSChoice == 1 and RPSBot == 2) or (RPSChoice == 3 and RPSBot == 1) or (RPSChoice == 2 and RPSBot == 3):
   print("You opponent gains one point.")
   RPSLoses = RPSLoses + 1
  elif (RPSChoice == 2 and RPSBot == 1) or (RPSChoice == 1 and RPSBot == 3) or (RPSChoice == 3 and RPSBot == 2):
   print("You gain one point.")
   RPSWins = RPSWins + 1
  print("")
  print(Scorebrd.format(RPSWins,RPSLoses))
  PETC_function()
 if RPSWins == 3:
  print('''You are the first to gain 3 points.''')
  time.sleep(1)
  print('''
Therefore, '''+Blue+'''YOU WON A GAME OF ROCK PAPER SCISSORS!'''+reset)
  PETC_function()
  return "W"
 elif RPSLoses == 3:
  print('''Your opponent was the first to gain 3 points.''')
  time.sleep(1)
  print('''
Therefore, '''+Red+'''you lost a game of Rock Paper Scissors'''+reset)
  PETC_function()
  return "L"