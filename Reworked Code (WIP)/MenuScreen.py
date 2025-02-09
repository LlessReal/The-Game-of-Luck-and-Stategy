import time
from UsefulStuff import yellow, reset, clearScreen
from guide import InvalidInput, YesOrNo, explainGame, NumChoiceWithQuit

def ModeSelection(TheMode):
    while True:
        clearScreen()
        print(f"Mode selected: {yellow}{TheMode}{reset}")
        time.sleep(0.5)
        print("\nContinue?")
        try:
            ModeConfirmation = YesOrNo() # Y/N to mode selection or not
        except:
            InvalidInput()
            continue
        if ModeConfirmation == 1:
            print(f"\nAlright! {TheMode} mode loading!")
            time.sleep(1)
            if TheMode == "Vs. Computer":
                print("\nMy bot is armed and ready for you") # Phrases based on mode chosen
            elif TheMode == "PVP":
                print("\n May the luckiest and smartest win!")
            time.sleep(1.5)
            clearScreen()
            return
        elif ModeConfirmation == 2:
            print("Understood.")
            time.sleep(1)
            clearScreen()
            return "Redecide" # If no, rego
    
def MenuScreen():
    while True:
        try:
            print("Menu Screen:")
            MenuOptions = ["Vs. Computer","PVP","What even is this game?"]
            for MenuOption in MenuOptions:
                print(f"\n{MenuOptions.index(MenuOption) + 1} - {MenuOption}")
                time.sleep(0.25)
            MenuOptionChoice = NumChoiceWithQuit()
            if MenuOptionChoice == "Quit":
                return "Quit"
            elif MenuOptionChoice == "Redo":
                continue
            MenuOptionSelected = MenuOptions[MenuOptionChoice - 1] # If it aint in there, prepare for za error
            clearScreen()
        except:
            InvalidInput()
            continue
        if MenuOptionSelected == "What even is this game?":
           explainGame()     
        else:
            ModeSelected = ModeSelection(MenuOptionSelected)
            if ModeSelected == "Redecide":
                continue
            else:
               return MenuOptionSelected # Will return a mode name, and determine where to go next based on that