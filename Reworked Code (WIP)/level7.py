import time, math, random
from guide import NumChoiceWithQuit, ExplanationSuggestion, InvalidInput, MessageStop, NumChoice, YesOrNo
from UsefulStuff import Red, reset, yellow, Blue, red, clearScreen

def level7_function():
   ExplanationSuggestion("GTN")
   GTNLoses = GTNWins = 0 # Prereqs
   Scorebrd = '''Scoreboard:\n\nYou - {} pts. \n\nBot - {} pts'''
   
   while True:
      v = random.randrange(1,8)
      BotChoice = random.randrange(1,8)
      print("Guess a number from 1 - 7")
      time.sleep(0.25)
      YourChoice = NumChoiceWithQuit()
      if YourChoice == "Redo":
         continue
      elif YourChoice == "Quit":
         return "Quit"
      elif YourChoice not in range(1,9):
         InvalidInput()
         continue
      
      YourChoiceIsClose = math.isclose(YourChoice, v, abs_tol = 1)
      BotChoiceIsClose = math.isclose(BotChoice, v, abs_tol = 1)
      print("The number generated was...")
      time.sleep(1)
      print(f"{v}!\n")
      time.sleep(1)
      if YourChoice == v:
         GTNWins += 1
         print(f"You chose {YourChoice}, so you get a point")
      elif YourChoice != v and YourChoiceIsClose == True:
         GTNWins += 0.5
         print(f"You chose {YourChoice}, so you get half a point")
      elif YourChoice != v and YourChoiceIsClose == False:
         print(f"You chose {YourChoice}, so you get no points")
      time.sleep(1)
      if BotChoice == v:
         GTNLoses = GTNLoses + 1
         BotsDecision = "Your opponent chose {}, so your opponent gets a point"
      elif BotChoice != v and BotChoiceIsClose == True:
         GTNLoses = GTNLoses + 0.5
         BotsDecision = "Your opponent chose {}, so your opponent gets half a point"
      elif BotChoice != v and BotChoiceIsClose == False:
         BotsDecision = f"Your opponent chose {BotChoice}, so your opponent gets no points"
      time.sleep(1)
      MessageStop("\n" + Scorebrd.format(GTNWins,GTNLoses))
      if GTNWins >= 3 and GTNLoses < 3:
         MessageStop('''You were the first to reach 3 points, 
Therefore, '''+Blue+'''you won the game of Guess the Number!'''+reset)
         return "W"
      elif GTNWins < 3 and GTNLoses >= 3:
         MessageStop('''Your opponent was the first to reach 3 points, 
Therefore, '''+Red+'''you lost the game of Guess the Number.'''+reset)
         return "L"
      elif GTNWins >= 3 and GTNLoses >= 3:
         print("It looks like you both hit 3 or over 3 at the same time! ")
         time.sleep(1)
         print("\n Time for a tie breaker!")
         time.sleep(1)
         def tiebreaker_function():
            MessageStop('''This time, the number generated will be from 1 - 5
   First challenger to guess it wins!
   This will recur if both you and your opponent guess it right though.''')
            while True:
               v = random.randrange(1,6)
               BotChoice = random.randrange(1,6)
               try:
                  YourChoice = int(input('''Guess a number from 1 - 5\n'''))
               except:
                  InvalidInput()
                  continue 
               print("The number generated was...")
               time.sleep(1)
               print(f"{v}!")
               time.sleep(1)
               print(f"\nYou chose {YourChoice}")
               time.sleep(1)
               print(f"\nYour opponent chose {BotChoice}")
               time.sleep(1)
               if YourChoice == v and BotChoice == v :
                  MessageStop('''\nYou and your opponent guessed the number correctly
\nTherefore, the tiebreaker has not been settled yet''')
                  continue
               elif YourChoice != v and BotChoice != v:
                  MessageStop('''You and your opponent guessed the number incorrectly
\nTherefore, the tiebreaker has not been settled yet''')
                  continue 
               elif YourChoice == v and BotChoice != v:
                  MessageStop('''You guessed the number correctly and your opponent did not
\nTherefore, '''+Blue+'''YOU WON THE TIEBREAKER FOR GUESS THE NUMBER!'''+reset)
                  return "W"
               elif YourChoice != v and BotChoice == v:
                  MessageStop('''You guessed the number correctly and your opponent did not
\nTherefore, '''+Red+'''you lost the tiebreaker for Guess the number.'''+reset)
                  return "L"
         TheTieBreaker = tiebreaker_function()
         return "W" if TheTieBreaker == "W" else "L"

def pvplevel7_function(OnePlayerName,TwoPlayerName):
   GTNLoses = GTNWins = 0 # Preeqs
   Scorebrdpvp = '''Scoreboard:\n\nYou - {} pts. \n\nBot - {} pts'''
   while True:
      v = random.randrange(1,8)
      print("{}! Guess a number from 1 - 7".format(OnePlayerName))
      time.sleep(0.25)
      YourChoice = NumChoiceWithQuit()
      if YourChoice == "Redo":
         continue
      elif YourChoice == "Quit":
         return "Quit"
      if YourChoice <= 0 or YourChoice >= 8:
         InvalidInput()
         continue
      while True:
         print("{}! Guess a number from 1 - 7".format(TwoPlayerName))
         time.sleep(0.25)
         BotChoice = NumChoiceWithQuit()
         if BotChoice == "Redo":
            continue
         elif BotChoice == "Quit":
            return "Quit"
         if BotChoice <= 0 or BotChoice >= 8:
            InvalidInput()
            continue
         break
      YourChoiceIsClose = math.isclose(YourChoice, v, abs_tol = 1)
      BotChoiceIsClose = math.isclose(BotChoice, v, abs_tol = 1)
      print("The number generated was...")
      time.sleep(0.5)
      TheNumber = f"\n{v}!\n"
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
      MessageStop("\n" + Scorebrdpvp.format(OnePlayerName,GTNWins,TwoPlayerName,GTNLoses))
      if GTNWins >= 3 and GTNLoses < 3:
         MessageStop(f"{OnePlayerName} {Blue} was the first to reach 3 points! {reset}")
         return "W"
      elif GTNWins < 3 and GTNLoses >= 3:
         MessageStop(f"{TwoPlayerName} {Blue} was the first to reach 3 points! {reset}")
         return "L"
      elif GTNWins >= 3 and GTNLoses >= 3:
         print("It looks like {0} and {1} both hit 3 or over 3 at the same time! ".format(OnePlayerName,TwoPlayerName))
         time.sleep(1)
         print("\n Time for a tie breaker!")
         time.sleep(1)
         def tiebreaker_function():
            print('''This time, the number generated will be from 1 - 5
         First challenger to guess it wins!
         This will recur if both you and your opponent guess it right though.''')
            MessageStop()
            while True:
               v = random.randrange(1,6)
               BotChoice = random.randrange(1,6)
               try:
                  print('''{}! Guess a number from 1 - 5'''.format(OnePlayerName))
                  YourChoice = int(input(""))
                  clearScreen()
               except:
                  InvalidInput()
                  continue 
               print("The number generated was...")
               time.sleep(1)
               TheNumber = f"{v}!"
               time.sleep(1)
               YourDecision = f"\n{OnePlayerName} chose {YourChoice}"
               time.sleep(1)
               BotsDecision = "\n{TwoPlayerName} chose {BotChoice}"
               time.sleep(1)
               if YourChoice == v and BotChoice == v:
                  MessageStop(f'''\nIt looks like {OnePlayerName} and {TwoPlayerName} guessed the number correctly
         \nTherefore, the tiebreaker has not been settled yet''')
                  continue
               elif YourChoice != v and BotChoice != v:
                  MessageStop(f'''It looks like {OnePlayerName} and {TwoPlayerName} guessed the number incorrectly
         \nTherefore, the tiebreaker has not been settled yet''')
                  continue 
               elif YourChoice == v and BotChoice != v:
                  MessageStop(f'''{OnePlayerName} guessed the number correctly and {TwoPlayerName} did not
         \nTherefore, '''+f'''{OnePlayerName} '''+Blue+'''won the tiebreaker for Guess the Number!'''+reset)
                  return "W"
               elif YourChoice != v and BotChoice == v:
                  MessageStop(f'''{TwoPlayerName} guessed the number correctly and {OnePlayerName} did not
         \nTherefore, '''+Red+f'''{TwoPlayerName} '''+Blue+'''won the tiebreaker for Guess the number.'''+reset)
                  return "L"
         TheTieBreaker = tiebreaker_function()
         return "W" if TheTieBreaker == "W" else "L"