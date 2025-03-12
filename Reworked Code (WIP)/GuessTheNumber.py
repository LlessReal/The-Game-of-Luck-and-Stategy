import math, random
from guide import NumChoiceWithQuit, ExplanationSuggestion, InvalidInput, MessageStop, NumChoice, YesOrNo
from UsefulStuff import Red, reset, yellow, Blue, red, clearScreen
from time import sleep

def GuessTheNumber():
	ExplanationSuggestion("GTN")
	GTNLoses = GTNWins = 0 # Prereqs
	Scorebrd = 'Scoreboard:\n\nYou - {} pts. \n\nBot - {} pts'
	
   	while True:
		GeneratedNum = random.randrange(1,8)
		BotChoice = random.randrange(1,8)
		print("Guess a number from 1 - 7"); sleep(0.25)
		try:
			YourChoice = NumChoiceWithQuit(1,8)
			if YourChoice == "Redo": continue
			elif YourChoice == "Quit": return "Quit"
		except: InvalidInput(); continue
		
		YourChoiceIsClose = math.isclose(YourChoice, GeneratedNum, abs_tol = 1)
		BotChoiceIsClose = math.isclose(BotChoice, GeneratedNum, abs_tol = 1)
		print("The number generated was..."); sleep(1)
		print(f"{GeneratedNum}!\n"); sleep(1)
		if YourChoice == GeneratedNum: print(f"You chose {YourChoice}, so you get a point"); GTNWins += 1
		elif YourChoice != GeneratedNum and YourChoiceIsClose == True: print(f"You chose {YourChoice}, so you get half a point"); GTNWins += 0.5
		elif YourChoice != GeneratedNum and YourChoiceIsClose == False: print(f"You chose {YourChoice}, so you get no points")
		sleep(1)
		if BotChoice == GeneratedNum: print(f"Your opponent chose {BotChoice}, so your opponent gets a point"); GTNLoses += 1
		elif BotChoice != GeneratedNum and BotChoiceIsClose == True:print(f"Your opponent chose {BotChoice}, so your opponent gets half a point"); GTNLoses += 0.5
		elif BotChoice != GeneratedNum and BotChoiceIsClose == False: print(f"Your opponent chose {BotChoice}, so your opponent gets no points")
		sleep(1)
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
			print("It looks like you both hit 3 or over 3 at the same time! "); sleep(1)
			print("\n Time for a tie breaker!"); sleep(1)
			def tiebreaker_function():
				MessageStop('''This time, the number generated will be from 1 - 5
First challenger to guess it wins!
This will recur if both you and your opponent guess it right though.''')
				while True:
					GeneratedNum = random.randrange(1,6)
					BotChoice = random.randrange(1,6)
					try: YourChoice = int(input('''Guess a number from 1 - 5\n'''))
					except: InvalidInput(); continue 
					print("The number generated was..."); sleep(1)
					print(f"{GeneratedNum}!"); sleep(1)
					print(f"\nYou chose {YourChoice}"); sleep(1)
					print(f"\nYour opponent chose {BotChoice}"); sleep(1)
					if YourChoice == GeneratedNum and BotChoice == GeneratedNum :
						MessageStop('''\nYou and your opponent guessed the number correctly
\nTherefore, the tiebreaker has not been settled yet''')
						continue
					elif YourChoice != GeneratedNum and BotChoice != GeneratedNum:
						MessageStop('''You and your opponent guessed the number incorrectly
\nTherefore, the tiebreaker has not been settled yet''')
						continue 
					elif YourChoice == GeneratedNum and BotChoice != GeneratedNum:
						MessageStop('''You guessed the number correctly and your opponent did not
\nTherefore, '''+Blue+'''YOU WON THE TIEBREAKER FOR GUESS THE NUMBER!'''+reset)
						return "W"
					elif YourChoice != GeneratedNum and BotChoice == GeneratedNum:
						MessageStop('''You guessed the number correctly and your opponent did not
\nTherefore, '''+Red+'''you lost the tiebreaker for Guess the number.'''+reset)
						return "L"
			TheTieBreaker = tiebreaker_function()
			return "W" if TheTieBreaker == "W" else "L"

def GuessTheNumber(OnePlayerName,TwoPlayerName):
	GTNLoses = GTNWins = 0 # Preeqs
	Scorebrdpvp = '''Scoreboard:\n\nYou - {} pts. \n\nBot - {} pts'''
   	while True:
		GeneratedNum = random.randrange(1,8)
		print(f"{OnePlayerName}! Guess a number from 1 - 7"); sleep(0.25)
		YourChoice = NumChoiceWithQuit(1,8)
		if YourChoice == "Redo": continue
		elif YourChoice == "Quit": return "Quit"
		if YourChoice <= 0 or YourChoice >= 8: InvalidInput(); continue
		while True:
			print(f"{TwoPlayerName}! Guess a number from 1 - 7"); sleep(0.25)
			BotChoice = NumChoiceWithQuit(1,8)
			if BotChoice == "Redo": continue
			elif BotChoice == "Quit": return "Quit"
			if BotChoice <= 0 or BotChoice >= 8: InvalidInput(); continue
			break
		YourChoiceIsClose = math.isclose(YourChoice, GeneratedNum, abs_tol = 1)
		BotChoiceIsClose = math.isclose(BotChoice, GeneratedNum, abs_tol = 1)
		print("The number generated was..."); sleep(0.5)
		TheNumber = f"\n{GeneratedNum}!\n"
		if YourChoice == GeneratedNum:
			GTNWins = GTNWins + 1
			YourDecision = "{0} chose {1}, so {0} gets a point"
		elif YourChoice != GeneratedNum and YourChoiceIsClose == True:
			GTNWins = GTNWins + 0.5
			print(f"{OnePlayerName} chose {YourChoice}, so {OnePlayerName} gets half a point"); sleep(0.25)
		elif YourChoice != GeneratedNum and YourChoiceIsClose == False:
			print(f"{OnePlayerName} chose {YourChoice}, so {OnePlayerName} gets no points"); sleep(0.25)
		if BotChoice == GeneratedNum: 
			GTNLoses += 1
			print(f"{TwoPlayerName} chose {BotChoice}, so {TwoPlayerName} gets a point"); sleep(0.25)
		elif BotChoice != GeneratedNum and BotChoiceIsClose == True:
			GTNLoses = GTNLoses + 0.5
			print(f"{TwoPlayerName} chose {BotChoice}, so {TwoPlayerName} gets half a point"); sleep(0.25)
		elif BotChoice != GeneratedNum and BotChoiceIsClose == False:
			print(f"{TwoPlayerName} chose {BotChoice}, so {TwoPlayerName} gets no points"); sleep(0.25)
		
		MessageStop("\n" + Scorebrdpvp.format(OnePlayerName,GTNWins,TwoPlayerName,GTNLoses))
		if GTNWins >= 3 and GTNLoses < 3:
			MessageStop(f"{OnePlayerName} {Blue} was the first to reach 3 points! {reset}"); return "W"
		elif GTNWins < 3 and GTNLoses >= 3:
			MessageStop(f"{TwoPlayerName} {Blue} was the first to reach 3 points! {reset}"); return "L"
		elif GTNWins >= 3 and GTNLoses >= 3:
			print("It looks like {0} and {1} both hit 3 or over 3 at the same time! ".format(OnePlayerName,TwoPlayerName))
			sleep(1)
			print("\n Time for a tie breaker!"); sleep(1)
			def tiebreaker_function():
				print('''This time, the number generated will be from 1 - 5
			First challenger to guess it wins!
			This will recur if both you and your opponent guess it right though.''')
				MessageStop()
				while True:
					GeneratedNum = random.randrange(1,6)
					BotChoice = random.randrange(1,6)
					try:
						print(f'{OnePlayerName}! Guess a number from 1 - 5')
						YourChoice = NumChoiceWithQuit(1,6)
					except: InvalidInput(); continue
					clearScreen()
					print("The number generated was..."); sleep(1)
					print(f"{GeneratedNum}!"); sleep(1)
					print(f"\n{OnePlayerName} chose {YourChoice}"); sleep(1)
					print(f"\n{TwoPlayerName} chose {BotChoice}"); sleep(1)
					if YourChoice == GeneratedNum and BotChoice == GeneratedNum:
						MessageStop(f'''\nIt looks like {OnePlayerName} and {TwoPlayerName} guessed the number correctly
\nTherefore, the tiebreaker has not been settled yet''')
						continue
					elif YourChoice != GeneratedNum and BotChoice != GeneratedNum:
						MessageStop(f'''It looks like {OnePlayerName} and {TwoPlayerName} guessed the number incorrectly
\nTherefore, the tiebreaker has not been settled yet''')
						continue 
					elif YourChoice == GeneratedNum and BotChoice != GeneratedNum:
						MessageStop(f'''{OnePlayerName} guessed the number correctly and {TwoPlayerName} did not
\nTherefore, '''+f'''{OnePlayerName} '''+Blue+'''won the tiebreaker for Guess the Number!'''+reset)
						return "W"
					elif YourChoice != GeneratedNum and BotChoice == GeneratedNum:
						MessageStop(f'''{TwoPlayerName} guessed the number correctly and {OnePlayerName} did not
\nTherefore, '''+Red+f'''{TwoPlayerName} '''+Blue+'''won the tiebreaker for Guess the number.'''+reset)
						return "L"
			TheTieBreaker = tiebreaker_function()
			return "W" if TheTieBreaker == "W" else "L"