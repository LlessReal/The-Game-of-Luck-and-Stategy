import random,time
from UsefulStuff import Blue, Red, reset, clearScreen
from guide import NumChoiceWithQuit, ExplanationSuggestion, InvalidInput, MessageStop

def RPS():
   RPSLoses = RPSWins = 0 # Prereqs
   ExplanationSuggestion("RPS") # Explain

   while RPSLoses != 3 and RPSWins != 3:
      try:
         print("Choose your weapon:")
         AllChoices = ["Rock","Paper","Scissors","Random"]
         # Lists choices (from above)
         for Choice in AllChoices: print(f"\n{AllChoices.index(Choice) + 1} - {Choice}"); time.sleep(0.1)
         RPSChoice = NumChoiceWithQuit() # Get number
         if RPSChoice == "Redo": continue
         elif RPSChoice == "Quit": return "Quit"
         # If you chose 4 (Random), will randomly choose weapon
         if RPSChoice == 4: RPSChoice = random.randrange(0,3)
         RPSBot = random.randrange(1,4) # Bot chooses
      except: InvalidInput(); continue
      
      # State who chose what
      clearScreen()
      print(f"\nYou {f"chose {AllChoices[RPSBot - 1]}" if RPSChoice != 4 else f"decided to randomly choose a weapon. Which is {AllChoices[RPSChoice]}"}\n")
      time.sleep(1)
      print(f"\nYour opponent chose {AllChoices[RPSBot - 1]}\n")
      time.sleep(1)
      # Winning condition
      RPSWinCondition = (RPSChoice == 2 and RPSBot == 1) or (RPSChoice == 1 and RPSBot == 3) or (RPSChoice == 3 and RPSBot == 2)
      if RPSChoice == RPSBot: MessageStop("Draw!")
      elif RPSWinCondition: MessageStop("You gain one point.\n"); RPSWins += 1  # Win
      else: MessageStop("You opponent gains one point."); RPSLoses += 1
      MessageStop(f'''Scoreboard: \n\nYou - {RPSWins} pts. \n\nBot - {RPSLoses} pts''') # Scoreboard

   # If someone hit 3 points, game ends
   print(f"{"You are" if RPSWins == 3 else "Your opponent is"} the first to gain 3 points.")
   time.sleep(1)
   MessageStop(f"\nTherefore, {f"{Blue}YOU WON A GAME OF ROCK PAPER SCISSORS!{reset}" if RPSWins == 3 else f"{Red}you lost a game of Rock Paper Scissors{reset}"}")
   return "W" if RPSWins == 3 else "L"