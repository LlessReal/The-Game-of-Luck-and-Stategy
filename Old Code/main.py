import random
import time
import level4
import level6
import level7
import level8
import level9
import level10
from os import system as sys
from os import name as osname
YFSPrintNumbers = 0
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
cyan_back = "\033[0;46m"
pink_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
red_back = "\033[0;41m"
grey_back = "\033[0;40m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
bold = "\033[4m"
reset = "\033[0m"
Scoreboard = '''Progess of Session:

{0} - {1} win(s).

{2} - {3} win(s).'''
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
def BeginningScreen():
  OnePlrPts = 0
  TwoPlrPts = 0
  clearScreen()
  print(Blue + '''WELCOME''' + reset)
  Text = "TO THE GAME OF LUCK AND STRATEGY!"
  TextInt = 0
  time.sleep(1)
  while TextInt <= 40:
      clearScreen()
      print(Blue + '''WELCOME''' + reset)
      TextInt = TextInt + 1
      print(Text[0:TextInt])
      time.sleep(0.1)
  while True:
      try:
          print('''Would you like to ''' + Blue + '''PLAY?''' + reset)
          time.sleep(0.75)
          print('''
1 - ''' + Blue + '''YES ''' + reset + '''I WANT TO ''' + Blue + '''PLAY!''' +
                reset)
          time.sleep(0.25)
          print('''
2 - ''' + Red + '''No''' + reset)
          time.sleep(0.25)
          print('''
3 - What even is this game?''')
          time.sleep(0.25)
          PNTC_function()
          BeginningDecision = int(input(""))
      except:
          II_function()
          continue
      if BeginningDecision == 1:
          Saying = random.randrange(0, 5)
          if Saying == 0:
              print("Yeah you better say yes")
          elif Saying == 1:
              print("Let's get this show on the road then!")
          elif Saying == 2:
              print("Alright! Let's do this!")
          elif Saying == 3:
              print("Time to play!")
          elif Saying == 4:
              print("We have a new challenger!")
          time.sleep(1)
          clearScreen()
          break
      elif BeginningDecision == 2:
          exit()
      elif BeginningDecision == 3:
          clearScreen()
          print('''Once again, it is the game of luck and strategy,
so you win THROUGH luck and strategy.''')
          PETC_function()
          print('''It is not just one game we are talking here. It is multiple.''')
          PETC_function()
          print('''These games are such as Tic-Tac-Toe, 
Rock Paper Scissors, 
and Four Corners.''')
          PETC_function()
          print('''You will most likely be prompted to type in a certain number in the games.
This is in order for you to make a move on that game.
For example, 
You must type in 1 in order to fill the top-left spot on Tic Tac Toe''')
          PETC_function()
          print('''There are two modes to this game:
"Player vs Computer" and "Player vs Player"''')
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
          continue
      else:
          II_function()
          continue
  ModeSelection = True
  while ModeSelection == True:
      try:
          print('''Choose your mode.''')
          time.sleep(0.5)
          print('''
1 - Player VS Computer''')
          time.sleep(0.25)
          print('''
2 - Player VS Player ''')
          time.sleep(0.25)
          PNTC_function()
          ModeChoice = int(input(""))
      except:
          II_function()
          continue
      if ModeChoice == 1:
          while True:
              clearScreen()
              print("Mode Selected: " + yellow + "Player VS Computer" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  ModeConfirmation = int(input(""))
                  clearScreen()
              except:
                  II_function()
                  continue
              if ModeConfirmation == 1:
                  print("Alright! Player VS Computer mode loading!")
                  time.sleep(1)
                  print('''
My bot is armed and ready for you''')
                  time.sleep(1.5)
                  clearScreen()
                  ModeSelection = False
                  break
              elif ModeConfirmation == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
      elif ModeChoice == 2:
          while True:
              clearScreen()
              print("Mode selected: " + yellow + "Player VS Player" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  ModeConfirmation = int(input(""))
              except:
                  II_function()
                  continue
              if ModeConfirmation == 1:
                  print("Alright! Player VS Player mode loading!")
                  time.sleep(1.5)
                  print('''
May the luckiest and smartest win!''')
                  time.sleep(1.5)
                  clearScreen()
                  ModeSelection = False
                  break
              elif ModeConfirmation == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
      else:
          II_function()
          continue
  if ModeChoice == 1:
      print('''Gain as many points as you can in 5 games!
You can win some and you can lose some.''')
      PETC_function()
      GamesLeft = 5
      GamesRemaining = '''
You get to play {} more game(s)'''
      while GamesLeft != 0:
          print('''
Choose your game.''')
          time.sleep(0.5)
          print('''
1 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
2 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
3 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
4 - Rock Paper Scissors '''+Blue+'''[300 points]'''+reset)
          time.sleep(0.1)
          print('''
5 - Gold Fish ''' + yellow + '''[UNDER CONSTRUCTION]''' + reset)
          time.sleep(0.1)
          print('''
6 - Four Corners '''+Blue+'''[100 - 500 points]'''+reset)
          time.sleep(0.1)
          print('''
7 - Guess the number '''+Blue+'''[300 points]'''+reset)
          time.sleep(0.1)
          print('''
8 - Board Game '''+Blue+'''[100 - 500 points]'''+reset)
          time.sleep(0.1)
          print('''
9 - Tic-Tac-Toe '''+Blue+'''[100 - 300 points]'''+reset)
          time.sleep(0.1)
          print('''
10 - Connect FOUR '''+Blue+'''[100 - 400 points]'''+reset)
          time.sleep(0.1)
          PNTCOQ_function()
          try:
              GameChoice = int(input(""))
              clearScreen()
          except:
              II_function()
              continue
          Quitchoice = 0
          while GameChoice == 0:
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
             return BeginningScreen()
            if Quitchoice == 2:
             print('''
Alrighty then!''')
             time.sleep(1)
             break
          if Quitchoice == 2:
            continue
          if GameChoice == 1:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
          elif GameChoice == 2:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
          elif GameChoice == 3:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
          elif GameChoice == 4:
              while True:
                  clearScreen()
                  print("Game selected: " + yellow + "Rock Paper Scissors" +reset)
                  time.sleep(0.5)
                  print('''
Continue?''')
                  YOR_function()
                  try:
                      GameChoice = int(input(""))
                  except:
                      clearScreen()
                      II_function()
                      continue
                  if GameChoice == 1:
                      print("Alright! Rock Paper Scissors loading!")
                      time.sleep(1.5)
                      clearScreen()
                      GameInSession = level4.level4_function()
                      clearScreen()
                      if GameInSession == "W":
                       OnePlrPts = OnePlrPts + 300
                       GameResults = Blue+'''Congratulations on your win in Rock Paper Scissors.
      
You gained 300 points so you have {} points in total now.'''+reset
                      elif GameInSession == "L":
                       OnePlrPts = OnePlrPts - 150
                       GameResults = Red+'''It looks like you lost a game of Rock Paper Scissors.
      
You lost 150 points so you have {} points in total now.'''+reset
                      elif GameInSession == "Quit":
                       return BeginningScreen()
                      print(GameResults.format(OnePlrPts))
                      PETC_function()
                      GamesLeft = GamesLeft - 1
                      print(GamesRemaining.format(GamesLeft))
                      PETC_function()
                      break
                  elif GameChoice == 2:
                      print("Understood.")
                      time.sleep(1)
                      clearScreen()
                      break
              else:
                  II_function()
                  continue
          elif GameChoice == 5:
              print(Red + '''Gold Fish is under construction at the moment.''' + reset)
              PETC_function()
          elif GameChoice == 6:
            while True:
              clearScreen()
              print("Game selected: " + yellow + "Four Corners" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Four Corners loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level6.level6_function()
                  clearScreen()
                  if GameInSession == "EW":
                   OnePlrPts = OnePlrPts + 100
                   GameResults = Blue+'''Congratulations on your win in Four Corners (Easy Difficulty)
  
You gained 100 points so you have {} points in total now.'''+reset
                  elif GameInSession == "MW":
                   OnePlrPts = OnePlrPts + 300
                   GameResults = Blue+'''Congratulations on your win in Four Corners (Medium Difficulty)
  
You gained 300 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HW":
                   OnePlrPts = OnePlrPts + 500
                   GameResults = Blue+'''Congratulations on your win in Four Corners (Hard Difficulty)
  
You gained 500 points so you have {} points in total now.'''+reset
                  elif GameInSession == "EL":
                   OnePlrPts = OnePlrPts - 50
                   GameResults = Red+'''It looks like you lost a game of Four Corners (Easy Difficulty)
  
You lost 50 points so you have {} points in total now.'''+reset
                  elif GameInSession == "ML":
                   OnePlrPts = OnePlrPts - 150
                   GameResults = Red+'''It looks like you lost a game of Four Corners (Medium Difficulty)
  
You lost 150 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HL":
                   OnePlrPts = OnePlrPts - 250
                   GameResults = Red+'''It looks like you lost a game of Four Corners (Hard Difficulty)
  
You lost 250 points so you have {} points in total now.'''+reset
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  print(GameResults.format(OnePlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 7:
            while True:
              clearScreen()
              print("Game selected: " + yellow + "Guess the number" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Guess the number loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level7.level7_function()
                  clearScreen()
                  if GameInSession == "W":
                   OnePlrPts = OnePlrPts + 300
                   GameResults = Blue+'''Congratulations on your win in Guess the Number
  
You gained 300 points so you have {} points in total now.'''+reset
                  elif GameInSession == "L":
                   OnePlrPts = OnePlrPts - 150
                   GameResults = Red+'''It looks like you lost a game of Guess the Number.
  
You lost 150 points so you have {} points in total now.'''+reset
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  print(GameResults.format(OnePlrPts))
                  PETC_function()
                  clearScreen()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 8:
           while True:
              clearScreen()
              print("Game selected: " + yellow + "Board Game" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Board Game loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level8.level8_function()
                  clearScreen()
                  if GameInSession == "EW":
                   OnePlrPts = OnePlrPts + 100
                   GameResults = Blue+'''Congratulations on your win in Board Game (Easy Difficulty)
  
You gained 100 points so you have {} points in total now.'''+reset
                  elif GameInSession == "MW":
                   OnePlrPts = OnePlrPts + 300
                   GameResults = Blue+'''Congratulations on your win in Board Game (Medium Difficulty)
  
You gained 300 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HW":
                   OnePlrPts = OnePlrPts + 500
                   GameResults = Blue+'''Congratulations on your win in Board Game (Hard Difficulty)
  
You gained 500 points so you have {} points in total now.'''+reset
                  elif GameInSession == "EL":
                   OnePlrPts = OnePlrPts - 50
                   GameResults = Red+'''It looks like you lost a game of Board Game (Easy Difficulty)
  
You lost 50 points so you have {} points in total now.'''+reset
                  elif GameInSession == "ML":
                   OnePlrPts = OnePlrPts - 150
                   GameResults = Red+'''It looks like you lost a game of Board Game (Medium Difficulty)
  
You lost 150 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HL":
                   OnePlrPts = OnePlrPts - 250
                   GameResults = Red+'''It looks like you lost a game of Board Game (Hard Difficulty)
  
You lost 250 points so you have {} points in total now.'''+reset
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  print(GameResults.format(OnePlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 9:
            while True:
              clearScreen()
              print("Game selected: " + yellow + "Tic-Tac-Toe" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Tic-Tac-Toe loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level9.level9_function()
                  clearScreen()
                  if GameInSession == "EW":
                   OnePlrPts = OnePlrPts + 100
                   GameResults = Blue+'''Congratulations on your win in Tic Tac Toe (Easy Difficulty)
  
You gained 100 points so you have {} points in total now.'''+reset
                  if GameInSession == "MW":
                   OnePlrPts = OnePlrPts + 200
                   GameResults = Blue+'''Congratulations on your win in Tic Tac Toe (Medium Difficulty)
  
You gained 200 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HW":
                   OnePlrPts = OnePlrPts + 300
                   GameResults = Blue+'''Congratulations on your win in Tic Tac Toe (Hard Difficulty)
  
You gained 300 points so you have {} points in total now.'''+reset
                  elif GameInSession == "EL":
                   OnePlrPts = OnePlrPts - 50
                   GameResults = Red+'''It looks like you lost a game of Tic Tac Toe (Easy Difficulty)
  
You lost 50 points so you have {} points in total now.'''+reset
                  elif GameInSession == "ML":
                   OnePlrPts = OnePlrPts - 100
                   GameResults = Red+'''It looks like you lost a game of Tic Tac Toe (Medium Difficulty)
  
You lost 100 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HL":
                   OnePlrPts = OnePlrPts - 150
                   GameResults = Red+'''It looks like you lost a game of Tic Tac Toe (Hard Difficulty)
  
You lost 150 points so you have {} points in total now.'''+reset
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  print(GameResults.format(OnePlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 10:
           while True:
              clearScreen()
              print("Game selected: " + yellow + "Connect Four" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Connect Four loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level10.level10_function()
                  clearScreen()
                  if GameInSession == "EW":
                   OnePlrPts = OnePlrPts + 100
                   GameResults = Blue+'''Congratulations on your win in Connect Four (Easy Difficulty)
  
You gained 100 points so you have {} points in total now.'''+reset
                  elif GameInSession == "MW":
                   OnePlrPts = OnePlrPts + 250
                   GameResults = Blue+'''Congratulations on your win in Connect Four (Medium Difficulty)
  
You gained 250 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HW":
                   OnePlrPts = OnePlrPts + 400
                   GameResults = Blue+'''Congratulations on your win in Connect Four (Hard Difficulty)
  
You gained 400 points so you have {} points in total now.'''+reset
                  elif GameInSession == "EL":
                   OnePlrPts = OnePlrPts - 50
                   GameResults = Red+'''It looks like you lost a game of Connect Four (Normal Difficulty)
  
You lost 50 points so you have {} points in total now.'''+reset
                  elif GameInSession == "ML":
                   OnePlrPts = OnePlrPts - 125
                   GameResults = Red+'''It looks like you lost a game of Connect Four (Medium Difficulty)
  
You lost 125 points so you have {} points in total now.'''+reset
                  elif GameInSession == "HL":
                   OnePlrPts = OnePlrPts - 200
                   GameResults = Red+'''It looks like you lost a game of Connect Four (Hard Difficulty)
  
You lost 200 points so you have {} points in total now.'''+reset
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  print(GameResults.format(OnePlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          else:
           II_function()
           continue
      print(Blue+'''You have finished your trial of 7 games!''' + reset)
      PETC_function()
      print("Your final score is")
      time.sleep(0.25)
      clearScreen()
      print("Your final score is.")
      time.sleep(0.25)
      clearScreen()
      print("Your final score is..")
      time.sleep(0.25)
      clearScreen()
      print("Your final score is...")
      time.sleep(0.25)
      clearScreen()
      print("Your final score is....")
      time.sleep(0.25)
      clearScreen()
      print("Your final score is.....")
      time.sleep(0.25)
      if OnePlrPts <= 0:
       Yourfinalscore =  Red + str(OnePlrPts) + reset + "."
       Messagechoice = random.randrange(0,7)
       print(Yourfinalscore)
       time.sleep(1)
       if Messagechoice == 1:
        print("Well, that's dissappointing.")
       elif Messagechoice == 2:
        print(Red+"I guess you're pretty unlucky huh."+reset)
       elif Messagechoice == 3:
        print(Red+"Oof, maybe you'll be luckier next time."+reset)
       elif Messagechoice == 4:
        print(Red+"Well, that wasn't impressive."+reset)
       elif Messagechoice == 5:
        print(Red+"WOW! That was Sh!%."+reset)
       elif Messagechoice == 6:
        print(Red+"Gosh you made me so mad it's unreal."+reset)
       time.sleep(1)
      elif OnePlrPts > 0 and OnePlrPts < 500:
       Yourfinalscore = str(OnePlrPts) + reset + "."
       print(Yourfinalscore)
       time.sleep(1)
       if OnePlrPts >= 500 and OnePlrPts < 1000:
        Yourfinalscore =  Blue + str(OnePlrPts) + reset + "!"
        print(Yourfinalscore)
        print("Not bad challenger!")
        time.sleep(1)
       elif OnePlrPts >= 1000 and OnePlrPts < 2000:
        Yourfinalscore =  Blue + str(OnePlrPts) + reset + "!"
        print(Yourfinalscore)
        print("You did great challenger!!")
        time.sleep(1)
       elif OnePlrPts >= 2000 and OnePlrPts < 3000:
        Yourfinalscore =  Blue + str(OnePlrPts) + reset + "!"
        print(Yourfinalscore)
        print("You're crazy challenger! Well done!")
        time.sleep(1)
       elif OnePlrPts >= 3000:
        Yourfinalscore =  Blue + str(OnePlrPts) + reset + "!"
        print(Yourfinalscore)
        time.sleep(1)
        print('''Woah! That's a very big score!''')
        time.sleep(1)
        print('''
You're not a challenger anymore...''')
        time.sleep(1)
        print('''
You're a '''+blue_back+'''GOD!'''+reset)
        time.sleep(1)
       print('''
Feel free to share your score with your friends!''')
      PETC_function()
      return BeginningScreen()
  elif ModeChoice == 2:
      OPNSelection = True
      while OPNSelection == True:
          OnePlayerName = str(
              input('''Player 1! Type in your name.
'''+yellow+
'''(Name must contain atleast one letter and be no longer than 10 characters.)
'''+reset))
          if len(OnePlayerName) != 0 and len(OnePlayerName) <= 10 and OnePlayerName.isdigit() == False:
              while True:
                  clearScreen()
                  OPNSelected = "Player 1 name selected: {}"
                  print(OPNSelected.format(OnePlayerName))
                  time.sleep(1)
                  print('''
Confirm?''')
                  YOR_function()
                  try:
                      OPNConfirmation = int(input(""))
                  except:
                      II_function()
                      continue
                  if OPNConfirmation == 1:
                      print("Great!")
                      time.sleep(1)
                      OPNNoCopy = OnePlayerName
                      OnePlayerName = green + OnePlayerName + reset
                      OPNName = '''
Player 1 Name: {}'''
                      print(OPNName.format(OnePlayerName))
                      time.sleep(1.5)
                      clearScreen()
                      OPNSelection = False
                      break
                  elif OPNConfirmation == 2:
                      print("Understood.")
                      time.sleep(1)
                      clearScreen()
                      break
                  else:
                      II_function()
          else: 
           clearScreen()
           print(Red + "Invalid Input" + reset)
           time.sleep(1)
           print('''(Name must contain atleast one letter and be no longer than 10 characters.)
(Your name also cannot be the same as Player 1's name''')
           PETC_function()
      TPNSelection = True
      while TPNSelection == True:
              TwoPlayerName = str(
                  input('''Player 2! Type in your name.
''' + yellow + '''(Name must contain atleast one letter and be no longer than 10 characters.)
(Your name also cannot be the same as Player 1's name) 
''' + reset))
              if len(TwoPlayerName) != 0 and len(TwoPlayerName) <= 10 and TwoPlayerName.isdigit() == False and TwoPlayerName != OPNNoCopy:
                  while True:
                      clearScreen()
                      TPNSelected = "Player 2 name selected: {}"
                      print(TPNSelected.format(TwoPlayerName))
                      time.sleep(1)
                      print('''
Confirm?''')
                      YOR_function()
                      try:
                       TPNConfirmation = int(input(""))
                      except:
                       II_function()
                       continue
                      if TPNConfirmation == 1:
                       print("Great!")
                       time.sleep(1)
                       TwoPlayerName = red + TwoPlayerName + reset
                       TPNName = '''
Player 2 Name: {}'''
                       print(TPNName.format(TwoPlayerName))
                       time.sleep(1.5)
                       clearScreen()
                       TPNSelection = False
                       break
                      elif TPNConfirmation == 2:
                       print("Understood.")
                       time.sleep(1)
                       clearScreen()
                       break
                      else:
                       II_function()
                       continue
              else:
                  clearScreen()
                  print(Red + "Invalid Input" + reset)
                  time.sleep(1)
                  print('''(Name must contain atleast one letter and be no longer than 10 characters.)
(Your name also cannot be the same as Player 1's name)''')
                  PETC_function()
  if ModeChoice == 2:
      print('''Win as many games as you can!
Whichever opponent reaches 3 wins in the games first will win the game of luck and stategy!''')
      PETC_function()
      GamesLeft = 5
      GamesRemaining = '''
You and your opponent get to play {} more game(s)'''
      while GamesLeft != 0  and OnePlrPts != 3 and TwoPlrPts != 3:
          print('''
Choose your game.''')
          time.sleep(0.5)
          print('''
1 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
2 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
3 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
4 - ''' + yellow + '''[TBA]''' + reset)
          time.sleep(0.1)
          print('''
5 - Gold Fish ''' + yellow + '''[UNDER CONSTRUCTION]''' + reset)
          time.sleep(0.1)
          print('''
6 - Four Corners ''')
          time.sleep(0.1)
          print('''
7 - Guess the number ''')
          time.sleep(0.1)
          print('''
8 - Board Game ''' + yellow + '''[UNDER CONSTRUCTION]''' + reset)
          time.sleep(0.1)
          print('''
9 - Tic-Tac-Toe ''')
          time.sleep(0.1)
          print('''
10 - Connect FOUR ''')
          time.sleep(0.1)
          PNTCOQ_function()
          try:
              GameChoice = int(input(""))
              clearScreen()
          except:
              II_function()
              continue
          Quitchoice = 0
          while GameChoice == 0:
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
             return BeginningScreen()
            if Quitchoice == 2:
             print('''
Alrighty then!''')
             time.sleep(1)
             break
          if Quitchoice == 2:
            continue
          if GameChoice == 1:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
              continue
          elif GameChoice == 2:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
              continue
          elif GameChoice == 3:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
              continue
          elif GameChoice == 4:
              print(Red + '''This game is not announced''' + reset)
              PETC_function()
              continue
              while True:
                  clearScreen()
                  print("Game selected: " + yellow + "TBA" +reset)
                  time.sleep(0.5)
                  print('''
Continue?''')
                  YOR_function()
                  try:
                      GameChoice = int(input(""))
                  except:
                      clearScreen()
                      II_function()
                      continue
                  if GameChoice == 1:
                      print("Alright! TBA loading!")
                      time.sleep(1.5)
                      clearScreen()
                      GameInSession = level4.pvplevel4_function(OnePlayerName,TwoPlayerName)
                      clearScreen()
                      if GameInSession == "W":
                       GameResults = green+'''{} has won the game of TBA!'''+reset
                       print(GameResults.format(OnePlayerName))
                       OnePlrPts = OnePlrPts + 1
                      elif GameInSession == "L":
                       GameResults = red+'''{} has won the game of TBA!'''+reset
                       print(GameResults.format(TwoPlayerName))
                       TwoPlrPts = TwoPlrPts + 1
                      elif GameInSession == "Quit":
                       return BeginningScreen()
                      PETC_function()
                      print(Scoreboard.format(OnePlayerName,OnePlrPts,TwoPlayerName,TwoPlrPts))
                      PETC_function()
                      GamesLeft = GamesLeft - 1
                      print(GamesRemaining.format(GamesLeft))
                      PETC_function()
                      break
                  elif GameChoice == 2:
                      print("Understood.")
                      time.sleep(1)
                      clearScreen()
                      break
              else:
                  II_function()
                  continue
          elif GameChoice == 5:
              print(Red + '''Gold Fish is under construction at the moment.''' + reset)
              PETC_function()
          elif GameChoice == 6:
            while True:
              clearScreen()
              print("Game selected: " + yellow + "Four Corners" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Four Corners loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level6.pvplevel6_function(OnePlayerName,TwoPlayerName)
                  clearScreen()
                  if GameInSession == "W":
                       GameResults = green+'''{} '''+Blue+'''has won the game of Four Corners!'''+reset
                       print(GameResults.format(OnePlayerName))
                       OnePlrPts = OnePlrPts + 1
                  elif GameInSession == "L":
                       GameResults = red+'''{} '''+Blue+'''has won the game of Four Corners!'''+reset
                       print(GameResults.format(TwoPlayerName))
                       TwoPlrPts = TwoPlrPts + 1
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  PETC_function()
                  print(Scoreboard.format(OnePlayerName,OnePlrPts,TwoPlayerName,TwoPlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 7:
            while True:
              clearScreen()
              print("Game selected: " + yellow + "Guess the number" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Guess the number loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level7.pvplevel7_function(OnePlayerName,TwoPlayerName)
                  clearScreen()
                  if GameInSession == "W":
                       GameResults = green+'''{} '''+Blue+'''has won the game of Guess the Number!'''+reset
                       print(GameResults.format(OnePlayerName))
                       OnePlrPts = OnePlrPts + 1
                  elif GameInSession == "L":
                       GameResults = red+'''{} '''+Blue+'''has won the game of Guess the Number!'''+reset
                       print(GameResults.format(TwoPlayerName))
                       TwoPlrPts = TwoPlrPts + 1
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  PETC_function()
                  print(Scoreboard.format(OnePlayerName,OnePlrPts,TwoPlayerName,TwoPlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 8:
           while True:
              clearScreen()
              print(Red + '''Board Game is under construction at the moment.''' + reset)
              PETC_function()
              print("Game selected: " + yellow + "Board Game" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Board Game loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level8.pvplevel8_function(OnePlayerName,TwoPlayerName)
                  clearScreen()
                  if GameInSession == "W":
                       GameResults = green+'''{} '''+Blue+'''has won the game of Board Game!'''+reset
                       print(GameResults.format(OnePlayerName))
                       OnePlrPts = OnePlrPts + 1
                  elif GameInSession == "L":
                       GameResults = red+'''{} '''+Blue+'''has won the game of Board Game!'''+reset
                       print(GameResults.format(TwoPlayerName))
                       TwoPlrPts = TwoPlrPts + 1
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  PETC_function()
                  print(Scoreboard.format(OnePlayerName,OnePlrPts,TwoPlayerName,TwoPlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 9:
            while True:
              clearScreen()
              print("Game selected: " + yellow + "Tic-Tac-Toe" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Tic-Tac-Toe loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level9.pvplevel9_function(OnePlayerName,TwoPlayerName)
                  clearScreen()
                  if GameInSession == "W":
                       GameResults = green+'''{} '''+Blue+'''has won the game of Tic-Tac-Toe!'''+reset
                       print(GameResults.format(OnePlayerName))
                       OnePlrPts = OnePlrPts + 1
                  elif GameInSession == "L":
                       GameResults = red+'''{} '''+Blue+'''has won the game of Tic-Tac-Toe!'''+reset
                       print(GameResults.format(TwoPlayerName))
                       TwoPlrPts = TwoPlrPts + 1
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  PETC_function()
                  print(Scoreboard.format(OnePlayerName,OnePlrPts,TwoPlayerName,TwoPlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          elif GameChoice == 10:
           while True:
              clearScreen()
              print("Game selected: " + yellow + "Connect Four" + reset)
              time.sleep(0.5)
              print('''
Continue?''')
              YOR_function()
              try:
                  GameChoice = int(input(""))
              except:
                  II_function()
                  continue
              if GameChoice == 1:
                  print("Alright! Connect Four loading!")
                  time.sleep(1.5)
                  clearScreen()
                  GameInSession = level10.pvplevel10_function(OnePlayerName,TwoPlayerName)
                  clearScreen()
                  if GameInSession == "W":
                       GameResults = green+'''{} '''+Blue+'''has won the game of Connect Four!'''+reset
                       print(GameResults.format(OnePlayerName))
                       OnePlrPts = OnePlrPts + 1
                  elif GameInSession == "L":
                       GameResults = red+'''{} '''+Blue+'''has won the game of Connect Four!'''+reset
                       print(GameResults.format(TwoPlayerName))
                       TwoPlrPts = TwoPlrPts + 1
                  elif GameInSession == "Quit":
                   return BeginningScreen()
                  PETC_function()
                  print(Scoreboard.format(OnePlayerName,OnePlrPts,TwoPlayerName,TwoPlrPts))
                  PETC_function()
                  GamesLeft = GamesLeft - 1
                  print(GamesRemaining.format(GamesLeft))
                  PETC_function()
                  break
              elif GameChoice == 2:
                  print("Understood.")
                  time.sleep(1)
                  clearScreen()
                  break
              else:
                  II_function()
                  continue
          else:
           II_function()
           continue
      print("Trial of games has ended!")
      time.sleep(1)
      print(Blue+'''We have a winner!''' + reset)
      PETC_function()
      print("The winner of the trial of games of luck and strategy is")
      time.sleep(0.25)
      clearScreen()
      print("The winner of the trial of games of luck and strategy is.")
      time.sleep(0.25)
      clearScreen()
      print("The winner of the trial of games of luck and strategy is..")
      time.sleep(0.25)
      clearScreen()
      print("The winner of the trial of games of luck and strategy is...")
      time.sleep(0.25)
      clearScreen()
      print("The winner of the trial of games of luck and strategy is....")
      time.sleep(0.25)
      clearScreen()
      print("The winner of the trial of games of luck and strategy is.....")
      time.sleep(0.25)
      if OnePlrPts < TwoPlrPts:
       print("{}!".format(OnePlayerName))
       time.sleep(1)
       print('''
Congratulations {}!'''.format(OnePlayerName))
      elif TwoPlrPts < OnePlrPts:
       print("{}!".format(TwoPlayerName))
       time.sleep(1)
       print('''
Congratulations {}!'''.format(TwoPlayerName))
      PETC_function()
      return BeginningScreen()
BeginningScreen()