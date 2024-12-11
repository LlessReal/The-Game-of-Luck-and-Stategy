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

def level7_function():
 GTNLoses = 0
 GTNWins = 0
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
   Explained = True
   continue
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   II_function()
 while True:
  v = random.randrange(1,8)
  BotChoice = random.randrange(1,8)
  print("Guess a number from 1 - 7")
  time.sleep(0.25)
  PNTCOQ_function()
  try:
   YourChoice = int(input(""))
  except:
   II_function()
   continue 
  Quitchoice = 0
  while YourChoice == 0:
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
  YourChoiceIsClose = math.isclose(YourChoice, v, abs_tol = 1)
  BotChoiceIsClose = math.isclose(BotChoice, v, abs_tol = 1)
  print("The number generated was...")
  time.sleep(1)
  TheNumber = "{}!"
  print(TheNumber.format(v))
  time.sleep(1)
  if YourChoice == v:
   GTNWins = GTNWins + 1
   YourDecision = "You chose {}, so you get a point"
  elif YourChoice != v and YourChoiceIsClose == True:
   GTNWins = GTNWins + 0.5
   YourDecision = "You chose {}, so you get half a point"
  elif YourChoice != v and YourChoiceIsClose == False:
   YourDecision = "You chose {}, so you get no points"
  print(YourDecision.format(YourChoice))
  time.sleep(1)
  print("")
  if BotChoice == v:
   GTNLoses = GTNLoses + 1
   BotsDecision = "Your opponent chose {}, so your opponent gets a point"
  elif BotChoice != v and BotChoiceIsClose == True:
   GTNLoses = GTNLoses + 0.5
   BotsDecision = "Your opponent chose {}, so your opponent gets half a point"
  elif BotChoice != v and BotChoiceIsClose == False:
   BotsDecision = "Your opponent chose {}, so your opponent gets no points"
  print(BotsDecision.format(BotChoice))
  time.sleep(1)
  print("")
  print(Scorebrd.format(GTNWins,GTNLoses))
  PETC_function()
  if GTNWins >= 3 and GTNLoses < 3:
   print('''You were the first to reach 3 points, 
Therefore, '''+Blue+'''you won the game of Guess the Number!'''+reset)
   PETC_function()
   return "W"
  elif GTNWins < 3 and GTNLoses >= 3:
   print('''Your opponent was the first to reach 3 points, 
Therefore, '''+Red+'''you lost the game of Guess the Number.'''+reset)
   PETC_function()
   return "L"
  elif GTNWins >= 3 and GTNLoses >= 3:
   print("It looks like you both hit 3 or over 3 at the same time! ")
   time.sleep(1)
   print("")
   print("Time for a tie breaker!")
   time.sleep(1)
   def tiebreaker_function():
    print('''This time, the number generated will be from 1 - 5
First challenger to guess it wins!
This will recur if both you and your opponent guess it right though.''')
    PETC_function()
    while True:
     v = random.randrange(1,6)
     BotChoice = random.randrange(1,6)
     try:
      YourChoice = int(input('''Guess a number from 1 - 5
'''))
     except:
      II_function()
      continue 
     print("The number generated was...")
     time.sleep(1)
     TheNumber = "{}!"
     print(TheNumber.format(v))
     time.sleep(1)
     print("")
     YourDecision = "You chose {}"
     print(YourDecision.format(YourChoice))
     time.sleep(1)
     print("")
     BotsDecision = "Your opponent chose {}"
     print(BotsDecision.format(BotChoice))
     time.sleep(1)
     print("")
     if YourChoice == v and BotChoice == v :
      print('''You and your opponent guessed the number correctly

Therefore, the tiebreaker has not been settled yet''')
      PETC_function()
      continue
     elif YourChoice != v and BotChoice != v:
      print('''You and your opponent guessed the number incorrectly

Therefore, the tiebreaker has not been settled yet''')
      PETC_function()
      continue 
     elif YourChoice == v and BotChoice != v:
      print('''You guessed the number correctly and your opponent did not

Therefore, '''+Blue+'''YOU WON THE TIEBREAKER FOR GUESS THE NUMBER!'''+reset)
      PETC_function()
      return "W"
     elif YourChoice != v and BotChoice == v:
      print('''You guessed the number correctly and your opponent did not

Therefore, '''+Red+'''you lost the tiebreaker for Guess the number.'''+reset)
      PETC_function()
      return "L"
   tiebreaker_function()
   if tiebreaker_function() == "L":
     return "L"
   elif tiebreaker_function() == "W":
     return "W"
#Level 7 - Guess the number 

def pvplevel7_function(OnePlayerName,TwoPlayerName):
 GTNLoses = 0
 GTNWins = 0
 Scorebrdpvp = '''Scoreboard:

{0} - {1} pts.

{2} - {3} pts'''
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
   Explained = True
   continue
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   II_function()
 while True:
  v = random.randrange(1,8)
  print("{}! Guess a number from 1 - 7".format(OnePlayerName))
  time.sleep(0.25)
  PNTCOQ_function()
  try:
   YourChoice = int(input(""))
   clearScreen()
  except:
   II_function()
   continue 
  Quitchoice = 0
  while YourChoice == 0:
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
  if YourChoice <= 0 or YourChoice >= 8:
   II_function()
   continue
  while True:
   print("{}! Guess a number from 1 - 7".format(TwoPlayerName))
   time.sleep(0.25)
   PNTCOQ_function()
   try:
    BotChoice = int(input(""))
    clearScreen()
   except:
    II_function()
    continue 
   Quitchoice = 0
   while BotChoice == 0:
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
   if BotChoice <= 0 or BotChoice >= 8:
    II_function()
    continue
   break
  YourChoiceIsClose = math.isclose(YourChoice, v, abs_tol = 1)
  BotChoiceIsClose = math.isclose(BotChoice, v, abs_tol = 1)
  print("The number generated was...")
  time.sleep(0.5)
  print("")
  TheNumber = "{}!"
  print(TheNumber.format(v))
  time.sleep(0.5)
  print("")
  if YourChoice == v:
   GTNWins = GTNWins + 1
   YourDecision = "{0} chose {1}, so {0} get a point"
  elif YourChoice != v and YourChoiceIsClose == True:
   GTNWins = GTNWins + 0.5
   YourDecision = "{0} chose {1}, so {0} get half a point"
  elif YourChoice != v and YourChoiceIsClose == False:
   YourDecision = "{0} chose {1}, so {0} get no points"
  print(YourDecision.format(OnePlayerName,YourChoice))
  time.sleep(0.25)
  print("")
  if BotChoice == v:
   GTNLoses = GTNLoses + 1
   BotsDecision = "{0} chose {1}, so {0} gets a point"
  elif BotChoice != v and BotChoiceIsClose == True:
   GTNLoses = GTNLoses + 0.5
   BotsDecision = "{0} chose {1}, so {0} gets half a point"
  elif BotChoice != v and BotChoiceIsClose == False:
   BotsDecision = "{0} chose {1}, so {0} gets no points"
  print(BotsDecision.format(TwoPlayerName,BotChoice))
  time.sleep(0.25)
  print("")
  print(Scorebrdpvp.format(OnePlayerName,GTNWins,TwoPlayerName,GTNLoses))
  PETC_function()
  if GTNWins >= 3 and GTNLoses < 3:
   print('''{} '''.format(OnePlayerName)+Blue+'''was the first to reach 3 points!'''+reset)
   PETC_function()
   return "W"
  elif GTNWins < 3 and GTNLoses >= 3:
   print('''{} '''.format(TwoPlayerName)+Blue+'''was the first to reach 3 points!'''+reset)
   PETC_function()
   return "L"
  elif GTNWins >= 3 and GTNLoses >= 3:
   print("It looks like {0} and {1} both hit 3 or over 3 at the same time! ".format(OnePlayerName,TwoPlayerName))
   time.sleep(1)
   print("")
   print("Time for a tie breaker!")
   time.sleep(1)
   def tiebreaker_function():
    print('''This time, the number generated will be from 1 - 5
First challenger to guess it wins!
This will recur if both you and your opponent guess it right though.''')
    PETC_function()
    while True:
     v = random.randrange(1,6)
     BotChoice = random.randrange(1,6)
     try:
      print('''{}! Guess a number from 1 - 5'''.format(OnePlayerName))
      YourChoice = int(input(""))
      clearScreen()
     except:
      II_function()
      continue 
     print("The number generated was...")
     time.sleep(1)
     TheNumber = "{}!"
     print(TheNumber.format(v))
     time.sleep(1)
     print("")
     YourDecision = "{0} chose {1}"
     print(YourDecision.format(OnePlayerName,YourChoice))
     time.sleep(1)
     print("")
     BotsDecision = "{0} chose {1}"
     print(BotsDecision.format(TwoPlayerName,BotChoice))
     time.sleep(1)
     print("")
     if YourChoice == v and BotChoice == v:
      print('''It looks like {0} and {1} guessed the number correctly

Therefore, the tiebreaker has not been settled yet'''.format(OnePlayerName,TwoPlayerName))
      PETC_function()
      continue
     elif YourChoice != v and BotChoice != v:
      print('''It looks like {0} and {1} guessed the number incorrectly

Therefore, the tiebreaker has not been settled yet'''.format(OnePlayerName,TwoPlayerName))
      PETC_function()
      continue 
     elif YourChoice == v and BotChoice != v:
      print('''{0} guessed the number correctly and {1} did not

Therefore, '''.format(OnePlayerName,TwoPlayerName)+'''{} '''.format(OnePlayerName)+Blue+'''won the tiebreaker for Guess the Number!'''+reset)
      PETC_function()
      return "W"
     elif YourChoice != v and BotChoice == v:
      print('''{0} guessed the number correctly and {1} did not

Therefore, '''.format(TwoPlayerName,OnePlayerName)+Red+'''{} '''.format(TwoPlayerName)+Blue+'''won the tiebreaker for Guess the number.'''+reset)
      PETC_function()
      return "L"
   tiebreaker_function()
   if tiebreaker_function() == "L":
     return "L"
   elif tiebreaker_function() == "W":
     return "W"
#Level 7 - Guess the number 