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
def NumChoiceWithQuit(): 
 print(yellow + '''
(Press a number and then Enter to choose. '''+reset+red+'''Press 0 to '''+reset+Red+'''quit.'''+reset+yellow+''')'''+reset)
def InvalidInput():
 clearScreen()
 print(Red + "Invalid Input" + reset)
 time.sleep(1)
 print('''You must press the number on the left.
Then, you press enter to choose.''')
 PETC_function()
def YesOrNo():
 time.sleep(0.5)
 print('''
1 - '''+Blue+'''Yes'''+reset)
 time.sleep(0.25)
 print('''
2 - '''+Red+'''No'''+reset)
 time.sleep(0.25)
 PNTC_function()
def level6_function():
 You = 0
 Youlives = 2
 Raphael = 0
 Raphaellives = 2
 Mike = 0
 Mikelives = 2
 Jalen = 0
 Jalenlives = 2
 Miguel = 0
 Miguellives = 2
 PlayersOut = 0
 Colorselection = ["",Red+"RED"+reset,green+"GREEN"+reset,yellow+"YELLOW"+reset,Blue+"BLUE"+reset]
 Colors = ["","RED","GREEN","YELLOW","BLUE"]
 while True:
  print('''
Choose your difficulty for Four Corners:''')
  time.sleep(0.5)
  print('''
1 - ''' + Blue + '''Easy (Atleast three winners)''' + reset)
  time.sleep(0.25)
  print('''
2 - ''' + yellow + '''Medium (Atleast two winners)''' + reset)
  time.sleep(0.25)
  print('''
3 - ''' + Red + '''Hard (Atleast one winner)''' + reset)
  time.sleep(0.25)
  PNTC_function()
  try:
   DifficultyChoice = int(input(""))
  except:
   InvalidInput()
   continue
  if DifficultyChoice == 1:
     print("Alright! Easy difficulty of Four Corners loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 2:
     print("Alright! Medium difficulty Four Corners loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 3:
     print("Alright! Hard difficulty Four Corners loading!")
     time.sleep(1.5)
     clearScreen()
     break
  else:
    clearScreen()
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
   print('''1 - A random color is chosen by the system''') 
   PETC_function()
   print('''2 - There is a list of four colors that will be randomly chosen''')
   PETC_function()
   print('''3 - Those colors are red, green, yellow, and blue.''')
   PETC_function()
   print('''4 - You will also choose the color that you want to pick''')
   PETC_function()
   print('''5 - You have 3 lives in this game.''')
   PETC_function()
   print('''6 - If the color that you choose gets picked, you lose a life
Once you run out of lives, you lose''')
   PETC_function()
   print('''7 - Only a certain amount of players can win.
This depends on difficulty.''')
   PETC_function()
   Explained = True
   continue
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   InvalidInput()
 while True:
  FourColors = random.randrange(1,5)
  Raphael = random.randrange(1,5)
  Mike = random.randrange(1,5)
  Jalen = random.randrange(1,5)
  Miguel = random.randrange(1,5)
  try:
   print('''Pick your color.''')
   time.sleep(0.5)
   for x in range(1,5):
    print('''
{0} - {1}'''.format(x,Colorselection[x]))
    time.sleep(0.25)
   NumChoiceWithQuit()
   You = int(input(""))
   clearScreen()
  except:
   InvalidInput()
   continue
  Quitchoice = 0
  while You == 0:
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
  if Quitchoice == 2:
   continue
  if You > 4 or You < 1:
   clearScreen()
   print(Red + "That is not an option" + reset)
   time.sleep(1)
   InvalidInput()
   continue
  print("The color chosen is......")
  time.sleep(0.5)
  if FourColors == 1:
   print(Red+"RED!"+reset)
  elif FourColors == 2:
   print(green+"GREEN!"+reset)
  elif FourColors == 3:
   print(yellow+"YELLOW!"+reset)
  elif FourColors == 4:
   print(Blue+"BLUE!"+reset) 
  time.sleep(0.5)
  if Raphaellives > 0:
   if Raphael != FourColors:
    Raphaellivesleft = Blue+"Raphael chose {}, so Raphael is safe"+reset
    print(Raphaellivesleft.format(Colors[Raphael],Raphaellives))
   elif Raphael == FourColors:
    Raphaellives = Raphaellives - 1
    Raphaellivesleft = Red+"Raphael chose {}, so Raphael has {} live(s) left"+reset  
    print(Raphaellivesleft.format(Colors[Raphael],Raphaellives))
   if Raphaellives == 0:
     print(Red+"RAPHAEL IS OUT"+reset)
     PlayersOut = PlayersOut + 1
  if Mikelives > 0:
   time.sleep(0.25)
   if Mike != FourColors:
    Mikelivesleft = Blue+"Mike chose {}, so Mike is safe"+reset
    print(Mikelivesleft.format(Colors[Mike],Mikelives))
   elif Mike == FourColors:
    Mikelives = Mikelives - 1
    Mikelivesleft = Red+"Mike chose {}, so Mike has {} live(s) left"+reset 
    print(Mikelivesleft.format(Colors[Mike],Mikelives))
    if Mikelives == 0:
     print(Red+"MIKE IS OUT"+reset)
     PlayersOut = PlayersOut + 1
  if Youlives > 0:
   time.sleep(0.25)
   if You != FourColors:
    Yourlivesleft = green+"You "+reset+Blue+"chose {}, so "+reset+green+"you "+reset+Blue+"are safe"+reset
    print(Yourlivesleft.format(Colors[You]))
   elif You == FourColors:
    Youlives = Youlives - 1
    Yourlivesleft = green+"You "+reset+Red+"chose {}, so "+reset+green+"You "+reset+Red+ "have {} live(s) left"+reset  
    print(Yourlivesleft.format(Colors[You],Youlives))
    if Youlives == 0:
     print(Red+"YOU ARE OUT"+reset)
  if Miguellives > 0:
   time.sleep(0.25)
   if Miguel != FourColors:
    Miguellivesleft = Blue+"Miguel chose {}, so Miguel is safe"+reset
    print(Miguellivesleft.format(Colors[Miguel]))
   elif Miguel == FourColors:
    Miguellives = Miguellives - 1
    Miguellivesleft = Red+"Miguel chose {}, so Miguel has {} live(s) left"+reset  
    print(Miguellivesleft.format(Colors[Miguel],Miguellives))
    if Miguellives == 0:
     print(Red+"MIGUEL IS OUT"+reset)
     PlayersOut = PlayersOut + 1
  time.sleep(0.25)
  if Jalenlives > 0:
   if Jalen != FourColors:
    Jalenlivesleft = Blue+"Jalen chose {}, so Jalen is safe"+reset
    print(Jalenlivesleft.format(Colors[Jalen]))
   elif Jalen == FourColors:
    Jalenlives = Jalenlives - 1
    Jalenlivesleft = Red+"Jalen chose {}, so Jalen has {} live(s) left"+reset  
    print(Jalenlivesleft.format(Colors[Jalen],Jalenlives))
    if Jalenlives == 0:
     print(Red+"JALEN IS OUT"+reset)
     PlayersOut = PlayersOut + 1
  PETC_function()
  if PlayersOut >= 2 and DifficultyChoice == 1: 
    print(Blue+"YOU WON A GAME OF FOUR CORNERS ON EASY DIFFICULTY!"+reset)
    PETC_function()
    return "EW"
  elif Youlives == 0 and PlayersOut < 2 and DifficultyChoice == 1: 
    print(Red+"You lost a game of Four Corners on easy difficulty."+reset)
    PETC_function()
    return "EL"
  elif PlayersOut >= 3 and DifficultyChoice == 2: 
    print(Blue+"YOU WON A GAME OF FOUR CORNERS ON MEDIUM DIFFICULTY!"+reset)
    PETC_function()
    return "MW"
  elif Youlives == 0 and PlayersOut < 3 and DifficultyChoice == 2: 
    print(Red+"You lost a game of Four Corners on medium difficulty."+reset)
    PETC_function()
    return "ML"
  elif PlayersOut >=  4 and DifficultyChoice == 3: 
    print(Blue+"YOU WON A GAME OF FOUR CORNERS ON HARD DIFFICULTY!"+reset)
    PETC_function()
    return "HW"
  elif Youlives == 0 and PlayersOut < 4 and DifficultyChoice == 3: 
    print(Red+"You lost a game of Four Corners on hard difficulty."+reset)
    PETC_function()
    return "HL"

#Level 6 - Four Corners

def pvplevel6_function(OnePlayerName,TwoPlayerName):
 Youlives = 2
 TwoPlrlives = 2
 Mikelives = 2
 Jalenlives = 2
 Miguellives = 2
 Colorselection = ["",Red+"RED"+reset,green+"GREEN"+reset,yellow+"YELLOW"+reset,Blue+"BLUE"+reset]
 Colors = ["","RED","GREEN","YELLOW","BLUE"]
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
   print('''1 - A random color is chosen by the system''') 
   PETC_function()
   print('''2 - There is a list of four colors that will be randomly chosen''')
   PETC_function()
   print('''3 - Those colors are red, green, yellow, and blue.''')
   PETC_function()
   print('''4 - You will also choose the color that you want to pick''')
   PETC_function()
   print('''5 - You have 3 lives in this game.''')
   PETC_function()
   print('''6 - If the color that you choose gets picked, you lose a life
Once you run out of lives, you lose''')
   PETC_function()
   print('''7 - Only a certain amount of players can win.
This depends on difficulty.''')
   PETC_function()
   Explained = True
   continue
  if Explanationchoice == 2:
   print("Alright, GOOD LUCK!")
   time.sleep(1.5)
   clearScreen()
   break
  else:
   InvalidInput()
 while True:
  FourColors = random.randrange(1,5)
  Mike = random.randrange(1,5)
  Jalen = random.randrange(1,5)
  Miguel = random.randrange(1,5)
  try:
   clearScreen()
   print('''{}! Choose your color.'''.format(OnePlayerName))
   time.sleep(0.5)
   for x in range(1,5):
    print('''
{0} - {1}'''.format(x,Colorselection[x]))
    time.sleep(0.25)
   NumChoiceWithQuit()
   You = int(input(""))
  except:
   InvalidInput()
   continue
  Quitchoice = 0
  while You == 0:
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
  if Quitchoice == 2:
   continue
  if You > 4 or You < 1:
   InvalidInput()
   continue
  while True:
   try:
    clearScreen()
    print('''{0} chose {1}.
'''.format(OnePlayerName,Colors[You]))
    time.sleep(1)
    print('''{}! Choose your color.'''.format(TwoPlayerName))
    time.sleep(0.5)
    for x in range(1,5):
     print('''
{0} - {1}'''.format(x,Colorselection[x]))
     time.sleep(0.25)
    NumChoiceWithQuit()
    TwoPlr = int(input(""))
    clearScreen()
   except:
    InvalidInput()
    continue
   Quitchoice = 0
   while TwoPlr == 0:
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
   if Quitchoice == 2:
    continue
   if TwoPlr > 4 or TwoPlr < 1:
    InvalidInput()
    continue
   elif TwoPlr != 0:
    break
  print("The color chosen is......")
  time.sleep(0.5)
  if FourColors == 1:
   print(Red+"RED!"+reset)
  elif FourColors == 2:
   print(green+"GREEN!"+reset)
  elif FourColors == 3:
   print(yellow+"YELLOW!"+reset)
  elif FourColors == 4:
   print(Blue+"BLUE!"+reset) 
  time.sleep(0.5)
  if Youlives > 0:
   time.sleep(0.25)
   if You != FourColors:
    Yourlivesleft = "{1} "+reset+Blue+"chose {0}, so "+reset+"{1} "+reset+Blue+"is safe"+reset
    print(Yourlivesleft.format(Colors[You],OnePlayerName))
   elif You == FourColors:
    Youlives = Youlives - 1
    Yourlivesleft = "{1} "+Red+"chose {0}, so "+reset+"{1} "+Red+"has {2} live(s) left"+reset   
    print(Yourlivesleft.format(Colors[You],OnePlayerName,Youlives))
    if Youlives == 0:
     Yourlivesleft = "{} "+Red+"IS OUT"+reset
     print(Yourlivesleft.format(OnePlayerName))
  if Mikelives > 0:
   time.sleep(0.25)
   if Mike != FourColors:
    Mikelivesleft = Blue+"Mike chose {}, so Mike is safe"+reset
    print(Mikelivesleft.format(Colors[Mike],Mikelives))
   elif Mike == FourColors:
    Mikelives = Mikelives - 1
    Mikelivesleft = Red+"Mike chose {}, so Mike has {} live(s) left"+reset 
    print(Mikelivesleft.format(Colors[Mike],Mikelives))
    if Mikelives == 0:
     print(Red+"MIKE IS OUT"+reset)
  if TwoPlrlives > 0:
   time.sleep(0.25)
   if TwoPlr != FourColors:
    TwoPlrlivesleft = "{1} "+Blue+"chose {0}, so "+reset+"{1} "+Blue+"is safe"+reset
    print(TwoPlrlivesleft.format(Colors[TwoPlr],TwoPlayerName))
   elif TwoPlr == FourColors:
    TwoPlrlives = TwoPlrlives - 1
    TwoPlrlivesleft = "{1} "+Red+"chose {0}, so "+reset+"{1} "+Red+"has {2} live(s) left"+reset  
    print(TwoPlrlivesleft.format(Colors[TwoPlr],TwoPlayerName,TwoPlrlives))
    if TwoPlrlives == 0:
     TwoPlrlivesleft = "{} "+Red+"IS OUT"+reset
     print(TwoPlrlivesleft.format(TwoPlayerName))
  if Miguellives > 0:
   time.sleep(0.25)
   if Miguel != FourColors:
    Miguellivesleft = Blue+"Miguel chose {}, so Miguel is safe"+reset
    print(Miguellivesleft.format(Colors[Miguel]))
   elif Miguel == FourColors:
    Miguellives = Miguellives - 1
    Miguellivesleft = Red+"Miguel chose {}, so Miguel has {} live(s) left"+reset  
    print(Miguellivesleft.format(Colors[Miguel],Miguellives))
    if Miguellives == 0:
     print(Red+"MIGUEL IS OUT"+reset)
  time.sleep(0.25)
  if Jalenlives > 0:
   if Jalen != FourColors:
    Jalenlivesleft = Blue+"Jalen chose {}, so Jalen is safe"+reset
    print(Jalenlivesleft.format(Colors[Jalen]))
   elif Jalen == FourColors:
    Jalenlives = Jalenlives - 1
    Jalenlivesleft = Red+"Jalen chose {}, so Jalen has {} live(s) left"+reset  
    print(Jalenlivesleft.format(Colors[Jalen],Jalenlives))
    if Jalenlives == 0:
     print(Red+"JALEN IS OUT"+reset)
  PETC_function()
  if Youlives > 0 and TwoPlrlives == 0:
   print("{0} has lasted longer than {1} in Four Corners!".format(OnePlayerName,TwoPlayerName))
   PETC_function()
   return "W"
  elif Youlives == 0 and TwoPlrlives > 0:
   print("{0} has lasted longer than {1} in Four Corners!".format(TwoPlayerName,OnePlayerName))
   PETC_function()
   return "L"
  elif Youlives == 0 and TwoPlrlives == 0:
   print("{0} and {1} has both been eliminated, so the game will now reset.".format(TwoPlayerName,OnePlayerName))
   PETC_function() 
   Youlives = 2
   TwoPlrlives = 2
   Mikelives = 2
   Jalenlives = 2
   Miguellives = 2
#Level 6 - Four Corners