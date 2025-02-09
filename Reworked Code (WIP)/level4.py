import random,time
from UsefulStuff import Blue, Red, reset, clearScreen
from guide import NumChoiceWithQuit, ExplanationSuggestion, InvalidInput, PETC_function

def level4_function():
   RPSLoses = RPSWins = 0 # Prereqs
   ExplanationSuggestion("RPS") # Explain

   while RPSLoses != 3 and RPSWins != 3:
      try:
         print("Choose your weapon:")
         AllChoices = ["Rock","Paper","Scissors","Random"]
         for Choice in AllChoices:
            print(f"\n{AllChoices.index(Choice) + 1} - {Choice}") # Lists choices (from above)
            time.sleep(0.1)
         RPSChoice = NumChoiceWithQuit() # Get number
         if RPSChoice == "Redo":
            continue
         elif RPSChoice == "Quit":
            return "Quit"
         if RPSChoice == 4: # If you chose 4 (Random), will randomly choose weapon
            RPSChoice = random.randrange(0,3)
         RPSBot = random.randrange(1,4) # Bot chooses
      except:
         InvalidInput() # Invalid Input
         continue
      
      # State who chose what
      clearScreen()
      print(f"\nYou {f"chose {AllChoices[RPSBot - 1]}" if RPSChoice != 4 else f"decided to randomly choose a weapon. Which is {AllChoices[RPSChoice]}"}\n")
      time.sleep(1)
      print(f"\nYour opponent chose {AllChoices[RPSBot - 1]}\n")
      time.sleep(1)
      # Winning condition
      RPSWinCondition = (RPSChoice == 2 and RPSBot == 1) or (RPSChoice == 1 and RPSBot == 3) or (RPSChoice == 3 and RPSBot == 2)
      if RPSChoice == RPSBot: # Draw
         print("Draw!")
      elif RPSWinCondition: # Win
         print("You gain one point.\n")
         RPSLoses += 1
      else: # Loss
         print("You opponent gains one point.")
         RPSWins += 1
      print(f'''Scoreboard: \n\nYou - {RPSWins} pts. \n\nBot - {RPSLoses} pts''') # Scoreboard
      PETC_function()

   # If someone hit 3 points, game ends
   print(f"{"You" if RPSWins == 3 else "Your opponent"} are the first to gain 3 points.")
   time.sleep(1)
   print(f"\nTherefore, {f"{Blue}YOU WON A GAME OF ROCK PAPER SCISSORS!{reset}" if RPSWins == 3 else f"{Red}you lost a game of Rock Paper Scissors{reset}"}")
   PETC_function()
   return "W" if RPSWins == 3 else "L"