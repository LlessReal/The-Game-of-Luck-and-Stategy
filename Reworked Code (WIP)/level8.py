import random, time, math
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
def YORBG_function():
 time.sleep(0.5)
 print('''
1 - '''+Blue+'''Yes'''+reset)
 time.sleep(0.25)
 print('''
2 - '''+Red+'''No'''+reset)
 time.sleep(0.25)
 print('''
3 - Check Player Progress''')
 time.sleep(0.25)
 PNTC_function()
def level8_function():
 Yourrt = 50
 Jalenrt = 50
 Jeremiahrt = 50
 Krisrt = 50
 YourProtection = False
 JalenProtection = False
 JeremiahProtection = False
 KrisProtection = False
 Yourstuck = False
 Jalenstuck = False
 Jeremiahstuck = False
 Krisstuck = False
 You = 50
 Jalen = 50
 Jeremiah = 50
 Kris = 50
 PlayerListNotYou = [Jalen,Jeremiah,Kris] 
 PlayerListNotJalen = [You,Jeremiah,Kris]
 PlayerListNotJeremiah = [You,Jalen,Kris]
 PlayerListNotKris = [You,Jalen,Jeremiah]
 while True:
  print('''
Choose your difficulty for Board Game:''')
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
     print("Alright! Easy difficulty of Board Game loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 2:
     print("Alright! Medium difficulty Board Game loading!")
     time.sleep(1.5)
     clearScreen()
     break
  elif DifficultyChoice == 3:
     print("Alright! Hard difficulty Board Game loading!")
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
   print('''1 - It's a board game. 
You cross through the trail to win.''') 
   PETC_function()
   print('''2 - There are 50 tiles on the trail''')
   PETC_function()
   print('''3 - You roll an imaginary dice that I made to move
(You do this by pressing enter)''')
   PETC_function()
   print('''4 - Whenever you land on an even tile (tile 92 for example), 
You are given a chance to test your luck.
When you take the chance to test your luck,
you have a chance of getting boosts or traps.
You will be introduced to that later.''')
   PETC_function()
   print('''5 - The farther you go/the more tiles you walk through on the trail,
the higher the chances of you encountering a trap when testing luck
However, you can avoid this but not testing your luck.''')
   PETC_function()
   print('''6 - While you can play safe by not testing your luck throughout the board game,
Other players can use weapons against you when having good luck''')
   PETC_function()
   print('''7 - First player to cross through the entire trail of the board game wins!''')
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
 PlayersLeft = 4
 Youwon = False
 Jalenwon = False
 Jeremiahwon = False
 Kriswon = False
 Jalenprt = '''
1 - Jalen ({} remaining tiles)'''
 Jeremiahprt = '''
2 - Jeremiah ({} remaining tiles)'''
 Krisprt = '''
3 - Kris ({} remaining tiles)'''
 Yournrt = '''
You - {} remaining tiles'''
 Jalennrt = '''
Jalen - {} remaining tiles'''
 Jeremiahnrt = '''
Jeremiah - {} remaining tiles'''
 Krisnrt = '''
Kris - {} remaining tiles'''
 def ChsPlr_function():
  time.sleep(0.5)
  if Jalenrt > 0:
   print(Jalenprt.format(Jalenrt))
  elif Jalenrt <= 0:
   print(Blue+'''
Jalen has escaped the board!'''+reset)
  time.sleep(0.25)
  if Jeremiahrt > 0:
   print(Jeremiahprt.format(Jeremiahrt))
  elif Jeremiahrt <= 0:
   print(Blue+'''
Jeremiah has escaped the board!'''+reset)
  time.sleep(0.25)
  if Krisrt > 0:
   print(Krisprt.format(Krisrt))
  elif Krisrt <= 0:
   print(Blue+'''
Kris has escaped the board!'''+reset)
  time.sleep(0.25)
  PNTC_function()
 def Progress_function():
  print("Progress of all players:")
  time.sleep(0.5)
  if Yourrt <= 0:
   print(Blue+'''
You have escaped the board!'''+reset)
  elif Yourrt > 0:
   print(Yournrt.format(Yourrt))
  time.sleep(0.25)
  if Jalenrt <= 0:
   print(Blue+'''
Jalen has escaped the board!'''+reset)
  elif Jalenrt > 0:
   print(Jalennrt.format(Jalenrt))
  time.sleep(0.25)
  if Jeremiahrt <= 0:
   print(Blue+'''
Jeremiah has escaped the board!'''+reset)
  elif Jeremiahrt > 0:
   print(Jeremiahnrt.format(Jeremiahrt))
  time.sleep(0.25)
  if Krisrt <= 0:
   print(Blue+'''
Kris has escaped the board!'''+reset)
  elif Krisrt > 0:
   print(Krisnrt.format(Krisrt))
  time.sleep(0.25)
  PETC_function()
 while PlayersLeft > DifficultyChoice and Yourrt > 0:
  Yourturn = True
  if Yourstuck == True:
   print(Red+"You are stuck so you cannot move."+reset)
   PETC_function()
   Yourstuck = False
   Yourturn = False
  elif Yourstuck == False:
   print("Your turn!")
   time.sleep(0.5)
   print("1 - Roll dice")
   time.sleep(0.25)
   print("2 - Check progress of players")
   time.sleep(0.25)
   NumChoiceWithQuit()
   try:
    Yourgo = int(input(""))
   except:
    InvalidInput()
    continue
   if Yourgo != 1 and Yourgo != 2:
    InvalidInput()
    continue
   elif Yourgo == 2:
    Progress_function()
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
   if Quitchoice == 2:
    continue
   Yourdiceroll1 = random.randrange(1,7)
   Yourdiceroll2 = random.randrange(1,7)
   Yourdicerollresults = "It looks like you rolled a {} and a {}, so you move {} tiles forward"
   print(Yourdicerollresults.format(Yourdiceroll1,Yourdiceroll2,Yourdiceroll1 + Yourdiceroll2))
   Yourtilesadded = Yourdiceroll1 + Yourdiceroll2
   Yourrt = Yourrt - Yourtilesadded
   You = 100 - Yourrt
   Yournt = "You have {} tiles remaining on the board"
   print(Yournt.format(Yourrt))
   time.sleep(1)
   if Yourrt % 2 == 0 and Yourrt > 0:
    while Yourturn == True:
     print('''It looks like you stepped on an even tile on the board,''')
     time.sleep(1)
     print('''Want to test your luck?''')
     YesOrNo()
     try:
      Yourlucktest = int(input(""))
     except: 
      InvalidInput()
      continue
     if Yourlucktest == 1:
      Yourrandomnumber = random.randrange(1,101)
      if Yourrandomnumber > Yourrt:
       Yourturn = False
       print(Red+"Uh Oh! It looks like you encountered a trap"+reset)
       if YourProtection == True and Youwon == False:
        print(Blue+"But you have protection so nothing will happen to you"+reset)
        YourProtection = False
        Yourturn = False
       elif YourProtection == False and Youwon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like you won't be going anywhere for one round")
         Yourstuck = True
         time.sleep(1)
         Yourturn = False
        elif Trapchoice == 2:
         print("You're going back to where you just came from!")
         time.sleep(1)
         Yourrt = Yourrt + Yourtilesadded
         Yournt = "You have {} tiles remaining on the board now"
         print(Yournt.format(Yourrt))
         time.sleep(1)
         Yourturn = False
        elif Trapchoice == 3:
         print('''You gave your luck away to one of your opponents!''')
         RandomNotYou = random.choice(PlayerListNotYou[0:3])
         if RandomNotYou == PlayerListNotYou[0]:
          JalenLuckChoice = random.randrange(1,5)
          if JalenLuckChoice == 1:
           print("Jalen moves your tiles now!")
           time.sleep(1)
           Jalenrt = Jalenrt - Yourtilesadded
           Jalennt = "Jalen has {} tiles remaining on the board now"
           time.sleep(1)
           print(Jalennt.format(Jalenrt))
           Jalenturn = False
          elif JalenLuckChoice == 2:
           Jalenbc = True
           while Jalenbc == True:
            Randomnumber = random.randrange(1,101)
            if Randomnumber <= 90:
             Jalenblow = 1
            elif Randomnumber > 90:
             Jalenblow = 2
            print("Jalen has been given the choice to blow someone away.")
            time.sleep(1)
            if Jalenblow == 1:
             Jalenblow = random.randrange(1,4)
             if Jalenblow == 1:
              print("Jalen chose to blow you away!")
              time.sleep(1)
              if YourProtection == False and Youwon == False:
               Yourta = (100 - Yourrt)/2
               Yourtr = round(Yourta)
               PlayerBlown = Red+"You have been blown {} tiles away."+reset
               print(PlayerBlown.format(Yourta))
               time.sleep(1)
               Yourrt = Yourrt + Yourtr
               Yournt = "You have {} tiles remaining on the board now"
               print(Yournt.format(Yourrt))
               time.sleep(1)
               Jalenbc = False
               Jalenturn = False
              elif YourProtection == True and Youwon == False:
               print(Blue+"You have protection so nothing happened!"+reset)
               time.sleep(1)
               YourProtection = False
               Jalenbc = False
               Jalenturn = False
              elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenblow == 2:
              print("Jalen chose to blow Jeremiah away!")
              time.sleep(1)
              if JeremiahProtection == False and Jeremiahwon == False:
               Jeremiahta = (100 - Jeremiahrt)/2
               Jeremiahtr = round(Jeremiahta)
               PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
               print(PlayerBlown.format(Jeremiahtr))
               time.sleep(1)
               Jeremiahrt = Jeremiahrt + Jeremiahtr
               Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
               print(Jeremiahnt.format(Jeremiahrt))
               time.sleep(1)
               Jalenbc = False
               Jalenturn = False
              elif JeremiahProtection == True and Jeremiahwon == False:
               print(Blue+"Jeremiah has protection so nothing happened!"+reset)
               time.sleep(1)
               JeremiahProtection = False
               Jalenbc = False
               Jalenturn = False
             elif Jalenblow != 1 and Jalenblow != 2:
              print("Jalen chose to blow Kris away!")
              time.sleep(1)
              if KrisProtection == False and Kriswon == False:
               Krista = (100 - Krisrt)/2
               Kristr = round(Krista)
               PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
               print(PlayerBlown.format(Kristr))
               time.sleep(1)
               Krisrt = Krisrt + Kristr   
               Krisnt = "Kris has {} tiles remaining on the board now"
               print(Krisnt.format(Krisrt))
               time.sleep(1)
               Jalenbc = False
               Jalenturn = False
              elif KrisProtection == True and Kriswon == False:
               print(Blue+"Kris has protection so nothing happened!"+reset)
               time.sleep(1)
               KrisProtection = False
               Jalenbc = False
               Jalenturn = False
              elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
            elif Jalenblow != 1:
             print("Jalen chose to not blow anyone away! how kind")
             time.sleep(1)
             Jalenbc = False
             Jalenturn = False
          elif JalenLuckChoice == 3:
           print(Blue+"Jalen is now protected from debuffs!"+reset)
           time.sleep(1)
           JalenProtection = True
           Jalenturn = False
          elif JalenLuckChoice == 4:
           Jalensc = True
           Randomnumber = random.randrange(1,101)
           while Jalensc == True:
            if Randomnumber <= 90:
             Jalenswap = 1
            elif Randomnumber > 90:
             Jalenswap = 2
            print("Jalen has been given the choice to swap with someone!")
            time.sleep(1)
            if Jalenswap == 1:
             Jalenswap = random.randrange(1,4)
             if Jalenswap == 1:
              print("Jalen chose to swap with you!")
              time.sleep(1)
              if YourProtection == False and Youwon == False:
               print(yellow+"Jalen swapped with you"+reset)
               time.sleep(1)
               Jalenoldtiles = Jalenrt
               Jalenrt = Yourrt
               Yourrt = Jalenoldtiles
               PlayerSwapped = "Jalen now has {} tiles remaining on the board and you have {} tiles remaining on the board."
               print(PlayerSwapped.format(Jalenrt,Yourrt))
               time.sleep(1)
               Jalensc = False
               Jalenturn = False
              elif YourProtection == True and Youwon == False:
               print(Blue+"You have protection so nothing happened!"+reset)
               time.sleep(1)
               YourProtection = False
               Jalensc = False
               Jalenturn = False
              elif Youwon == True:
               print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
               time.sleep(1)
               continue
             elif Jalenswap == 2:
              print("Jalen chose to swap with Jeremiah!")
              time.sleep(1)
              if JeremiahProtection == False and Jeremiahwon == False:
               print(yellow+"Jalen swapped with Jeremiah"+reset)
               time.sleep(1)
               Jalenoldtiles = Jalenrt
               Jalenrt = Jeremiahrt
               Jeremiahrt = Jalenoldtiles
               PlayerSwapped = "Jalen now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
               print(PlayerSwapped.format(Jalenrt,Jeremiahrt))
               time.sleep(1)
               Jalensc = False
               Jalenturn = False
              elif JeremiahProtection == True and Jeremiahwon == False:
               print(Blue+"Jeremiah has protection, so nothing happened"+reset)
               time.sleep(1)
               JeremiahProtection = False
               Jalensc = False
               Jalenturn = False
              elif Jeremiahwon == True:
               print(yellow+"Jeremiah has escaped the board, so Jalen will rechoose."+reset)
               time.sleep(1)
               continue
             elif Jalenswap != 1 or Jalenswap != 2:
              print("Jalen chose to swap with Kris!")
              time.sleep(1)
              if KrisProtection == False and Kriswon == False:
               print(yellow+"Jalen swapped with Kris"+reset)
               time.sleep(1)
               Jeremiaholdtiles = Jeremiahrt
               Jeremiahrt = Krisrt
               Krisrt = Jeremiaholdtiles
               PlayerSwapped = "Jalen now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
               print(PlayerSwapped.format(Jalenrt,Krisrt))
               time.sleep(1)
               Jalensc = False
               Jalenturn = False
              elif KrisProtection == True and Kriswon == False:
               print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
               time.sleep(1)
               KrisProtection = False
               Jalensc = False
               Jalenturn = False
              elif Kriswon == True:
               print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
               time.sleep(1)
               continue
            elif Jalenswap != 1:
             print("Jalen would not like to swap, that's ok")
             time.sleep(1)
             Jalensc = False
             Jalenturn = False
          Yourturn = False
         elif RandomNotYou == PlayerListNotYou[1]:
           JeremiahLuckChoice = random.randrange(1,5)
           if JeremiahLuckChoice == 1:
            print("Jeremiah moves your tiles now!")
            time.sleep(1)
            Jeremiahrt = Jeremiahrt - Yourtilesadded
            Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jeremiahnt.format(Jeremiahrt))
            Jeremiahturn = False
           elif JeremiahLuckChoice == 2:
            Jeremiahbc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahbc == True:
             if Randomnumber <= 90:
              Jeremiahblow = 1
             elif Randomnumber > 90:
              Jeremiahblow = 2
             print("Jeremiah has been given the choice to blow someone away.")
             time.sleep(1)
             if Jeremiahblow == 1:
              Jeremiahblow = random.randrange(1,4)
              if Jeremiahblow == 1:
               print("Jeremiah chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
              elif Jeremiahblow == 2:
               print("Jeremiah chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)         
                JalenProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow != 1 and Jeremiahblow != 2:
               print("Jeremiah chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahblow != 1:
              print("Jeremiah chose to not blow anyone away! how kind")
              time.sleep(1)
              Jeremiahbc = False
              Jeremiahturn = False
           elif JeremiahLuckChoice == 3:
            print(Blue+"Jeremiah is now protected from debuffs!"+reset)
            time.sleep(1)
            JeremiahProtection = True
            Jeremiahturn = False
           elif JeremiahLuckChoice == 4:
            Jeremiahsc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahsc == True:
             if Randomnumber <= 90:
              Jeremiahswap = 1
             elif Randomnumber > 90:
              Jeremiahswap = 2
             print("Jeremiah has been given the choice to swap with someone!")
             time.sleep(1)
             if Jeremiahswap == 1:
              Jeremiahswap = random.randrange(1,4)
              if Jeremiahswap == 1:
               print("Jeremiah chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jeremiah swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Yourrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap == 2:
               print("Jeremiah chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Jeremiah swapped with Jalen"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Jalenrt
                Jalenrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Jalenrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap != 1 or Jeremiahswap != 2:
               print("Jeremiah chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jeremiah swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Krisrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahswap != 1:
              print("Jeremiah would not like to swap, that's ok")
              time.sleep(1)
              Jeremiahsc = False
              Jeremiahturn = False
           Yourturn = False
         elif RandomNotYou == PlayerListNotYou[2]:
           KrisLuckChoice = random.randrange(1,5)
           if KrisLuckChoice == 1:
            print("Kris moves your tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Yourtilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
           elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)
                JalenProtection = False
                Krisbc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
           elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
           elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Kris swapped with Jalen"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jalenrt
                Jalenrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jalenrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Krissc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
           Yourturn = False
      elif Yourrandomnumber <= Yourrt:
       Yourturn = False
       print(Blue+"Lucky you! You obtained a boost!"+reset)
       YourLuckchoice = random.randrange(1,5)
       if YourLuckchoice == 1:
         print("You move double tiles now!")
         time.sleep(1)
         Yourrt = Yourrt - Yourtilesadded
         Yournt = "You have {} tiles remaining on the board now"
         print(Yournt.format(Yourrt))
         time.sleep(1)
         Yourturn = False
       elif YourLuckchoice == 2:
         Yourbc = True
         while Yourbc == True:
          print('''You were granted the ability to blow a player away, proceed?''')
          YORBG_function()
          try:
           Yourblow = int(input(""))
          except:
           InvalidInput()
           continue
          if Yourblow == 1:
           while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if JalenProtection == False and Jalenwon == False:
                   Jalenta = (100 - Jalenrt)/2
                   Jalentr = round(Jalenta)
                   PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jalentr))
                   Jalenrt = Jalenrt + Jalentr
                   Jalennt = "Jalen has {} tiles remaining on the board now"
                   print(Jalennt.format(Jalenrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
          elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
          elif Yourblow == 3:
                 Progress_function()
                 continue
          else:
                 InvalidInput()
                 continue
       elif YourLuckchoice == 3:
         print(Blue+"You are now protected from debuffs!"+reset)
         time.sleep(1)
         YourProtection = True
         Yourturn = False
       elif YourLuckchoice == 4:
         Yoursc = True
         while Yoursc == True:
             print("You were granted the ability to swap with another player, proceed?")
             YORBG_function()
             try:
               Yourswap = int(input(""))
             except:
               InvalidInput()
               continue
             if Yourswap == 1:
              while Yoursc == True:
               print("Choose the player that you want to swap with:")
               ChsPlr_function()
               try:
                Yourswap = int(input(""))
               except:
                InvalidInput()
                continue
               if Yourswap == 1:
                if JalenProtection == False and Jalenwon == False:
                 print(yellow+"You swapped with Jalen"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Jalenrt
                 Jalenrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Jalenrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif JalenProtection == True and Jalenwon == False:
                 print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                 JalenProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               elif Yourswap == 2:
                if JeremiahProtection == False and Jeremiahwon == False:
                 print(yellow+"You swapped with Jeremiah"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Jeremiahrt
                 Jeremiahrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif JeremiahProtection == True and Jeremiahwon == False:
                 print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                 JeremiahProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
               elif Yourswap == 3:
                if KrisProtection == False and Kriswon == False:
                 print(yellow+"You swapped with Kris"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Krisrt
                 Krisrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Krisrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif KrisProtection == True and Kriswon == False:
                 print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                 KrisProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               else:
                InvalidInput()
                continue
             elif Yourswap == 2:
               print("Well that's ok")
               time.sleep(1)
               Yoursc = False
             elif Yourswap == 3:
               Progress_function()
             else:
              InvalidInput()
              continue    
       Yourturn = False
     elif Yourlucktest == 2:
      print("It looks like you chose to play safe, that's ok.")
      time.sleep(1)
      Yourturn = False
   elif Yourrt % 2 != 0:
    Yourturn = False
  if Yourrt <= 0:
   clearScreen()
   print(Blue+"You have successfully crossed the entire trail of the game so you win!"+reset)
   PETC_function()
   if DifficultyChoice == 1:
    return "EW"
   elif DifficultyChoice == 2:
    return "MW"
   elif DifficultyChoice == 3:
    return "HW"
  Jalenturn = True
  if Jalenstuck == True:
   print(Red+"Jalen is stuck so he cannot move."+reset)
   time.sleep(1)
   Jalenstuck = False
   Jalenturn = False
  elif Jalenwon == True:
   print(Blue+"Jalen has escaped the board!"+reset)
   time.sleep(1)
  elif Jalenstuck == False and Jalenrt > 0 and Jalenwon == False:
   print("Jalen's turn!")
   time.sleep(1)
   Jalendiceroll1 = random.randrange(1,7)
   Jalendiceroll2 = random.randrange(1,7)
   Jalendicerollresults = "It looks like Jalen rolled a {} and a {}, so Jalen moves {} tiles forward"
   print(Jalendicerollresults.format(Jalendiceroll1,Jalendiceroll2,Jalendiceroll1 + Jalendiceroll2))
   Jalentilesadded = Jalendiceroll1 + Jalendiceroll2
   Jalenrt = Jalenrt - Jalentilesadded
   Jalennt = "Jalen has {} tiles remaining on the board"
   print(Jalennt.format(Jalenrt))
   time.sleep(1)
   if Jalenrt % 2 == 0 and Jalenrt > 0:
    while Jalenturn == True:
     print('''It looks like Jalen stepped on an even tile on the board''')
     time.sleep(1)
     Randomnumber = random.randrange(1,101)
     if Randomnumber <= 75:
      Jalenlucktest = 1
     elif Randomnumber > 75:
      Jalenlucktest = 2
     if Jalenlucktest == 1:
      print("Jalen wants to test his luck")
      time.sleep(1)
      Jalenrandomnumber = random.randrange(1,101)
      if Jalenrandomnumber > Jalenrt:
       Jalenturn = False
       print(Red+"Uh Oh! It looks like Jalen encountered a trap"+reset)
       time.sleep(1)
       if JalenProtection == True and Jalenwon == False:
        print(Blue+"But Jalen has protection so nothing will happen to Jalen "+reset)
        time.sleep(1)
        JalenProtection == False and Jalenwon == False
        Jalenturn = False
       elif JalenProtection == False and Jalenwon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like Jalen won't be going anywhere for one round")
         time.sleep(1)
         Jalenstuck = True
         Jalenturn = False
        elif Trapchoice == 2:
         print("Jalen is going back to where he just came from!")
         time.sleep(1)
         Jalenrt = Jalenrt + Jalentilesadded
         Jalennt = "Jalen has {} tiles remaining on the board now"
         time.sleep(1)
         print(Jalennt.format(Jalenrt))
         Jalenturn = False
        elif Trapchoice == 3:
         print('''Jalen gave his luck away to one of his opponents!''')
         time.sleep(1)
         RandomNotJalen = random.choice(PlayerListNotJalen[0:3])
         if RandomNotJalen == PlayerListNotJalen[0]:
            YourLuckchoice = random.randrange(1,5)
            if YourLuckchoice == 1:
             print("You move Jalen's tiles now!")
             Yourrt = Yourrt - Yourtilesadded
             Yournt = "You have {} tiles remaining on the board now"
             print(Yournt.format(Yourrt))
             time.sleep(1)
             Yourturn = False
            elif YourLuckchoice == 2:
             Yourbc = True
             while Yourbc == True:
              print("You were granted the ability to blow a player away, proceed?")
              YORBG_function()
              try:
               Yourblow = int(input(""))
              except:
               InvalidInput()
               continue
              if Yourblow == 1:
               while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if JalenProtection == False and Jalenwon == False:
                   Jalenta = (100 - Jalenrt)/2
                   Jalentr = round(Jalenta)
                   PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jalentr))
                   Jalenrt = Jalenrt + Jalentr
                   Jalennt = "Jalen has {} tiles remaining on the board now"
                   print(Jalennt.format(Jalenrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
              elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
              elif Yourblow == 3:
                 Progress_function()
                 continue
              else:
                 InvalidInput()
                 continue
            elif YourLuckchoice == 3:
             print(Blue+"You are now protected from debuffs!"+reset)
             time.sleep(1)
             YourProtection = True
             Yourturn = False
            elif YourLuckchoice == 4:
             Yoursc = True
             while Yoursc == True:
               print("You were granted the ability to swap with another player, proceed?")
               YORBG_function()
               try:
                 Yourswap = int(input(""))
               except:
                 InvalidInput()
                 continue
               if Yourswap == 1:
                while Yoursc == True:
                 print("Choose the player that you want to swap with:")
                 ChsPlr_function()
                 try:
                  Yourswap = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourswap == 1:
                  if JalenProtection == False and Jalenwon == False:
                   print(yellow+"You swapped with Jalen"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jalenrt
                   Jalenrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jalenrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   print(yellow+"You swapped with Jeremiah"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jeremiahrt
                   Jeremiahrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                   JeremiahProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                 elif Yourswap == 3:
                  if KrisProtection == False and Kriswon == False:
                   print(yellow+"You swapped with Kris"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Krisrt
                   Krisrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Krisrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
               elif Yourswap == 2:
                 print("Well that's ok")
                 time.sleep(1)
                 Yoursc = False
               elif Yourswap == 3:
                 Progress_function()
               else:
                InvalidInput()
                continue
         elif RandomNotJalen == PlayerListNotJalen[1]:
            YourLuckchoice = random.randrange(1,5)
            if YourLuckchoice == 1:
             print("You move Jalen's tiles now!")
             Yourrt = Yourrt - Yourtilesadded
             Yournt = "You have {} tiles remaining on the board now"
             print(Yournt.format(Yourrt))
             time.sleep(1)
             Yourturn = False
            elif YourLuckchoice == 2:
             Yourbc = True
             while Yourbc == True:
              print("You were granted the ability to blow a player away, proceed?")
              YORBG_function()
              try:
               Yourblow = int(input(""))
              except:
               InvalidInput()
               continue
              if Yourblow == 1:
               while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if JalenProtection == False and Jalenwon == False:
                   Jalenta = (100 - Jalenrt)/2
                   Jalentr = round(Jalenta)
                   PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jalentr))
                   Jalenrt = Jalenrt + Jalentr
                   Jalennt = "Jalen has {} tiles remaining on the board now"
                   print(Jalennt.format(Jalenrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
              elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
              elif Yourblow == 3:
                 Progress_function()
                 continue
              else:
                 InvalidInput()
                 continue
            elif YourLuckchoice == 3:
             print(Blue+"You are now protected from debuffs!"+reset)
             time.sleep(1)
             YourProtection = True
             Yourturn = False
            elif YourLuckchoice == 4:
             Yoursc = True
             while Yoursc == True:
               print("You were granted the ability to swap with another player, proceed?")
               YORBG_function()
               try:
                 Yourswap = int(input(""))
               except:
                 InvalidInput()
                 continue
               if Yourswap == 1:
                while Yoursc == True:
                 print("Choose the player that you want to swap with:")
                 ChsPlr_function()
                 try:
                  Yourswap = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourswap == 1:
                  if JalenProtection == False and Jalenwon == False:
                   print(yellow+"You swapped with Jalen"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jalenrt
                   Jalenrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jalenrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   print(yellow+"You swapped with Jeremiah"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jeremiahrt
                   Jeremiahrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                   JeremiahProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                 elif Yourswap == 3:
                  if KrisProtection == False and Kriswon == False:
                   print(yellow+"You swapped with Kris"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Krisrt
                   Krisrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Krisrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
               elif Yourswap == 2:
                 print("Well that's ok")
                 time.sleep(1)
                 Yoursc = False
               elif Yourswap == 3:
                 Progress_function()
               else:
                InvalidInput()
                continue
         elif RandomNotJalen == PlayerListNotJalen[2]:
           KrisLuckChoice = random.randrange(1,5)
           if KrisLuckChoice == 1:
            print("Kris moves Jalen's tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Jalentilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
           elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)
                JalenProtection = False
                Krisbc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr 
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
           elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
           elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Kris swapped with Jalen"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jalenrt
                Jalenrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jalenrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Krissc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
      elif Jalenrandomnumber <= Jalenrt:
       Jalenturn = False
       print(Blue+"Lucky Jalen! Jalen obtained a boost!"+reset)
       time.sleep(1)
       JalenLuckChoice = random.randrange(1,5)
       if JalenLuckChoice == 1:
            print("Jalen moves double tiles now!")
            time.sleep(1)
            Jalenrt = Jalenrt - Jalentilesadded
            Jalennt = "Jalen has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jalennt.format(Jalenrt))
            Jalenturn = False
       elif JalenLuckChoice == 2:
            Jalenbc = True
            Randomnumber = random.randrange(1,101)
            while Jalenbc == True:
             if Randomnumber <= 90:
              Jalenblow = 1
             elif Randomnumber > 90:
              Jalenblow = 2
             print("Jalen has been given the choice to blow someone away.")
             time.sleep(1)
             if Jalenblow == 1:
              Jalenblow = random.randrange(1,4)
              if Jalenblow == 1:
               print("Jalen chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenblow == 2:
               print("Jalen chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Jalenbc = False
                Jalenturn = False
              elif Jalenblow != 1 and Jalenblow != 2:
               print("Jalen chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenblow != 1:
              print("Jalen chose to not blow anyone away! how kind")
              time.sleep(1)
              Jalenbc = False
              Jalenturn = False
       elif JalenLuckChoice == 3:
            print(Blue+"Jalen is now protected from debuffs!"+reset)
            time.sleep(1)
            JalenProtection = True
            Jalenturn = False
       elif JalenLuckChoice == 4:
            Jalensc = True
            Randomnumber = random.randrange(1,101)
            while Jalensc == True:
             if Randomnumber <= 90:
              Jalenswap = 1
             elif Randomnumber > 90:
              Jalenswap = 2
             print("Jalen has been given the choice to swap with someone!")
             time.sleep(1)
             if Jalenswap == 1:
              Jalenswap = random.randrange(1,4)
              if Jalenswap == 1:
               print("Jalen chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jalen swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jalenrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Yourrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jalensc = False
                Jalenturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenswap == 2:
               print("Jalen chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Jalen swapped with Jeremiah"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jalenrt = Jeremiahrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Jeremiahrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Jalensc = False
                Jalenturn = False
              elif Jalenswap != 1 or Jalenswap != 2:
               print("Jalen chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jalen swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Krisrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jalensc = False
                Jalenturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenswap != 1:
              print("Jalen would not like to swap, that's ok")
              time.sleep(1)
              Jalensc = False
              Jalenturn = False
     elif Jalenlucktest == 2:
      print("It looks like Jalen chose to play safe, that's ok.")
      time.sleep(1)
      Jalenturn = False
   elif Jalenrt % 2 != 0:
    Jalenturn = False 
  if Jalenrt <= 0 and Jalenwon == False:
   clearScreen()
   print(Blue+"Jalen has successfully crossed the entire trail of the game!"+reset)
   PETC_function()
   PlayersLeft = PlayersLeft - 1
   Jalenwon = True
  Jeremiahturn = True
  if Jeremiahstuck == True:
   print(Red+"Jeremiah is stuck so he cannot move."+reset)
   time.sleep(1)
   Jeremiahstuck = False
   Jeremiahturn = False
  elif Jeremiahwon == True:
   print(Blue+"Jeremiah has escaped the board!"+reset)
   time.sleep(1)
  elif Jeremiahstuck == False and Jeremiahrt > 0 and Jeremiahwon == False:
   print("Jeremiah's turn!")
   time.sleep(1)
   Jeremiahdiceroll1 = random.randrange(1,7)
   Jeremiahdiceroll2 = random.randrange(1,7)
   Jeremiahdicerollresults = "It looks like Jeremiah rolled a {} and a {}, so Jeremiah moves {} tiles forward"
   print(Jeremiahdicerollresults.format(Jeremiahdiceroll1,Jeremiahdiceroll2,Jeremiahdiceroll1 + Jeremiahdiceroll2))
   Jeremiahtilesadded = Jeremiahdiceroll1 + Jeremiahdiceroll2
   Jeremiahrt = Jeremiahrt - Jeremiahtilesadded
   Jeremiahnt = "Jeremiah has {} tiles remaining on the board"
   print(Jeremiahnt.format(Jeremiahrt))
   time.sleep(1)
   if Jeremiahrt % 2 == 0 and Jeremiahrt > 0:
    while Jeremiahturn == True:
     print('''It looks like Jeremiah stepped on an even tile on the board''')
     time.sleep(1)
     Randomnumber = random.randrange(1,101)
     if Randomnumber <= 75:
      Jeremiahlucktest = 1
     elif Randomnumber > 75:
      Jeremiahlucktest = 2
     if Jeremiahlucktest == 1:
      print("Jeremiah wants to test his luck")
      time.sleep(1)
      Jeremiahrandomnumber = random.randrange(1,101)
      if Jeremiahrandomnumber > Jeremiahrt:
       Jeremiahturn = False
       print(Red+"Uh Oh! It looks like Jeremiah encountered a trap"+reset)
       time.sleep(1)
       if JeremiahProtection == True and Jeremiahwon == False:
        print(Blue+"But Jeremiah has protection so nothing will happen to Jeremiah"+reset)
        time.sleep(1)
        Jeremiahturn = False
        JeremiahProtection = False
       elif JeremiahProtection == False and Jeremiahwon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like Jeremiah won't be going anywhere for one round")
         time.sleep(1)
         Jeremiahstuck = True
         Jeremiahturn = False
        elif Trapchoice == 2:
         print("Jeremiah is going back to where he just came from!")
         time.sleep(1)
         Jeremiahrt = Jeremiahrt + Jeremiahtilesadded
         Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
         time.sleep(1)
         print(Jeremiahnt.format(Jeremiahrt))
         Jeremiahturn = False
        elif Trapchoice == 3:
         print('''Jeremiah gave his luck away to one of his opponents!''')
         time.sleep(1)
         RandomNotJeremiah = random.choice(PlayerListNotJeremiah[0:3])
         if RandomNotJeremiah == PlayerListNotJeremiah[0]:
          YourLuckchoice = random.randrange(1,5)
          if YourLuckchoice == 1:
             print("You move Jeremiah's tiles now!")
             Yourrt = Yourrt - Jeremiahtilesadded
             Yournt = "You have {} tiles remaining on the board now"
             print(Yournt.format(Yourrt))
             time.sleep(1)
             Yourturn = False
          elif YourLuckchoice == 2:
             Yourbc = True
             while Yourbc == True:
              print("You were granted the ability to blow a player away, proceed?")
              YORBG_function()
              try:
               Yourblow = int(input(""))
              except:
               InvalidInput()
               continue
              if Yourblow == 1:
               while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if JalenProtection == False and Jalenwon == False:
                   Jalenta = (100 - Jalenrt)/2
                   Jalentr = round(Jalenta)
                   PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jalentr))
                   Jalenrt = Jalenrt + Jalentr
                   Jalennt = "Jalen has {} tiles remaining on the board now"
                   print(Jalennt.format(Jalenrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
              elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
              elif Yourblow == 3:
                 Progress_function()
                 continue
              else:
                 InvalidInput()
                 continue
          elif YourLuckchoice == 3:
             print(Blue+"You are now protected from debuffs!"+reset)
             time.sleep(1)
             YourProtection = True
             Yourturn = False
          elif YourLuckchoice == 4:
             Yoursc = True
             while Yoursc == True:
               print("You were granted the ability to swap with another player, proceed?")
               YORBG_function()
               try:
                 Yourswap = int(input(""))
               except:
                 InvalidInput()
                 continue
               if Yourswap == 1:
                while Yoursc == True:
                 print("Choose the player that you want to swap with:")
                 ChsPlr_function()
                 try:
                  Yourswap = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourswap == 1:
                  if JalenProtection == False and Jalenwon == False:
                   print(yellow+"You swapped with Jalen"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jalenrt
                   Jalenrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jalenrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   print(yellow+"You swapped with Jeremiah"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jeremiahrt
                   Jeremiahrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                   JeremiahProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 3:
                  if KrisProtection == False and Kriswon == False:
                   print(yellow+"You swapped with Kris"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Krisrt
                   Krisrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Krisrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
               elif Yourswap == 2:
                 print("Well that's ok")
                 time.sleep(1)
                 Yoursc = False
               elif Yourswap == 3:
                 Progress_function()
               else:
                InvalidInput()
                continue
         elif RandomNotJeremiah == PlayerListNotJeremiah[1]:
           JalenLuckChoice = random.randrange(1,5)
           if JalenLuckChoice == 1:
            print("Jalen moves Jeremiah's tiles now!")
            time.sleep(1)
            Jalenrt = Jalenrt - Jeremiahtilesadded
            Jalennt = "Jalen has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jalennt.format(Jalenrt))
            Jalenturn = False
           elif JalenLuckChoice == 2:
            Jalenbc = True
            Randomnumber = random.randrange(1,101)
            while Jalenbc == True:
             if Randomnumber <= 90:
              Jalenblow = 1
             elif Randomnumber > 90:
              Jalenblow = 2
             print("Jalen has been given the choice to blow someone away.")
             time.sleep(1)
             if Jalenblow == 1:
              Jalenblow = random.randrange(1,4)
              if Jalenblow == 1:
               print("Jalen chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2 
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenblow == 2:
               print("Jalen chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenblow != 1 and Jalenblow != 2:
               print("Jalen chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenblow != 1:
              print("Jalen chose to not blow anyone away! how kind")
              time.sleep(1)
              Jalenbc = False
              Jalenturn = False
           elif JalenLuckChoice == 3:
            print(Blue+"Jalen is now protected from debuffs!"+reset)
            time.sleep(1)
            JalenProtection = True
            Jalenturn = False
           elif JalenLuckChoice == 4:
            Jalensc = True
            Randomnumber = random.randrange(1,101)
            while Jalensc == True:
             if Randomnumber <= 90:
              Jalenswap = 1
             elif Randomnumber > 90:
              Jalenswap = 2
             print("Jalen has been given the choice to swap with someone!")
             time.sleep(1)
             if Jalenswap == 1:
              Jalenswap = random.randrange(1,4)
              if Jalenswap == 1:
               print("Jalen chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jalen swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jalenrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Yourrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jalensc = False
                Jalenturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenswap == 2:
               print("Jalen chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Jalen swapped with Jeremiah"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jalenrt = Jeremiahrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Jeremiahrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Jalensc = False
                Jalenturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenswap != 1 or Jalenswap != 2:
               print("Jalen chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jalen swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Krisrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jalensc = False
                Jalenturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenswap != 1:
              print("Jalen would not like to swap, that's ok")
              time.sleep(1)
              Jalensc = False
              Jalenturn = False
         elif RandomNotJeremiah == PlayerListNotJeremiah[2]:
           KrisLuckChoice = random.randrange(1,5)
           if KrisLuckChoice == 1:
            print("Kris moves Jeremiah's tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Jeremiahtilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
           elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)
                JalenProtection = False
                Krisbc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr 
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
           elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
           elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Kris swapped with Jalen"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jalenrt
                Jalenrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jalenrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Krissc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
      elif Jeremiahrandomnumber <= Jeremiahrt:
       Jeremiahturn = False
       print(Blue+"Lucky Jeremiah! Jeremiah obtained a boost!"+reset)
       time.sleep(1)
       JeremiahLuckChoice = random.randrange(1,5)
       if JeremiahLuckChoice == 1:
            print("Jeremiah moves double tiles now!")
            time.sleep(1)
            Jeremiahrt = Jeremiahrt - Jeremiahtilesadded
            Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jeremiahnt.format(Jeremiahrt))
            Jeremiahturn = False
       elif JeremiahLuckChoice == 2:
            Jeremiahbc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahbc == True:
             if Randomnumber <= 90:
              Jeremiahblow = 1
             elif Randomnumber > 90:
              Jeremiahblow = 2
             print("Jeremiah has been given the choice to blow someone away.")
             time.sleep(1)
             if Jeremiahblow == 1:
              Jeremiahblow = random.randrange(1,4)
              if Jeremiahblow == 1:
               print("Jeremiah chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow == 2:
               print("Jeremiah chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)         
                JalenProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow != 1 and Jeremiahblow != 2:
               print("Jeremiah chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Krista))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahblow != 1:
              print("Jeremiah chose to not blow anyone away! how kind")
              time.sleep(1)
              Jeremiahbc = False
              Jeremiahturn = False
       elif JeremiahLuckChoice == 3:
            print(Blue+"Jeremiah is now protected from debuffs!"+reset)
            time.sleep(1)
            JeremiahProtection = True
            Jeremiahturn = False
       elif JeremiahLuckChoice == 4:
            Jeremiahsc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahsc == True:
             if Randomnumber <= 90:
              Jeremiahswap = 1
             elif Randomnumber > 90:
              Jeremiahswap = 2
             print("Jeremiah has been given the choice to swap with someone!")
             time.sleep(1)
             if Jeremiahswap == 1:
              Jeremiahswap = random.randrange(1,4)
              if Jeremiahswap == 1:
               print("Jeremiah chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jeremiah swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Yourrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap == 2:
               print("Jeremiah chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Jeremiah swapped with Jalen"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Jalenrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Jalenrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap != 1 or Jeremiahswap != 2:
               print("Jeremiah chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jeremiah swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Krisrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahswap != 1:
               print("Jeremiah would not like to swap, that's ok")
               time.sleep(1)
               Jeremiahsc = False
               Jeremiahturn = False
     elif Jeremiahlucktest == 2:
      print("It looks like Jeremiah chose to play safe, that's ok.")
      time.sleep(1)
      Jeremiahturn = False
   elif Jeremiahrt % 2 != 0:
    Jeremiahturn = False
  if Jeremiahrt <= 0 and Jeremiahwon == False:
   clearScreen()
   print(Blue+"Jeremiah has successfully crossed the entire trail of the game!"+reset)
   PETC_function()
   PlayersLeft = PlayersLeft - 1
   Jeremiahwon = True
  Kristurn = True
  if Krisstuck == True:
   print(Red+"Kris is stuck so he cannot move."+reset)
   time.sleep(1)
   Krisstuck = False
   Kristurn = False
  elif Kriswon == True:
   print(Blue+"Kris has escaped the board!"+reset)
   time.sleep(1)
  elif Krisstuck == False and Krisrt > 0 and Kriswon == False:
   print("Kris's turn!")
   time.sleep(1)
   Krisdiceroll1 = random.randrange(1,7)
   Krisdiceroll2 = random.randrange(1,7)
   Krisdicerollresults = "It looks like Kris rolled a {} and a {}, so Kris moves {} tiles forward"
   print(Krisdicerollresults.format(Krisdiceroll1,Krisdiceroll2,Krisdiceroll1 + Krisdiceroll2))
   Kristilesadded = Krisdiceroll1 + Krisdiceroll2
   Krisrt = Krisrt - Kristilesadded
   Krisnt = "Kris has {} tiles remaining on the board"
   print(Krisnt.format(Krisrt))
   time.sleep(1)
   if Krisrt % 2 == 0 and Krisrt > 0:
    while Kristurn == True:
     print('''It looks like Kris stepped on an even tile on the board''')
     time.sleep(1)
     Randomnumber = random.randrange(1,101)
     if Randomnumber <= 75:
      Krislucktest = 1
     elif Randomnumber > 75:
      Krislucktest = 2
     if Krislucktest == 1:
      print("Kris wants to test his luck")
      time.sleep(1)
      Krisrandomnumber = random.randrange(1,101)
      if Krisrandomnumber > Krisrt:
       Kristurn = False
       print(Red+"Uh Oh! It looks like Kris encountered a trap"+reset)
       time.sleep(1)
       if KrisProtection == True and Kriswon == False:
        print(Blue+"But Kris has protection so nothing will happen to Kris "+reset)
        KrisProtection = False
        time.sleep(1)
        Kristurn = False
       elif KrisProtection == False and Kriswon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like Kris won't be going anywhere for one round")
         time.sleep(1)
         Krisstuck = True
         Kristurn = False
        elif Trapchoice == 2:
         print("Kris is going back to where he just came from!")
         time.sleep(1)
         Krisrt = Krisrt + Kristilesadded
         Krisnt = "Kris has {} tiles remaining on the board now"
         time.sleep(1)
         print(Krisnt.format(Krisrt))
         Kristurn = False
        elif Trapchoice == 3:
         print('''Kris gave his luck away to one of his opponents!''')
         time.sleep(1)
         RandomNotKris = random.choice(PlayerListNotKris[0:3])
         if RandomNotKris == PlayerListNotKris[0]:
          YourLuckchoice = random.randrange(1,5)
          if YourLuckchoice == 1:
           print("You move Kris's tiles now!")
           Yourrt = Yourrt - Kristilesadded
           Yournt = "You have {} tiles remaining on the board now"
           print(Yournt.format(Yourrt))
           time.sleep(1)
           Yourturn = False
          elif YourLuckchoice == 2:
            Yourbc = True
            while Yourbc == True:
                print('''You were granted the ability to blow a player away, proceed?''')
                YORBG_function()
                try:
                  Yourblow = int(input(""))
                except:
                  InvalidInput()
                  continue
                if Yourblow == 1:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if JalenProtection == False and Jalenwon == False:
                   Jalenta = (100 - Jalenrt)/2
                   Jalentr = round(Jalenta)
                   PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jalentr))
                   Jalenrt = Jalenrt + Jalentr
                   Jalennt = "Jalen has {} tiles remaining on the board now"
                   print(Jalennt.format(Jalenrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JalenProtection == True and Jalenwon == False:
                   print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                   JalenProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
                elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
                elif Yourblow == 3:
                 Progress_function()
                else:
                 InvalidInput()
                 continue
          elif YourLuckchoice == 3:
            print(Blue+"You are now protected from debuffs!"+reset)
            time.sleep(1)
            YourProtection = True
            Yourturn = False
          elif YourLuckchoice == 4:
            Yoursc = True
            while Yoursc == True:
             print("You were granted the ability to swap with another player, proceed?")
             YORBG_function()
             try:
               Yourswap = int(input(""))
             except:
               InvalidInput()
               continue
             if Yourswap == 1:
              while Yoursc == True:
               print("Choose the player that you want to swap with:")
               ChsPlr_function()
               try:
                Yourswap = int(input(""))
               except:
                InvalidInput()
                continue
               if Yourswap == 1:
                if JalenProtection == False and Jalenwon == False:
                 print(yellow+"You swapped with Jalen"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Jalenrt
                 Jalenrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Jalenrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif JalenProtection == True and Jalenwon == False:
                 print(Blue+Blue+"Jalen has protection so nothing happened!"+reset)
                 JalenProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               elif Yourswap == 2:
                if JeremiahProtection == False and Jeremiahwon == False:
                 print(yellow+"You swapped with Jeremiah"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Jeremiahrt
                 Jeremiahrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif JeremiahProtection == True and Jeremiahwon == False:
                 print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                 JeremiahProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               elif Yourswap == 3:
                if KrisProtection == False and Kriswon == False:
                 print(yellow+"You swapped with Kris"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Krisrt
                 Krisrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Krisrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif KrisProtection == True and Kriswon == False:
                 print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                 KrisProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               else:
                InvalidInput()
                continue
             elif Yourswap == 2:
               print("Well that's ok")
               time.sleep(1)
               Yoursc = False
             elif Yourswap == 3:
               Progress_function()
             else:
              InvalidInput()
              continue
         elif RandomNotKris == PlayerListNotKris[1]:
           JalenLuckChoice = random.randrange(1,5)
           if JalenLuckChoice == 1:
            print("Jalen moves Kris's tiles now!")
            time.sleep(1)
            Jalenrt = Jalenrt - Kristilesadded
            Jalennt = "Jalen has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jalennt.format(Jalenrt))
            Jalenturn = False
           elif JalenLuckChoice == 2:
            Jalenbc = True
            Randomnumber = random.randrange(1,101)
            while Jalenbc == True:
             if Randomnumber <= 90:
              Jalenblow = 1
             elif Randomnumber > 90:
              Jalenblow = 2
             print("Jalen has been given the choice to blow someone away.")
             time.sleep(1)
             if Jalenblow == 1:
              Jalenblow = random.randrange(1,4)
              if Jalenblow == 1:
               print("Jalen chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenblow == 2:
               print("Jalen chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenblow != 1 and Jalenblow != 2:
               print("Jalen chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jalenbc = False
                Jalenturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jalenbc = False
                Jalenturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenblow != 1:
              print("Jalen chose to not blow anyone away! how kind")
              time.sleep(1)
              Jalenbc = False
              Jalenturn = False
           elif JalenLuckChoice == 3:
            print(Blue+"Jalen is now protected from debuffs!"+reset)
            time.sleep(1)
            JalenProtection = True
            Jalenturn = False
           elif JalenLuckChoice == 4:
            Jalensc = True
            Randomnumber = random.randrange(1,101)
            while Jalensc == True:
             if Randomnumber <= 90:
              Jalenswap = 1
             elif Randomnumber > 90:
              Jalenswap = 2
             print("Jalen has been given the choice to swap with someone!")
             time.sleep(1)
             if Jalenswap == 1:
              Jalenswap = random.randrange(1,4)
              if Jalenswap == 1:
               print("Jalen chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jalen swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jalenrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Yourrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jalensc = False
                Jalenturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenswap == 2:
               print("Jalen chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Jalen swapped with Jeremiah"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jalenrt = Jeremiahrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Jeremiahrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Jalensc = False
                Jalenturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jalenswap != 1 or Jalenswap != 2:
               print("Jalen chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jalen swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jalen now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jalenrt,Krisrt))
                time.sleep(1)
                Jalensc = False
                Jalenturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jalensc = False
                Jalenturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jalen will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jalenswap != 1:
              print("Jalen would not like to swap, that's ok")
              time.sleep(1)
              Jalensc = False
              Jalenturn = False
         elif RandomNotKris == PlayerListNotKris[2]:
           JeremiahLuckChoice = random.randrange(1,5)
           if JeremiahLuckChoice == 1:
            print("Jeremiah moves Kris's tiles now!")
            time.sleep(1)
            Jeremiahrt = Jeremiahrt - Kristilesadded
            Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jeremiahnt.format(Jeremiahrt))
            Jeremiahturn = False
           elif JeremiahLuckChoice == 2:
            Jeremiahbc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahbc == True:
             if Randomnumber <= 90:
              Jeremiahblow = 1
             elif Randomnumber > 90:
              Jeremiahblow = 2
             print("Jeremiah has been given the choice to blow someone away.")
             time.sleep(1)
             if Jeremiahblow == 1:
              Jeremiahblow = random.randrange(1,4)
              if Jeremiahblow == 1:
               print("Jeremiah chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow == 2:
               print("Jeremiah chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)         
                JalenProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow != 1 and Jeremiahblow != 2:
               print("Jeremiah chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahblow != 1:
              print("Jeremiah chose to not blow anyone away! how kind")
              time.sleep(1)
              Jeremiahbc = False
              Jeremiahturn = False
           elif JeremiahLuckChoice == 3:
            print(Blue+"Jeremiah is now protected from debuffs!"+reset)
            time.sleep(1)
            JeremiahProtection = True
            Jeremiahturn = False
           elif JeremiahLuckChoice == 4:
            Jeremiahsc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahsc == True:
             Jeremiahsc = False
             if Randomnumber <= 90:
              Jeremiahswap = 1
             elif Randomnumber > 90:
              Jeremiahswap = 2
             print("Jeremiah has been given the choice to swap with someone!")
             time.sleep(1)
             if Jeremiahswap == 1:
              Jeremiahswap = random.randrange(1,4)
              if Jeremiahswap == 1:
               print("Jeremiah chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jeremiah swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Yourrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap == 2:
               print("Jeremiah chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Jeremiah swapped with Jalen"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Jalenrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Jalenrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap != 1 or Jeremiahswap != 2:
               print("Jeremiah chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jeremiah swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Krisrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahswap != 1:
              print("Jeremiah would not like to swap, that's ok")
              time.sleep(1)
              Jeremiahsc = False
              Jeremiahturn = False
      elif Krisrandomnumber <= Krisrt:
       Kristurn = False
       print(Blue+"Lucky Kris! Kris obtained a boost!"+reset)
       time.sleep(1)
       KrisLuckChoice = random.randrange(1,5)
       if KrisLuckChoice == 1:
            print("Kris moves double tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Kristilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
       elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow Jalen away!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                Jalenta = (100 - Jalenrt)/2
                Jalentr = round(Jalenta)
                PlayerBlown = Red+"Jalen has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jalentr))
                time.sleep(1)
                Jalenrt = Jalenrt + Jalentr
                Jalennt = "Jalen has {} tiles remaining on the board now"
                print(Jalennt.format(Jalenrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print(Blue+"Jalen has protection so nothing happened!"+reset)
                time.sleep(1)
                JalenProtection = False
                Krisbc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr   
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
       elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
       elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with Jalen!")
               time.sleep(1)
               if JalenProtection == False and Jalenwon == False:
                print(yellow+"Kris swapped with Jalen"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jalenrt
                Jalenrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jalen has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jalenrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JalenProtection == True and Jalenwon == False:
                print("Jalen has protection, so nothing happened!")
                time.sleep(1)
                JalenProtection = False
                Krissc = False
                Kristurn = False
               elif Jalenwon == True:
                   print(yellow+"Jalen has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
     elif Krislucktest == 2:
      print("It looks like Kris chose to play safe, that's ok.")
      time.sleep(1)
      Kristurn = False
   elif Krisrt % 2 != 0:
    Kristurn = False
  if Krisrt <= 0 and Kriswon == False:
   clearScreen()
   print(Blue+"Kris has successfully crossed the entire trail of the game!"+reset)
   PETC_function()
   PlayersLeft = PlayersLeft - 1
   Kriswon = True
  Progress_function()
 if Krisrt <= 0:
  print("KRIS WINS") 
 elif Krisrt > 0:
  print("KRIS LOSES")
 if Jeremiahrt <= 0:
  print("JEREMIAH WINS")
 elif Jeremiahrt > 0:
  print("JEREMIAH LOSES")
 if Jalenrt <= 0:
  print("JALEN WINS")
 elif Jalenrt > 0:
  print("JALEN LOSES")
 if Yourrt <= 0:
  print("YOU WIN")
 elif Yourrt > 0:
  print("YOU LOSE")
 PETC_function()
 if Yourrt <= 0 and DifficultyChoice == 1:
  return "EW"
 elif Yourrt <= 0 and DifficultyChoice == 2:
  return "MW"
 elif Yourrt <= 0 and DifficultyChoice == 3:
  return "HW"
 elif Yourrt > 0 and DifficultyChoice == 1:
  return "EL"
 elif Yourrt > 0 and DifficultyChoice == 2:
  return "ML"
 elif Yourrt > 0 and DifficultyChoice == 3:
  return "HL"
   
#Board Game 

def pvplevel8_function(PlayerOneName,PlayerTwoName):
 Yourrt = 50
 TwoPlrrt = 50
 Jeremiahrt = 50
 Krisrt = 50
 YourProtection = False
 TwoPlrProtection = False
 JeremiahProtection = False
 KrisProtection = False
 Yourstuck = False
 TwoPlrstuck = False
 Jeremiahstuck = False
 Krisstuck = False
 You = 50
 TwoPlr = 50
 Jeremiah = 50
 Kris = 50
 PlayerListNotYou = [TwoPlr,Jeremiah,Kris] 
 PlayerListNotTwoPlr = [You,Jeremiah,Kris]
 PlayerListNotJeremiah = [You,TwoPlr,Kris]
 PlayerListNotKris = [You,TwoPlr,Jeremiah]
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
   print('''1 - It's a board game. 
You cross through the trail to win.''') 
   PETC_function()
   print('''2 - There are 50 tiles on the trail''')
   PETC_function()
   print('''3 - You roll an imaginary dice that I made to move
(You do this by pressing enter)''')
   PETC_function()
   print('''4 - Whenever you land on an even tile (tile 92 for example), 
You are given a chance to test your luck.
When you take the chance to test your luck,
you have a chance of getting boosts or traps.
You will be introduced to that later.''')
   PETC_function()
   print('''5 - The farther you go/the more tiles you walk through on the trail,
the higher the chances of you encountering a trap when testing luck
However, you can avoid this but not testing your luck.''')
   PETC_function()
   print('''6 - While you can play safe by not testing your luck throughout the board game,
Other players can use weapons against you when having good luck''')
   PETC_function()
   print('''7 - First player to cross through the entire trail of the board game wins!''')
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
 Youwon = False
 TwoPlrwon = False
 Jeremiahwon = False
 Kriswon = False
 TwoPlrprt = '''
1 - {0} ({1} remaining tiles)'''
 Jeremiahprt = '''
2 - Jeremiah ({} remaining tiles)'''
 Krisprt = '''
3 - Kris ({} remaining tiles)'''
 Yournrt = '''
{0} - {1} remaining tiles'''
 TwoPlrnrt = '''
TwoPlr - {} remaining tiles'''
 Jeremiahnrt = '''
Jeremiah - {} remaining tiles'''
 Krisnrt = '''
Kris - {} remaining tiles'''
 def ChsPlr_function():
  time.sleep(0.5)
  if TwoPlrrt > 0:
   print(TwoPlrprt.format(PlayerTwoName,TwoPlrrt))
  elif TwoPlrrt <= 0:
   print('''
TwoPlr '''+Blue+'''has escaped the board!'''+reset)
  time.sleep(0.25)
  if Jeremiahrt > 0:
   print(Jeremiahprt.format(Jeremiahrt))
  elif Jeremiahrt <= 0:
   print(Blue+'''
Jeremiah has escaped the board!'''+reset)
  time.sleep(0.25)
  if Krisrt > 0:
   print(Krisprt.format(Krisrt))
  elif Krisrt <= 0:
   print(Blue+'''
Kris has escaped the board!'''+reset)
  time.sleep(0.25)
  PNTC_function()
 def Progress_function():
  print("Progress of all players:")
  time.sleep(0.5)
  if Yourrt <= 0:
   print(Blue+'''
You have escaped the board!'''+reset)
  elif Yourrt > 0:
   print(Yournrt.format(Yourrt))
  time.sleep(0.25)
  if TwoPlrrt <= 0:
   print(Blue+'''
TwoPlr has escaped the board!'''+reset)
  elif TwoPlrrt > 0:
   print(TwoPlrnrt.format(TwoPlrrt))
  time.sleep(0.25)
  if Jeremiahrt <= 0:
   print(Blue+'''
Jeremiah has escaped the board!'''+reset)
  elif Jeremiahrt > 0:
   print(Jeremiahnrt.format(Jeremiahrt))
  time.sleep(0.25)
  if Krisrt <= 0:
   print(Blue+'''
Kris has escaped the board!'''+reset)
  elif Krisrt > 0:
   print(Krisnrt.format(Krisrt))
  time.sleep(0.25)
  PETC_function()
 while TwoPlrrt > 0 and Yourrt > 0:
  Yourturn = True
  if Yourstuck == True:
   print(Red+"You are stuck so you cannot move."+reset)
   PETC_function()
   Yourstuck = False
   Yourturn = False
  elif Yourstuck == False:
   print("Your turn!")
   time.sleep(0.5)
   print("1 - Roll dice")
   time.sleep(0.25)
   print("2 - Check progress of players")
   time.sleep(0.25)
   NumChoiceWithQuit()
   try:
    Yourgo = int(input(""))
   except:
    InvalidInput()
    continue
   if Yourgo != 1 and Yourgo != 2:
    InvalidInput()
    continue
   elif Yourgo == 2:
    Progress_function()
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
    elif Quitchoice == 2:
     print('''
Alrighty then!''')
     time.sleep(1)
     break
   if Quitchoice == 2:
    continue
   Yourdiceroll1 = random.randrange(1,7)
   Yourdiceroll2 = random.randrange(1,7)
   Yourdicerollresults = "It looks like you rolled a {} and a {}, so you move {} tiles forward"
   print(Yourdicerollresults.format(Yourdiceroll1,Yourdiceroll2,Yourdiceroll1 + Yourdiceroll2))
   Yourtilesadded = Yourdiceroll1 + Yourdiceroll2
   Yourrt = Yourrt - Yourtilesadded
   You = 100 - Yourrt
   Yournt = "You have {} tiles remaining on the board"
   print(Yournt.format(Yourrt))
   time.sleep(1)
   if Yourrt % 2 == 0 and Yourrt > 0:
    while Yourturn == True:
     print('''It looks like you stepped on an even tile on the board,''')
     time.sleep(1)
     print('''Want to test your luck?''')
     YesOrNo()
     try:
      Yourlucktest = int(input(""))
     except: 
      InvalidInput()
      continue
     if Yourlucktest == 1:
      Yourrandomnumber = random.randrange(1,101)
      if Yourrandomnumber > Yourrt:
       Yourturn = False
       print(Red+"Uh Oh! It looks like you encountered a trap"+reset)
       if YourProtection == True and Youwon == False:
        print(Blue+"But you have protection so nothing will happen to you"+reset)
        YourProtection = False
        Yourturn = False
       elif YourProtection == False and Youwon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like you won't be going anywhere for one round")
         Yourstuck = True
         time.sleep(1)
         Yourturn = False
        elif Trapchoice == 2:
         print("You're going back to where you just came from!")
         time.sleep(1)
         Yourrt = Yourrt + Yourtilesadded
         Yournt = "You have {} tiles remaining on the board now"
         print(Yournt.format(Yourrt))
         time.sleep(1)
         Yourturn = False
        elif Trapchoice == 3:
         print('''You gave your luck away to one of your opponents!''')
         RandomNotYou = random.choice(PlayerListNotYou[0:3])
         if RandomNotYou == PlayerListNotYou[0]:
          TwoPlrLuckChoice = random.randrange(1,5)
          if TwoPlrLuckChoice == 1:
           print("{0} moves your tiles now!")
           time.sleep(1)
           TwoPlrrt = TwoPlrrt - Yourtilesadded
           TwoPlrnt = "{0} has {} tiles remaining on the board now"
           time.sleep(1)
           print(TwoPlrnt.format(TwoPlrrt))
           TwoPlrturn = False
          elif TwoPlrLuckChoice == 2:
           TwoPlrbc = True
           while TwoPlrbc == True:
            Randomnumber = random.randrange(1,101)
            if Randomnumber <= 90:
             TwoPlrblow = 1
            elif Randomnumber > 90:
             TwoPlrblow = 2
            print("{0} has been given the choice to blow someone away.")
            time.sleep(1)
            if TwoPlrblow == 1:
             TwoPlrblow = random.randrange(1,4)
             if TwoPlrblow == 1:
              print("{0} chose to blow you away!")
              time.sleep(1)
              if YourProtection == False and Youwon == False:
               Yourta = (100 - Yourrt)/2
               Yourtr = round(Yourta)
               PlayerBlown = Red+"You have been blown {} tiles away."+reset
               print(PlayerBlown.format(Yourta))
               time.sleep(1)
               Yourrt = Yourrt + Yourtr
               Yournt = "You have {} tiles remaining on the board now"
               print(Yournt.format(Yourrt))
               time.sleep(1)
               TwoPlrbc = False
               TwoPlrturn = False
              elif YourProtection == True and Youwon == False:
               print(Blue+"You have protection so nothing happened!"+reset)
               time.sleep(1)
               YourProtection = False
               TwoPlrbc = False
               TwoPlrturn = False
              elif Youwon == True:
                   print(yellow+"You have escaped the board, so {} will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrblow == 2:
              print("{0} chose to blow Jeremiah away!")
              time.sleep(1)
              if JeremiahProtection == False and Jeremiahwon == False:
               Jeremiahta = (100 - Jeremiahrt)/2
               Jeremiahtr = round(Jeremiahta)
               PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
               print(PlayerBlown.format(Jeremiahtr))
               time.sleep(1)
               Jeremiahrt = Jeremiahrt + Jeremiahtr
               Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
               print(Jeremiahnt.format(Jeremiahrt))
               time.sleep(1)
               TwoPlrbc = False
               TwoPlrturn = False
              elif JeremiahProtection == True and Jeremiahwon == False:
               print(Blue+"Jeremiah has protection so nothing happened!"+reset)
               time.sleep(1)
               JeremiahProtection = False
               TwoPlrbc = False
               TwoPlrturn = False
             elif TwoPlrblow != 1 and TwoPlrblow != 2:
              print("{0} chose to blow Kris away!")
              time.sleep(1)
              if KrisProtection == False and Kriswon == False:
               Krista = (100 - Krisrt)/2
               Kristr = round(Krista)
               PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
               print(PlayerBlown.format(Kristr))
               time.sleep(1)
               Krisrt = Krisrt + Kristr   
               Krisnt = "Kris has {} tiles remaining on the board now"
               print(Krisnt.format(Krisrt))
               time.sleep(1)
               TwoPlrbc = False
               TwoPlrturn = False
              elif KrisProtection == True and Kriswon == False:
               print(Blue+"Kris has protection so nothing happened!"+reset)
               time.sleep(1)
               KrisProtection = False
               TwoPlrbc = False
               TwoPlrturn = False
              elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
            elif TwoPlrblow != 1:
             print("{0} chose to not blow anyone away! how kind")
             time.sleep(1)
             TwoPlrbc = False
             TwoPlrturn = False
          elif TwoPlrLuckChoice == 3:
           print(Blue+"{0} is now protected from debuffs!"+reset)
           time.sleep(1)
           TwoPlrProtection = True
           TwoPlrturn = False
          elif TwoPlrLuckChoice == 4:
           TwoPlrsc = True
           Randomnumber = random.randrange(1,101)
           while TwoPlrsc == True:
            if Randomnumber <= 90:
             TwoPlrswap = 1
            elif Randomnumber > 90:
             TwoPlrswap = 2
            print("{0} has been given the choice to swap with someone!")
            time.sleep(1)
            if TwoPlrswap == 1:
             TwoPlrswap = random.randrange(1,4)
             if TwoPlrswap == 1:
              print("{0} chose to swap with you!")
              time.sleep(1)
              if YourProtection == False and Youwon == False:
               print(yellow+"{0} swapped with you"+reset)
               time.sleep(1)
               TwoPlroldtiles = TwoPlrrt
               TwoPlrrt = Yourrt
               Yourrt = TwoPlroldtiles
               PlayerSwapped = "{0} now has {} tiles remaining on the board and you have {} tiles remaining on the board."
               print(PlayerSwapped.format(TwoPlrrt,Yourrt))
               time.sleep(1)
               TwoPlrsc = False
               TwoPlrturn = False
              elif YourProtection == True and Youwon == False:
               print(Blue+"You have protection so nothing happened!"+reset)
               time.sleep(1)
               YourProtection = False
               TwoPlrsc = False
               TwoPlrturn = False
              elif Youwon == True:
               print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
               time.sleep(1)
               continue
             elif TwoPlrswap == 2:
              print("{0} chose to swap with Jeremiah!")
              time.sleep(1)
              if JeremiahProtection == False and Jeremiahwon == False:
               print(yellow+"{0} swapped with Jeremiah"+reset)
               time.sleep(1)
               TwoPlroldtiles = TwoPlrrt
               TwoPlrrt = Jeremiahrt
               Jeremiahrt = TwoPlroldtiles
               PlayerSwapped = "{0} now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
               print(PlayerSwapped.format(TwoPlrrt,Jeremiahrt))
               time.sleep(1)
               TwoPlrsc = False
               TwoPlrturn = False
              elif JeremiahProtection == True and Jeremiahwon == False:
               print(Blue+"Jeremiah has protection, so nothing happened"+reset)
               time.sleep(1)
               JeremiahProtection = False
               TwoPlrsc = False
               TwoPlrturn = False
              elif Jeremiahwon == True:
               print(yellow+"Jeremiah has escaped the board, so TwoPlr will rechoose."+reset)
               time.sleep(1)
               continue
             elif TwoPlrswap != 1 or TwoPlrswap != 2:
              print("{0} chose to swap with Kris!")
              time.sleep(1)
              if KrisProtection == False and Kriswon == False:
               print(yellow+"{0} swapped with Kris"+reset)
               time.sleep(1)
               Jeremiaholdtiles = Jeremiahrt
               Jeremiahrt = Krisrt
               Krisrt = Jeremiaholdtiles
               PlayerSwapped = "{0} now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
               print(PlayerSwapped.format(TwoPlrrt,Krisrt))
               time.sleep(1)
               TwoPlrsc = False
               TwoPlrturn = False
              elif KrisProtection == True and Kriswon == False:
               print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
               time.sleep(1)
               KrisProtection = False
               TwoPlrsc = False
               TwoPlrturn = False
              elif Kriswon == True:
               print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
               time.sleep(1)
               continue
            elif TwoPlrswap != 1:
             print("{0} would not like to swap, that's ok")
             time.sleep(1)
             TwoPlrsc = False
             TwoPlrturn = False
          Yourturn = False
         elif RandomNotYou == PlayerListNotYou[1]:
           JeremiahLuckChoice = random.randrange(1,5)
           if JeremiahLuckChoice == 1:
            print("Jeremiah moves your tiles now!")
            time.sleep(1)
            Jeremiahrt = Jeremiahrt - Yourtilesadded
            Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jeremiahnt.format(Jeremiahrt))
            Jeremiahturn = False
           elif JeremiahLuckChoice == 2:
            Jeremiahbc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahbc == True:
             if Randomnumber <= 90:
              Jeremiahblow = 1
             elif Randomnumber > 90:
              Jeremiahblow = 2
             print("Jeremiah has been given the choice to blow someone away.")
             time.sleep(1)
             if Jeremiahblow == 1:
              Jeremiahblow = random.randrange(1,4)
              if Jeremiahblow == 1:
               print("Jeremiah chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
              elif Jeremiahblow == 2:
               print("Jeremiah chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)         
                TwoPlrProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow != 1 and Jeremiahblow != 2:
               print("Jeremiah chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahblow != 1:
              print("Jeremiah chose to not blow anyone away! how kind")
              time.sleep(1)
              Jeremiahbc = False
              Jeremiahturn = False
           elif JeremiahLuckChoice == 3:
            print(Blue+"Jeremiah is now protected from debuffs!"+reset)
            time.sleep(1)
            JeremiahProtection = True
            Jeremiahturn = False
           elif JeremiahLuckChoice == 4:
            Jeremiahsc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahsc == True:
             if Randomnumber <= 90:
              Jeremiahswap = 1
             elif Randomnumber > 90:
              Jeremiahswap = 2
             print("Jeremiah has been given the choice to swap with someone!")
             time.sleep(1)
             if Jeremiahswap == 1:
              Jeremiahswap = random.randrange(1,4)
              if Jeremiahswap == 1:
               print("Jeremiah chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jeremiah swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Yourrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap == 2:
               print("Jeremiah chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Jeremiah swapped with TwoPlr"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = TwoPlrrt
                TwoPlrrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,TwoPlrrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap != 1 or Jeremiahswap != 2:
               print("Jeremiah chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jeremiah swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Krisrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahswap != 1:
              print("Jeremiah would not like to swap, that's ok")
              time.sleep(1)
              Jeremiahsc = False
              Jeremiahturn = False
           Yourturn = False
         elif RandomNotYou == PlayerListNotYou[2]:
           KrisLuckChoice = random.randrange(1,5)
           if KrisLuckChoice == 1:
            print("Kris moves your tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Yourtilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
           elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)
                TwoPlrProtection = False
                Krisbc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
           elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
           elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Kris swapped with TwoPlr"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = TwoPlrrt
                TwoPlrrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,TwoPlrrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Krissc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
           Yourturn = False
      elif Yourrandomnumber <= Yourrt:
       Yourturn = False
       print(Blue+"Lucky you! You obtained a boost!"+reset)
       YourLuckchoice = random.randrange(1,5)
       if YourLuckchoice == 1:
         print("You move double tiles now!")
         time.sleep(1)
         Yourrt = Yourrt - Yourtilesadded
         Yournt = "You have {} tiles remaining on the board now"
         print(Yournt.format(Yourrt))
         time.sleep(1)
         Yourturn = False
       elif YourLuckchoice == 2:
         Yourbc = True
         while Yourbc == True:
          print('''You were granted the ability to blow a player away, proceed?''')
          YORBG_function()
          try:
           Yourblow = int(input(""))
          except:
           InvalidInput()
           continue
          if Yourblow == 1:
           while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   TwoPlrta = (100 - TwoPlrrt)/2
                   TwoPlrtr = round(TwoPlrta)
                   PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                   print(PlayerBlown.format(TwoPlrtr))
                   TwoPlrrt = TwoPlrrt + TwoPlrtr
                   TwoPlrnt = "{0} has {} tiles remaining on the board now"
                   print(TwoPlrnt.format(TwoPlrrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
          elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
          elif Yourblow == 3:
                 Progress_function()
                 continue
          else:
                 InvalidInput()
                 continue
       elif YourLuckchoice == 3:
         print(Blue+"You are now protected from debuffs!"+reset)
         time.sleep(1)
         YourProtection = True
         Yourturn = False
       elif YourLuckchoice == 4:
         Yoursc = True
         while Yoursc == True:
             print("You were granted the ability to swap with another player, proceed?")
             YORBG_function()
             try:
               Yourswap = int(input(""))
             except:
               InvalidInput()
               continue
             if Yourswap == 1:
              while Yoursc == True:
               print("Choose the player that you want to swap with:")
               ChsPlr_function()
               try:
                Yourswap = int(input(""))
               except:
                InvalidInput()
                continue
               if Yourswap == 1:
                if TwoPlrProtection == False and TwoPlrwon == False:
                 print(yellow+"You swapped with TwoPlr"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = TwoPlrrt
                 TwoPlrrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,TwoPlrrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif TwoPlrProtection == True and TwoPlrwon == False:
                 print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                 TwoPlrProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               elif Yourswap == 2:
                if JeremiahProtection == False and Jeremiahwon == False:
                 print(yellow+"You swapped with Jeremiah"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Jeremiahrt
                 Jeremiahrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif JeremiahProtection == True and Jeremiahwon == False:
                 print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                 JeremiahProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
               elif Yourswap == 3:
                if KrisProtection == False and Kriswon == False:
                 print(yellow+"You swapped with Kris"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Krisrt
                 Krisrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Krisrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif KrisProtection == True and Kriswon == False:
                 print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                 KrisProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               else:
                InvalidInput()
                continue
             elif Yourswap == 2:
               print("Well that's ok")
               time.sleep(1)
               Yoursc = False
             elif Yourswap == 3:
               Progress_function()
             else:
              InvalidInput()
              continue    
       Yourturn = False
     elif Yourlucktest == 2:
      print("It looks like you chose to play safe, that's ok.")
      time.sleep(1)
      Yourturn = False
   elif Yourrt % 2 != 0:
    Yourturn = False
  if Yourrt <= 0:
   clearScreen()
   print(Blue+"You have successfully crossed the entire trail of the game so you win!"+reset)
   PETC_function()
   return "W"
  TwoPlrturn = True
  if TwoPlrstuck == True:
   print(Red+"{0} is stuck so he cannot move."+reset)
   time.sleep(1)
   TwoPlrstuck = False
   TwoPlrturn = False
  elif TwoPlrwon == True:
   print(Blue+"{0} has escaped the board!"+reset)
   time.sleep(1)
  elif TwoPlrstuck == False and TwoPlrrt > 0 and TwoPlrwon == False:
   print("{0}'s turn!")
   time.sleep(1)
   TwoPlrdiceroll1 = random.randrange(1,7)
   TwoPlrdiceroll2 = random.randrange(1,7)
   TwoPlrdicerollresults = "It looks like TwoPlr rolled a {0} and a {1}, so {2} moves {3} tiles forward"
   print(TwoPlrdicerollresults.format(TwoPlrdiceroll1,TwoPlrdiceroll2,PlayerTwoName,TwoPlrdiceroll1 + TwoPlrdiceroll2))
   TwoPlrtilesadded = TwoPlrdiceroll1 + TwoPlrdiceroll2
   TwoPlrrt = TwoPlrrt - TwoPlrtilesadded
   TwoPlrnt = "{0} has {} tiles remaining on the board"
   print(TwoPlrnt.format(TwoPlrrt))
   time.sleep(1)
   if TwoPlrrt % 2 == 0 and TwoPlrrt > 0:
    while TwoPlrturn == True:
     print('''It looks like TwoPlr stepped on an even tile on the board''')
     time.sleep(1)
     Randomnumber = random.randrange(1,101)
     if Randomnumber <= 75:
      TwoPlrlucktest = 1
     elif Randomnumber > 75:
      TwoPlrlucktest = 2
     if TwoPlrlucktest == 1:
      print("{0} wants to test his luck")
      time.sleep(1)
      TwoPlrrandomnumber = random.randrange(1,101)
      if TwoPlrrandomnumber > TwoPlrrt:
       TwoPlrturn = False
       print(Red+"Uh Oh! It looks like {} encountered a trap"+reset)
       time.sleep(1)
       if TwoPlrProtection == True and TwoPlrwon == False:
        print(Blue+"But {0} has protection so nothing will happen to TwoPlr "+reset)
        time.sleep(1)
        TwoPlrProtection == False and TwoPlrwon == False
        TwoPlrturn = False
       elif TwoPlrProtection == False and TwoPlrwon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like TwoPlr won't be going anywhere for one round")
         time.sleep(1)
         TwoPlrstuck = True
         TwoPlrturn = False
        elif Trapchoice == 2:
         print("{0} is going back to where he just came from!")
         time.sleep(1)
         TwoPlrrt = TwoPlrrt + TwoPlrtilesadded
         TwoPlrnt = "{0} has {} tiles remaining on the board now"
         time.sleep(1)
         print(TwoPlrnt.format(TwoPlrrt))
         TwoPlrturn = False
        elif Trapchoice == 3:
         print('''TwoPlr gave his luck away to one of his opponents!''')
         time.sleep(1)
         RandomNotTwoPlr = random.choice(PlayerListNotTwoPlr[0:3])
         if RandomNotTwoPlr == PlayerListNotTwoPlr[0]:
            YourLuckchoice = random.randrange(1,5)
            if YourLuckchoice == 1:
             print("You move TwoPlr's tiles now!")
             Yourrt = Yourrt - Yourtilesadded
             Yournt = "You have {} tiles remaining on the board now"
             print(Yournt.format(Yourrt))
             time.sleep(1)
             Yourturn = False
            elif YourLuckchoice == 2:
             Yourbc = True
             while Yourbc == True:
              print("You were granted the ability to blow a player away, proceed?")
              YORBG_function()
              try:
               Yourblow = int(input(""))
              except:
               InvalidInput()
               continue
              if Yourblow == 1:
               while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   TwoPlrta = (100 - TwoPlrrt)/2
                   TwoPlrtr = round(TwoPlrta)
                   PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                   print(PlayerBlown.format(TwoPlrtr))
                   TwoPlrrt = TwoPlrrt + TwoPlrtr
                   TwoPlrnt = "{0} has {} tiles remaining on the board now"
                   print(TwoPlrnt.format(TwoPlrrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
              elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
              elif Yourblow == 3:
                 Progress_function()
                 continue
              else:
                 InvalidInput()
                 continue
            elif YourLuckchoice == 3:
             print(Blue+"You are now protected from debuffs!"+reset)
             time.sleep(1)
             YourProtection = True
             Yourturn = False
            elif YourLuckchoice == 4:
             Yoursc = True
             while Yoursc == True:
               print("You were granted the ability to swap with another player, proceed?")
               YORBG_function()
               try:
                 Yourswap = int(input(""))
               except:
                 InvalidInput()
                 continue
               if Yourswap == 1:
                while Yoursc == True:
                 print("Choose the player that you want to swap with:")
                 ChsPlr_function()
                 try:
                  Yourswap = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourswap == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   print(yellow+"You swapped with TwoPlr"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = TwoPlrrt
                   TwoPlrrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,TwoPlrrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   print(yellow+"You swapped with Jeremiah"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jeremiahrt
                   Jeremiahrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                   JeremiahProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                 elif Yourswap == 3:
                  if KrisProtection == False and Kriswon == False:
                   print(yellow+"You swapped with Kris"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Krisrt
                   Krisrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Krisrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
               elif Yourswap == 2:
                 print("Well that's ok")
                 time.sleep(1)
                 Yoursc = False
               elif Yourswap == 3:
                 Progress_function()
               else:
                InvalidInput()
                continue
         elif RandomNotTwoPlr == PlayerListNotTwoPlr[1]:
            YourLuckchoice = random.randrange(1,5)
            if YourLuckchoice == 1:
             print("You move TwoPlr's tiles now!")
             Yourrt = Yourrt - Yourtilesadded
             Yournt = "You have {} tiles remaining on the board now"
             print(Yournt.format(Yourrt))
             time.sleep(1)
             Yourturn = False
            elif YourLuckchoice == 2:
             Yourbc = True
             while Yourbc == True:
              print("You were granted the ability to blow a player away, proceed?")
              YORBG_function()
              try:
               Yourblow = int(input(""))
              except:
               InvalidInput()
               continue
              if Yourblow == 1:
               while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   TwoPlrta = (100 - TwoPlrrt)/2
                   TwoPlrtr = round(TwoPlrta)
                   PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                   print(PlayerBlown.format(TwoPlrtr))
                   TwoPlrrt = TwoPlrrt + TwoPlrtr
                   TwoPlrnt = "{0} has {} tiles remaining on the board now"
                   print(TwoPlrnt.format(TwoPlrrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
              elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
              elif Yourblow == 3:
                 Progress_function()
                 continue
              else:
                 InvalidInput()
                 continue
            elif YourLuckchoice == 3:
             print(Blue+"You are now protected from debuffs!"+reset)
             time.sleep(1)
             YourProtection = True
             Yourturn = False
            elif YourLuckchoice == 4:
             Yoursc = True
             while Yoursc == True:
               print("You were granted the ability to swap with another player, proceed?")
               YORBG_function()
               try:
                 Yourswap = int(input(""))
               except:
                 InvalidInput()
                 continue
               if Yourswap == 1:
                while Yoursc == True:
                 print("Choose the player that you want to swap with:")
                 ChsPlr_function()
                 try:
                  Yourswap = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourswap == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   print(yellow+"You swapped with TwoPlr"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = TwoPlrrt
                   TwoPlrrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,TwoPlrrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   print(yellow+"You swapped with Jeremiah"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jeremiahrt
                   Jeremiahrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                   JeremiahProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                 elif Yourswap == 3:
                  if KrisProtection == False and Kriswon == False:
                   print(yellow+"You swapped with Kris"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Krisrt
                   Krisrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Krisrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
               elif Yourswap == 2:
                 print("Well that's ok")
                 time.sleep(1)
                 Yoursc = False
               elif Yourswap == 3:
                 Progress_function()
               else:
                InvalidInput()
                continue
         elif RandomNotTwoPlr == PlayerListNotTwoPlr[2]:
           KrisLuckChoice = random.randrange(1,5)
           if KrisLuckChoice == 1:
            print("Kris moves TwoPlr's tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - TwoPlrtilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
           elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)
                TwoPlrProtection = False
                Krisbc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr 
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
           elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
           elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Kris swapped with TwoPlr"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = TwoPlrrt
                TwoPlrrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,TwoPlrrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Krissc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
      elif TwoPlrrandomnumber <= TwoPlrrt:
       TwoPlrturn = False
       print(Blue+"Lucky TwoPlr! TwoPlr obtained a boost!"+reset)
       time.sleep(1)
       TwoPlrLuckChoice = random.randrange(1,5)
       if TwoPlrLuckChoice == 1:
            print("{0} moves double tiles now!")
            time.sleep(1)
            TwoPlrrt = TwoPlrrt - TwoPlrtilesadded
            TwoPlrnt = "{0} has {} tiles remaining on the board now"
            time.sleep(1)
            print(TwoPlrnt.format(TwoPlrrt))
            TwoPlrturn = False
       elif TwoPlrLuckChoice == 2:
            TwoPlrbc = True
            Randomnumber = random.randrange(1,101)
            while TwoPlrbc == True:
             if Randomnumber <= 90:
              TwoPlrblow = 1
             elif Randomnumber > 90:
              TwoPlrblow = 2
             print("{0} has been given the choice to blow someone away.")
             time.sleep(1)
             if TwoPlrblow == 1:
              TwoPlrblow = random.randrange(1,4)
              if TwoPlrblow == 1:
               print("{0} chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrblow == 2:
               print("{0} chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
              elif TwoPlrblow != 1 and TwoPlrblow != 2:
               print("{0} chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrblow != 1:
              print("{0} chose to not blow anyone away! how kind")
              time.sleep(1)
              TwoPlrbc = False
              TwoPlrturn = False
       elif TwoPlrLuckChoice == 3:
            print(Blue+"{0} is now protected from debuffs!"+reset)
            time.sleep(1)
            TwoPlrProtection = True
            TwoPlrturn = False
       elif TwoPlrLuckChoice == 4:
            TwoPlrsc = True
            Randomnumber = random.randrange(1,101)
            while TwoPlrsc == True:
             if Randomnumber <= 90:
              TwoPlrswap = 1
             elif Randomnumber > 90:
              TwoPlrswap = 2
             print("{0} has been given the choice to swap with someone!")
             time.sleep(1)
             if TwoPlrswap == 1:
              TwoPlrswap = random.randrange(1,4)
              if TwoPlrswap == 1:
               print("{0} chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"{0} swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                TwoPlrrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Yourrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrswap == 2:
               print("{0} chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"{0} swapped with Jeremiah"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                TwoPlrrt = Jeremiahrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Jeremiahrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                time.sleep(1)
                JeremiahProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
              elif TwoPlrswap != 1 or TwoPlrswap != 2:
               print("{0} chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"{0} swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Krisrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrswap != 1:
              print("{0} would not like to swap, that's ok")
              time.sleep(1)
              TwoPlrsc = False
              TwoPlrturn = False
     elif TwoPlrlucktest == 2:
      print("It looks like TwoPlr chose to play safe, that's ok.")
      time.sleep(1)
      TwoPlrturn = False
   elif TwoPlrrt % 2 != 0:
    TwoPlrturn = False 
  if TwoPlrrt <= 0 and TwoPlrwon == False:
   clearScreen()
   print(Blue+"{0} has successfully crossed the entire trail of the game!"+reset)
   PETC_function()
   PlayersLeft = PlayersLeft - 1
   TwoPlrwon = True
  Jeremiahturn = True
  if Jeremiahstuck == True:
   print(Red+"Jeremiah is stuck so he cannot move."+reset)
   time.sleep(1)
   Jeremiahstuck = False
   Jeremiahturn = False
  elif Jeremiahwon == True:
   print(Blue+"Jeremiah has escaped the board!"+reset)
   time.sleep(1)
  elif Jeremiahstuck == False and Jeremiahrt > 0 and Jeremiahwon == False:
   print("Jeremiah's turn!")
   time.sleep(1)
   Jeremiahdiceroll1 = random.randrange(1,7)
   Jeremiahdiceroll2 = random.randrange(1,7)
   Jeremiahdicerollresults = "It looks like Jeremiah rolled a {} and a {}, so Jeremiah moves {} tiles forward"
   print(Jeremiahdicerollresults.format(Jeremiahdiceroll1,Jeremiahdiceroll2,Jeremiahdiceroll1 + Jeremiahdiceroll2))
   Jeremiahtilesadded = Jeremiahdiceroll1 + Jeremiahdiceroll2
   Jeremiahrt = Jeremiahrt - Jeremiahtilesadded
   Jeremiahnt = "Jeremiah has {} tiles remaining on the board"
   print(Jeremiahnt.format(Jeremiahrt))
   time.sleep(1)
   if Jeremiahrt % 2 == 0 and Jeremiahrt > 0:
    while Jeremiahturn == True:
     print('''It looks like Jeremiah stepped on an even tile on the board''')
     time.sleep(1)
     Randomnumber = random.randrange(1,101)
     if Randomnumber <= 75:
      Jeremiahlucktest = 1
     elif Randomnumber > 75:
      Jeremiahlucktest = 2
     if Jeremiahlucktest == 1:
      print("Jeremiah wants to test his luck")
      time.sleep(1)
      Jeremiahrandomnumber = random.randrange(1,101)
      if Jeremiahrandomnumber > Jeremiahrt:
       Jeremiahturn = False
       print(Red+"Uh Oh! It looks like Jeremiah encountered a trap"+reset)
       time.sleep(1)
       if JeremiahProtection == True and Jeremiahwon == False:
        print(Blue+"But Jeremiah has protection so nothing will happen to Jeremiah"+reset)
        time.sleep(1)
        Jeremiahturn = False
        JeremiahProtection = False
       elif JeremiahProtection == False and Jeremiahwon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like Jeremiah won't be going anywhere for one round")
         time.sleep(1)
         Jeremiahstuck = True
         Jeremiahturn = False
        elif Trapchoice == 2:
         print("Jeremiah is going back to where he just came from!")
         time.sleep(1)
         Jeremiahrt = Jeremiahrt + Jeremiahtilesadded
         Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
         time.sleep(1)
         print(Jeremiahnt.format(Jeremiahrt))
         Jeremiahturn = False
        elif Trapchoice == 3:
         print('''Jeremiah gave his luck away to one of his opponents!''')
         time.sleep(1)
         RandomNotJeremiah = random.choice(PlayerListNotJeremiah[0:3])
         if RandomNotJeremiah == PlayerListNotJeremiah[0]:
          YourLuckchoice = random.randrange(1,5)
          if YourLuckchoice == 1:
             print("You move Jeremiah's tiles now!")
             Yourrt = Yourrt - Jeremiahtilesadded
             Yournt = "You have {} tiles remaining on the board now"
             print(Yournt.format(Yourrt))
             time.sleep(1)
             Yourturn = False
          elif YourLuckchoice == 2:
             Yourbc = True
             while Yourbc == True:
              print("You were granted the ability to blow a player away, proceed?")
              YORBG_function()
              try:
               Yourblow = int(input(""))
              except:
               InvalidInput()
               continue
              if Yourblow == 1:
               while Yourbc == True:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   TwoPlrta = (100 - TwoPlrrt)/2
                   TwoPlrtr = round(TwoPlrta)
                   PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                   print(PlayerBlown.format(TwoPlrtr))
                   TwoPlrrt = TwoPlrrt + TwoPlrtr
                   TwoPlrnt = "{0} has {} tiles remaining on the board now"
                   print(TwoPlrnt.format(TwoPlrrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing  happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
              elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
              elif Yourblow == 3:
                 Progress_function()
                 continue
              else:
                 InvalidInput()
                 continue
          elif YourLuckchoice == 3:
             print(Blue+"You are now protected from debuffs!"+reset)
             time.sleep(1)
             YourProtection = True
             Yourturn = False
          elif YourLuckchoice == 4:
             Yoursc = True
             while Yoursc == True:
               print("You were granted the ability to swap with another player, proceed?")
               YORBG_function()
               try:
                 Yourswap = int(input(""))
               except:
                 InvalidInput()
                 continue
               if Yourswap == 1:
                while Yoursc == True:
                 print("Choose the player that you want to swap with:")
                 ChsPlr_function()
                 try:
                  Yourswap = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourswap == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   print(yellow+"You swapped with TwoPlr"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = TwoPlrrt
                   TwoPlrrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,TwoPlrrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   print(yellow+"You swapped with Jeremiah"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Jeremiahrt
                   Jeremiahrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                   JeremiahProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourswap == 3:
                  if KrisProtection == False and Kriswon == False:
                   print(yellow+"You swapped with Kris"+reset)
                   time.sleep(1)
                   Youroldtiles = Yourrt
                   Yourrt = Krisrt
                   Krisrt = Youroldtiles
                   PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                   print(PlayerSwapped.format(Yourrt,Krisrt))
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yoursc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
               elif Yourswap == 2:
                 print("Well that's ok")
                 time.sleep(1)
                 Yoursc = False
               elif Yourswap == 3:
                 Progress_function()
               else:
                InvalidInput()
                continue
         elif RandomNotJeremiah == PlayerListNotJeremiah[1]:
           TwoPlrLuckChoice = random.randrange(1,5)
           if TwoPlrLuckChoice == 1:
            print("{0} moves Jeremiah's tiles now!")
            time.sleep(1)
            TwoPlrrt = TwoPlrrt - Jeremiahtilesadded
            TwoPlrnt = "{0} has {} tiles remaining on the board now"
            time.sleep(1)
            print(TwoPlrnt.format(TwoPlrrt))
            TwoPlrturn = False
           elif TwoPlrLuckChoice == 2:
            TwoPlrbc = True
            Randomnumber = random.randrange(1,101)
            while TwoPlrbc == True:
             if Randomnumber <= 90:
              TwoPlrblow = 1
             elif Randomnumber > 90:
              TwoPlrblow = 2
             print("{0} has been given the choice to blow someone away.")
             time.sleep(1)
             if TwoPlrblow == 1:
              TwoPlrblow = random.randrange(1,4)
              if TwoPlrblow == 1:
               print("{0} chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2 
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrblow == 2:
               print("{0} chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrblow != 1 and TwoPlrblow != 2:
               print("{0} chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrblow != 1:
              print("{0} chose to not blow anyone away! how kind")
              time.sleep(1)
              TwoPlrbc = False
              TwoPlrturn = False
           elif TwoPlrLuckChoice == 3:
            print(Blue+"{0} is now protected from debuffs!"+reset)
            time.sleep(1)
            TwoPlrProtection = True
            TwoPlrturn = False
           elif TwoPlrLuckChoice == 4:
            TwoPlrsc = True
            Randomnumber = random.randrange(1,101)
            while TwoPlrsc == True:
             if Randomnumber <= 90:
              TwoPlrswap = 1
             elif Randomnumber > 90:
              TwoPlrswap = 2
             print("{0} has been given the choice to swap with someone!")
             time.sleep(1)
             if TwoPlrswap == 1:
              TwoPlrswap = random.randrange(1,4)
              if TwoPlrswap == 1:
               print("{0} chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"{0} swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                TwoPlrrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Yourrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrswap == 2:
               print("{0} chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"{0} swapped with Jeremiah"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                TwoPlrrt = Jeremiahrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Jeremiahrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                time.sleep(1)
                JeremiahProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrswap != 1 or TwoPlrswap != 2:
               print("{0} chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"{0} swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Krisrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrswap != 1:
              print("{0} would not like to swap, that's ok")
              time.sleep(1)
              TwoPlrsc = False
              TwoPlrturn = False
         elif RandomNotJeremiah == PlayerListNotJeremiah[2]:
           KrisLuckChoice = random.randrange(1,5)
           if KrisLuckChoice == 1:
            print("Kris moves Jeremiah's tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Jeremiahtilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
           elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)
                TwoPlrProtection = False
                Krisbc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr 
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
           elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
           elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Kris swapped with TwoPlr"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = TwoPlrrt
                TwoPlrrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,TwoPlrrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Krissc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
      elif Jeremiahrandomnumber <= Jeremiahrt:
       Jeremiahturn = False
       print(Blue+"Lucky Jeremiah! Jeremiah obtained a boost!"+reset)
       time.sleep(1)
       JeremiahLuckChoice = random.randrange(1,5)
       if JeremiahLuckChoice == 1:
            print("Jeremiah moves double tiles now!")
            time.sleep(1)
            Jeremiahrt = Jeremiahrt - Jeremiahtilesadded
            Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jeremiahnt.format(Jeremiahrt))
            Jeremiahturn = False
       elif JeremiahLuckChoice == 2:
            Jeremiahbc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahbc == True:
             if Randomnumber <= 90:
              Jeremiahblow = 1
             elif Randomnumber > 90:
              Jeremiahblow = 2
             print("Jeremiah has been given the choice to blow someone away.")
             time.sleep(1)
             if Jeremiahblow == 1:
              Jeremiahblow = random.randrange(1,4)
              if Jeremiahblow == 1:
               print("Jeremiah chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow == 2:
               print("Jeremiah chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)         
                TwoPlrProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow != 1 and Jeremiahblow != 2:
               print("Jeremiah chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Krista))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahblow != 1:
              print("Jeremiah chose to not blow anyone away! how kind")
              time.sleep(1)
              Jeremiahbc = False
              Jeremiahturn = False
       elif JeremiahLuckChoice == 3:
            print(Blue+"Jeremiah is now protected from debuffs!"+reset)
            time.sleep(1)
            JeremiahProtection = True
            Jeremiahturn = False
       elif JeremiahLuckChoice == 4:
            Jeremiahsc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahsc == True:
             if Randomnumber <= 90:
              Jeremiahswap = 1
             elif Randomnumber > 90:
              Jeremiahswap = 2
             print("Jeremiah has been given the choice to swap with someone!")
             time.sleep(1)
             if Jeremiahswap == 1:
              Jeremiahswap = random.randrange(1,4)
              if Jeremiahswap == 1:
               print("Jeremiah chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jeremiah swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Yourrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap == 2:
               print("Jeremiah chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Jeremiah swapped with TwoPlr"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = TwoPlrrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,TwoPlrrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap != 1 or Jeremiahswap != 2:
               print("Jeremiah chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jeremiah swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Krisrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahswap != 1:
               print("Jeremiah would not like to swap, that's ok")
               time.sleep(1)
               Jeremiahsc = False
               Jeremiahturn = False
     elif Jeremiahlucktest == 2:
      print("It looks like Jeremiah chose to play safe, that's ok.")
      time.sleep(1)
      Jeremiahturn = False
   elif Jeremiahrt % 2 != 0:
    Jeremiahturn = False
  if Jeremiahrt <= 0 and Jeremiahwon == False:
   clearScreen()
   print(Blue+"Jeremiah has successfully crossed the entire trail of the game!"+reset)
   PETC_function()
   PlayersLeft = PlayersLeft - 1
   Jeremiahwon = True
  Kristurn = True
  if Krisstuck == True:
   print(Red+"Kris is stuck so he cannot move."+reset)
   time.sleep(1)
   Krisstuck = False
   Kristurn = False
  elif Kriswon == True:
   print(Blue+"Kris has escaped the board!"+reset)
   time.sleep(1)
  elif Krisstuck == False and Krisrt > 0 and Kriswon == False:
   print("Kris's turn!")
   time.sleep(1)
   Krisdiceroll1 = random.randrange(1,7)
   Krisdiceroll2 = random.randrange(1,7)
   Krisdicerollresults = "It looks like Kris rolled a {} and a {}, so Kris moves {} tiles forward"
   print(Krisdicerollresults.format(Krisdiceroll1,Krisdiceroll2,Krisdiceroll1 + Krisdiceroll2))
   Kristilesadded = Krisdiceroll1 + Krisdiceroll2
   Krisrt = Krisrt - Kristilesadded
   Krisnt = "Kris has {} tiles remaining on the board"
   print(Krisnt.format(Krisrt))
   time.sleep(1)
   if Krisrt % 2 == 0 and Krisrt > 0:
    while Kristurn == True:
     print('''It looks like Kris stepped on an even tile on the board''')
     time.sleep(1)
     Randomnumber = random.randrange(1,101)
     if Randomnumber <= 75:
      Krislucktest = 1
     elif Randomnumber > 75:
      Krislucktest = 2
     if Krislucktest == 1:
      print("Kris wants to test his luck")
      time.sleep(1)
      Krisrandomnumber = random.randrange(1,101)
      if Krisrandomnumber > Krisrt:
       Kristurn = False
       print(Red+"Uh Oh! It looks like Kris encountered a trap"+reset)
       time.sleep(1)
       if KrisProtection == True and Kriswon == False:
        print(Blue+"But Kris has protection so nothing will happen to Kris "+reset)
        KrisProtection = False
        time.sleep(1)
        Kristurn = False
       elif KrisProtection == False and Kriswon == False: 
        Trapchoice = random.randrange(1,4)
        if Trapchoice == 1:
         print("Looks like Kris won't be going anywhere for one round")
         time.sleep(1)
         Krisstuck = True
         Kristurn = False
        elif Trapchoice == 2:
         print("Kris is going back to where he just came from!")
         time.sleep(1)
         Krisrt = Krisrt + Kristilesadded
         Krisnt = "Kris has {} tiles remaining on the board now"
         time.sleep(1)
         print(Krisnt.format(Krisrt))
         Kristurn = False
        elif Trapchoice == 3:
         print('''Kris gave his luck away to one of his opponents!''')
         time.sleep(1)
         RandomNotKris = random.choice(PlayerListNotKris[0:3])
         if RandomNotKris == PlayerListNotKris[0]:
          YourLuckchoice = random.randrange(1,5)
          if YourLuckchoice == 1:
           print("You move Kris's tiles now!")
           Yourrt = Yourrt - Kristilesadded
           Yournt = "You have {} tiles remaining on the board now"
           print(Yournt.format(Yourrt))
           time.sleep(1)
           Yourturn = False
          elif YourLuckchoice == 2:
            Yourbc = True
            while Yourbc == True:
                print('''You were granted the ability to blow a player away, proceed?''')
                YORBG_function()
                try:
                  Yourblow = int(input(""))
                except:
                  InvalidInput()
                  continue
                if Yourblow == 1:
                 print("Choose the player that you want to blow away:")
                 ChsPlr_function()
                 try:
                  Yourblow = int(input(""))
                 except:
                  InvalidInput()
                  continue
                 if Yourblow == 1:
                  if TwoPlrProtection == False and TwoPlrwon == False:
                   TwoPlrta = (100 - TwoPlrrt)/2
                   TwoPlrtr = round(TwoPlrta)
                   PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                   print(PlayerBlown.format(TwoPlrtr))
                   TwoPlrrt = TwoPlrrt + TwoPlrtr
                   TwoPlrnt = "{0} has {} tiles remaining on the board now"
                   print(TwoPlrnt.format(TwoPlrrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrProtection == True and TwoPlrwon == False:
                   print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                   TwoPlrProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 2:
                  if JeremiahProtection == False and Jeremiahwon == False:
                   Jeremiahta = (100 - Jeremiahrt)/2
                   Jeremiahtr = round(Jeremiahta)
                   PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Jeremiahtr))
                   Jeremiahrt = Jeremiahrt + Jeremiahtr
                   Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                   print(Jeremiahnt.format(Jeremiahrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif JeremiahProtection == True and Jeremiahwon == False:
                   print("Jeremiah is protected so nothing happened!")
                   JeremiahProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 elif Yourblow == 3:
                  if KrisProtection == False and Kriswon == False:
                   Krista = (100 - Krisrt)/2
                   Kristr = round(Krista)
                   PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                   print(PlayerBlown.format(Kristr))
                   Krisrt = Krisrt + Kristr   
                   Krisnt = "Kris has {} tiles remaining on the board now"
                   print(Krisnt.format(Krisrt))
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif KrisProtection == True and Kriswon == False:
                   print(Blue+"Kris has protection so nothing happened!"+reset)
                   KrisProtection = False
                   time.sleep(1)
                   Yourbc = False
                   Yourturn = False
                  elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
                 else:
                  InvalidInput()
                  continue
                elif Yourblow == 2:
                 print("Ah you're so kind")
                 time.sleep(1)
                 Yourbc = False
                 Yourturn = False
                elif Yourblow == 3:
                 Progress_function()
                else:
                 InvalidInput()
                 continue
          elif YourLuckchoice == 3:
            print(Blue+"You are now protected from debuffs!"+reset)
            time.sleep(1)
            YourProtection = True
            Yourturn = False
          elif YourLuckchoice == 4:
            Yoursc = True
            while Yoursc == True:
             print("You were granted the ability to swap with another player, proceed?")
             YORBG_function()
             try:
               Yourswap = int(input(""))
             except:
               InvalidInput()
               continue
             if Yourswap == 1:
              while Yoursc == True:
               print("Choose the player that you want to swap with:")
               ChsPlr_function()
               try:
                Yourswap = int(input(""))
               except:
                InvalidInput()
                continue
               if Yourswap == 1:
                if TwoPlrProtection == False and TwoPlrwon == False:
                 print(yellow+"You swapped with TwoPlr"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = TwoPlrrt
                 TwoPlrrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,TwoPlrrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif TwoPlrProtection == True and TwoPlrwon == False:
                 print(Blue+Blue+"{0} has protection so nothing happened!"+reset)
                 TwoPlrProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               elif Yourswap == 2:
                if JeremiahProtection == False and Jeremiahwon == False:
                 print(yellow+"You swapped with Jeremiah"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Jeremiahrt
                 Jeremiahrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Jeremiahrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif JeremiahProtection == True and Jeremiahwon == False:
                 print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                 JeremiahProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               elif Yourswap == 3:
                if KrisProtection == False and Kriswon == False:
                 print(yellow+"You swapped with Kris"+reset)
                 time.sleep(1)
                 Youroldtiles = Yourrt
                 Yourrt = Krisrt
                 Krisrt = Youroldtiles
                 PlayerSwapped = "You now have {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                 print(PlayerSwapped.format(Yourrt,Krisrt))
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif KrisProtection == True and Kriswon == False:
                 print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                 KrisProtection = False
                 time.sleep(1)
                 Yoursc = False
                 Yourturn = False
                elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so you will rechoose."+reset)
                   time.sleep(1)
                   continue
               else:
                InvalidInput()
                continue
             elif Yourswap == 2:
               print("Well that's ok")
               time.sleep(1)
               Yoursc = False
             elif Yourswap == 3:
               Progress_function()
             else:
              InvalidInput()
              continue
         elif RandomNotKris == PlayerListNotKris[1]:
           TwoPlrLuckChoice = random.randrange(1,5)
           if TwoPlrLuckChoice == 1:
            print("{0} moves Kris's tiles now!")
            time.sleep(1)
            TwoPlrrt = TwoPlrrt - Kristilesadded
            TwoPlrnt = "{0} has {} tiles remaining on the board now"
            time.sleep(1)
            print(TwoPlrnt.format(TwoPlrrt))
            TwoPlrturn = False
           elif TwoPlrLuckChoice == 2:
            TwoPlrbc = True
            Randomnumber = random.randrange(1,101)
            while TwoPlrbc == True:
             if Randomnumber <= 90:
              TwoPlrblow = 1
             elif Randomnumber > 90:
              TwoPlrblow = 2
             print("{0} has been given the choice to blow someone away.")
             time.sleep(1)
             if TwoPlrblow == 1:
              TwoPlrblow = random.randrange(1,4)
              if TwoPlrblow == 1:
               print("{0} chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrblow == 2:
               print("{0} chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrblow != 1 and TwoPlrblow != 2:
               print("{0} chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                TwoPlrbc = False
                TwoPlrturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                TwoPlrbc = False
                TwoPlrturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrblow != 1:
              print("{0} chose to not blow anyone away! how kind")
              time.sleep(1)
              TwoPlrbc = False
              TwoPlrturn = False
           elif TwoPlrLuckChoice == 3:
            print(Blue+"{0} is now protected from debuffs!"+reset)
            time.sleep(1)
            TwoPlrProtection = True
            TwoPlrturn = False
           elif TwoPlrLuckChoice == 4:
            TwoPlrsc = True
            Randomnumber = random.randrange(1,101)
            while TwoPlrsc == True:
             if Randomnumber <= 90:
              TwoPlrswap = 1
             elif Randomnumber > 90:
              TwoPlrswap = 2
             print("{0} has been given the choice to swap with someone!")
             time.sleep(1)
             if TwoPlrswap == 1:
              TwoPlrswap = random.randrange(1,4)
              if TwoPlrswap == 1:
               print("{0} chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"{0} swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                TwoPlrrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Yourrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrswap == 2:
               print("{0} chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"{0} swapped with Jeremiah"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                TwoPlrrt = Jeremiahrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Jeremiahrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+"Jeremiah has protection, so nothing happened"+reset)
                time.sleep(1)
                JeremiahProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif TwoPlrswap != 1 or TwoPlrswap != 2:
               print("{0} chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"{0} swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "{0} now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(TwoPlrrt,Krisrt))
                time.sleep(1)
                TwoPlrsc = False
                TwoPlrturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                TwoPlrsc = False
                TwoPlrturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so TwoPlr will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif TwoPlrswap != 1:
              print("{0} would not like to swap, that's ok")
              time.sleep(1)
              TwoPlrsc = False
              TwoPlrturn = False
         elif RandomNotKris == PlayerListNotKris[2]:
           JeremiahLuckChoice = random.randrange(1,5)
           if JeremiahLuckChoice == 1:
            print("Jeremiah moves Kris's tiles now!")
            time.sleep(1)
            Jeremiahrt = Jeremiahrt - Kristilesadded
            Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
            time.sleep(1)
            print(Jeremiahnt.format(Jeremiahrt))
            Jeremiahturn = False
           elif JeremiahLuckChoice == 2:
            Jeremiahbc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahbc == True:
             if Randomnumber <= 90:
              Jeremiahblow = 1
             elif Randomnumber > 90:
              Jeremiahblow = 2
             print("Jeremiah has been given the choice to blow someone away.")
             time.sleep(1)
             if Jeremiahblow == 1:
              Jeremiahblow = random.randrange(1,4)
              if Jeremiahblow == 1:
               print("Jeremiah chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow == 2:
               print("Jeremiah chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)         
                TwoPlrProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahblow != 1 and Jeremiahblow != 2:
               print("Jeremiah chose to blow Kris away!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                Krista = (100 - Krisrt)/2
                Kristr = round(Krista)
                PlayerBlown = Red+"Kris has been blown {} tiles away."+reset
                print(PlayerBlown.format(Kristr))
                time.sleep(1)
                Krisrt = Krisrt + Kristr   
                Krisnt = "Kris has {} tiles remaining on the board now"
                print(Krisnt.format(Krisrt))
                time.sleep(1)
                Jeremiahbc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahbc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahblow != 1:
              print("Jeremiah chose to not blow anyone away! how kind")
              time.sleep(1)
              Jeremiahbc = False
              Jeremiahturn = False
           elif JeremiahLuckChoice == 3:
            print(Blue+"Jeremiah is now protected from debuffs!"+reset)
            time.sleep(1)
            JeremiahProtection = True
            Jeremiahturn = False
           elif JeremiahLuckChoice == 4:
            Jeremiahsc = True
            Randomnumber = random.randrange(1,101)
            while Jeremiahsc == True:
             Jeremiahsc = False
             if Randomnumber <= 90:
              Jeremiahswap = 1
             elif Randomnumber > 90:
              Jeremiahswap = 2
             print("Jeremiah has been given the choice to swap with someone!")
             time.sleep(1)
             if Jeremiahswap == 1:
              Jeremiahswap = random.randrange(1,4)
              if Jeremiahswap == 1:
               print("Jeremiah chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Jeremiah swapped with you"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Yourrt
                Yourrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Yourrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap == 2:
               print("Jeremiah chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Jeremiah swapped with TwoPlr"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = TwoPlrrt
                Jeremiahrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,TwoPlrrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Jeremiahswap != 1 or Jeremiahswap != 2:
               print("Jeremiah chose to swap with Kris!")
               time.sleep(1)
               if KrisProtection == False and Kriswon == False:
                print(yellow+"Jeremiah swapped with Kris"+reset)
                time.sleep(1)
                Jeremiaholdtiles = Jeremiahrt
                Jeremiahrt = Krisrt
                Krisrt = Jeremiaholdtiles
                PlayerSwapped = "Jeremiah now has {} tiles remaining on the board and Kris has {} tiles remaining on the board."
                print(PlayerSwapped.format(Jeremiahrt,Krisrt))
                time.sleep(1)
                Jeremiahsc = False
                Jeremiahturn = False
               elif KrisProtection == True and Kriswon == False:
                print(Blue+Blue+"Kris has protection so nothing happened!"+reset)
                time.sleep(1)
                KrisProtection = False
                Jeremiahsc = False
                Jeremiahturn = False
               elif Kriswon == True:
                   print(yellow+"Kris has escaped the board, so Jeremiah will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Jeremiahswap != 1:
              print("Jeremiah would not like to swap, that's ok")
              time.sleep(1)
              Jeremiahsc = False
              Jeremiahturn = False
      elif Krisrandomnumber <= Krisrt:
       Kristurn = False
       print(Blue+"Lucky Kris! Kris obtained a boost!"+reset)
       time.sleep(1)
       KrisLuckChoice = random.randrange(1,5)
       if KrisLuckChoice == 1:
            print("Kris moves double tiles now!")
            time.sleep(1)
            Krisrt = Krisrt - Kristilesadded
            Krisnt = "Kris has {} tiles remaining on the board now"
            time.sleep(1)
            print(Krisnt.format(Krisrt))
            Kristurn = False
       elif KrisLuckChoice == 2:
            Krisbc = True
            Randomnumber = random.randrange(1,101)
            while Krisbc == True:
             if Randomnumber <= 90:
              Krisblow = 1
             elif Randomnumber > 90:
              Krisblow = 2
             print("Kris has been given the choice to blow someone away.")
             time.sleep(1)
             if Krisblow == 1:
              Krisblow = random.randrange(1,4)
              if Krisblow == 1:
               print("Kris chose to blow you away!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                Yourta = (100 - Yourrt)/2
                Yourtr = round(Yourta)
                PlayerBlown = Red+"You have been blown {} tiles away."+reset
                print(PlayerBlown.format(Yourtr))
                time.sleep(1)
                Yourrt = Yourrt + Yourtr
                Yournt = "You have {} tiles remaining on the board now"
                print(Yournt.format(Yourrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krisbc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow == 2:
               print("Kris chose to blow TwoPlr away!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                TwoPlrta = (100 - TwoPlrrt)/2
                TwoPlrtr = round(TwoPlrta)
                PlayerBlown = Red+"{0} has been blown {} tiles away."+reset
                print(PlayerBlown.format(TwoPlrtr))
                time.sleep(1)
                TwoPlrrt = TwoPlrrt + TwoPlrtr
                TwoPlrnt = "{0} has {} tiles remaining on the board now"
                print(TwoPlrnt.format(TwoPlrrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print(Blue+"{0} has protection so nothing happened!"+reset)
                time.sleep(1)
                TwoPlrProtection = False
                Krisbc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisblow != 1 and Krisblow != 2:
               print("Kris chose to blow Jeremiah away!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                Jeremiahta = (100 - Jeremiahrt)/2
                Jeremiahtr = round(Jeremiahta)
                PlayerBlown = Red+"Jeremiah has been blown {} tiles away."+reset
                print(PlayerBlown.format(Jeremiahtr))
                time.sleep(1)
                Jeremiahrt = Jeremiahrt + Jeremiahtr   
                Jeremiahnt = "Jeremiah has {} tiles remaining on the board now"
                print(Jeremiahnt.format(Jeremiahrt))
                time.sleep(1)
                Krisbc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krisbc = False
                Kristurn = False
               elif Jeremiahwon == True:
                   print(yellow+"Jeremiah has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
             elif Krisblow != 1:
              print("Kris chose to not blow anyone away! how kind")
              time.sleep(1)
              Krisbc = False
              Kristurn = False
       elif KrisLuckChoice == 3:
            print(Blue+"Kris is now protected from debuffs!"+reset)
            time.sleep(1)
            KrisProtection = True
            Kristurn = False
       elif KrisLuckChoice == 4:
            Krissc = True
            Randomnumber = random.randrange(1,101)
            while Krissc == True:
             if Randomnumber <= 90:
              Krisswap = 1
             elif Randomnumber > 90:
              Krisswap = 2
             print("Kris has been given the choice to swap with someone!")
             time.sleep(1)
             if Krisswap == 1:
              Krisswap = random.randrange(1,4)
              if Krisswap == 1:
               print("Kris chose to swap with you!")
               time.sleep(1)
               if YourProtection == False and Youwon == False:
                print(yellow+"Kris swapped with you"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Yourrt
                Yourrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and you have {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Yourrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif YourProtection == True and Youwon == False:
                print(Blue+"You have protection so nothing happened!"+reset)
                time.sleep(1)
                YourProtection = False
                Krissc = False
                Kristurn = False
               elif Youwon == True:
                   print(yellow+"You have escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap == 2:
               print("Kris chose to swap with TwoPlr!")
               time.sleep(1)
               if TwoPlrProtection == False and TwoPlrwon == False:
                print(yellow+"Kris swapped with TwoPlr"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = TwoPlrrt
                TwoPlrrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and TwoPlr has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,TwoPlrrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif TwoPlrProtection == True and TwoPlrwon == False:
                print("{0} has protection, so nothing happened!")
                time.sleep(1)
                TwoPlrProtection = False
                Krissc = False
                Kristurn = False
               elif TwoPlrwon == True:
                   print(yellow+"{0} has escaped the board, so Kris will rechoose."+reset)
                   time.sleep(1)
                   continue
              elif Krisswap != 1 or Krisswap != 2:
               print("Kris chose to swap with Jeremiah!")
               time.sleep(1)
               if JeremiahProtection == False and Jeremiahwon == False:
                print(yellow+"Kris swapped with Jeremiah"+reset)
                time.sleep(1)
                Krisoldtiles = Krisrt
                Krisrt = Jeremiahrt
                Jeremiahrt = Krisoldtiles
                PlayerSwapped = "Kris now has {} tiles remaining on the board and Jeremiah has {} tiles remaining on the board."
                print(PlayerSwapped.format(Krisrt,Jeremiahrt))
                time.sleep(1)
                Krissc = False
                Kristurn = False
               elif JeremiahProtection == True and Jeremiahwon == False:
                print(Blue+Blue+"Jeremiah has protection so nothing happened!"+reset)
                time.sleep(1)
                JeremiahProtection = False
                Krissc = False
                Kristurn = False
             elif Krisswap != 1:
              print("Kris would not like to swap, that's ok")
              time.sleep(1)
              Krissc = False
              Kristurn = False
     elif Krislucktest == 2:
      print("It looks like Kris chose to play safe, that's ok.")
      time.sleep(1)
      Kristurn = False
   elif Krisrt % 2 != 0:
    Kristurn = False
  if Krisrt <= 0 and Kriswon == False:
   clearScreen()
   print(Blue+"Kris has successfully crossed the entire trail of the game!"+reset)
   PETC_function()
   PlayersLeft = PlayersLeft - 1
   Kriswon = True
  Progress_function()
 if Krisrt <= 0:
  print("KRIS WINS") 
 elif Krisrt > 0:
  print("KRIS LOSES")
 if Jeremiahrt <= 0:
  print("JEREMIAH WINS")
 elif Jeremiahrt > 0:
  print("JEREMIAH LOSES")
 if TwoPlrrt <= 0:
  print("{0} WINS")
 elif TwoPlrrt > 0:
  print("{0} LOSES")
 if Yourrt <= 0:
  print("YOU WIN")
 elif Yourrt > 0:
  print("YOU LOSE")
 PETC_function()
 if Yourrt <= 0 and TwoPlrrt > 0:
  return "W"
 elif TwoPlrrt <= 0 and Yourrt > 0:
  return "L"
#Board Game 