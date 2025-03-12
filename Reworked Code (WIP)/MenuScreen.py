import time
from UsefulStuff import yellow, reset, clearScreen
from guide import InvalidInput, YesOrNo, GameExplanation, NumChoiceWithQuit
    
def MenuScreen():
    while True:
        try:
            print("Menu Screen:") # Label
            MenuOptions = ["Vs. Computer","PVP","What even is this game?"] # All menu options
            for MenuOption in MenuOptions:
                print(f"\n{MenuOptions.index(MenuOption) + 1} - {MenuOption}") # Lays em out on page like a list
                time.sleep(0.25) 
            MenuOptionChoice = NumChoiceWithQuit() # Prompt Choice with quit option
            if MenuOptionChoice == "Quit": return "Quit"
            elif MenuOptionChoice == "Redo": continue
            MenuOptionSelected = MenuOptions[MenuOptionChoice - 1] # If it aint in there, prepare for za error
            clearScreen()
        except: InvalidInput() ; continue
        if MenuOptionSelected == "What even is this game?": GameExplanation("Game System") # Explains entire game system
        else:
            ModeSelected = ModeSelection(MenuOptionSelected) # Confirms mode if a mode was selected
            if ModeSelected == "Redecide": continue
            else: return MenuOptionSelected # Will return a mode name, and determine where to go next based on that

# Mode selection function
def ModeSelection(TheMode):
    while True:
        clearScreen()
        print(f"Mode selected: {yellow}{TheMode}{reset}")
        time.sleep(0.5)
        try: ModeConfirmation = YesOrNo() # Y/N to mode selection or not
        except: InvalidInput() ; continue
        if ModeConfirmation == 1:
            print(f"\nAlright! {TheMode} mode loading!")
            time.sleep(1)
            if TheMode == "Vs. Computer": print("\nMy bot is armed and ready for you") # Phrases based on mode chosen
            elif TheMode == "PVP": print("\n May the luckiest and smartest win!")
            time.sleep(1.5)
            clearScreen()
            return
        elif ModeConfirmation == 2: print("Understood."); time.sleep(1); clearScreen(); return "Redecide" # If no, rego