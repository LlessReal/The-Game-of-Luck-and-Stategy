import random
from UsefulStuff import yellow, Red, green, Blue, reset, clearScreen
from guide import InvalidInput, NumChoiceWithQuit, NumChoice, ExplanationSuggestion, MessageStop
from time import sleep
# Player Vs. Computer
def FourCorners():
    while True:
        print('''\n Choose your difficulty for Four Corners:''')
        sleep(0.5)
        Difficulties = [f"{Blue}Easy (3+ winners){reset}",f"{yellow}Medium (2+ winners){reset}", f"{Red}Hard (1+ winners){reset}"]
        for difficulty in Difficulties:
            print(f"\n {Difficulties.index(difficulty) + 1} - {difficulty}")
            sleep(0.25) # Display difficulty choices

        try:
            DifficultyChoice = NumChoice(range(1,4))
        except:
            InvalidInput()
            continue

        # Gets up until space
        DifficultyAlone = Difficulties[DifficultyChoice - 1][0:Difficulties[DifficultyChoice - 1].find(" ")]
        print(f"Alright! {DifficultyAlone} difficulty of Four Corners loading!")
        GameDecision = DifficultyChoice + 1 # Determines how many players must die for victor
        sleep(1.5)
        clearScreen()
        break
    
    ExplanationSuggestion("4C")
    # Variables needed
    AllColors = [Red+"RED"+reset,green+"GREEN"+reset,yellow+"YELLOW"+reset,Blue+"BLUE"+reset]
    RaphaelLives = MikeLives = JalenLives = MiguelLives = YourLives = 2
    PlayersOut = 0
    while True:
        try:
            print("Pick your color.")
            sleep(0.5)
            for x in range(1,5):
                print(f"\n{x} - {AllColors[x]}") # Color choices
                sleep(0.25)
          
            You = NumChoiceWithQuit(range(1,5)) - 1 # -1 for the index
            if You == "Quit":
                return
            elif You == "Redo":
                continue
        except:
            InvalidInput()
            continue
        Raphael = Mike = Jalen = Miguel = random.randrange(0,4) # Bots choose random color
        FourColors = random.randrange(0,4) # Random color chosen
        # Tally up choices n lives n allat
        AllPlayers = [[Raphael,RaphaelLives,"Raphael"],[Mike,MikeLives,"Mike"],[Jalen,JalenLives,"Jalen"],[Miguel,MiguelLives,"Miguel"],[You,YourLives,"You"]]
        print("The color chosen is......")
        sleep(0.5)
        print(f"{AllColors[FourColors]}!!!")
        sleep(0.5)
        for Character in AllPlayers:
            if Character[1] > 0: # If the character aint dead
                if Character[0] != FourColors: # If the same color wasn't chosen
                    print(f"{Blue}{Character[2]} chose {AllColors[Character[0]]}, so {Character[2]} is safe {reset}")
                elif Character[0] == FourColors:
                    Character[1] -= 1
                    print(f"{Red}{Character[2]} chose {AllColors[Character[0]]}, so Miguel has {Character[1]} live(s) left. {f"\n {Red+f"{Character[2]} IS OUT"+reset}" if Character[1] == 0 else ""} {reset}")
                    PlayersOut += 1 if Character[1] == 0 else 0 # Nothing happens if their lives isn't 0            
        MessageStop() # Message is already shown, no need for another
        LoseReturns = ["EL","ML","HL"]
        WinReturns = ["EW","MW","HW"]
        
        if YourLives == 0:
            MessageStop(Red+f"You lost a game of Four Corners on {DifficultyAlone.lower()} difficulty."+reset)
            return LoseReturns[DifficultyChoice - 1]
        elif PlayersOut >= GameDecision:
            MessageStop(Blue+f"YOU WON A GAME OF FOUR CORNERS ON {DifficultyAlone.upper()} DIFFICULTY!"+reset)
            return WinReturns[DifficultyChoice - 1]
    
# PVP Mode
def FourCorners(OnePlayerName,TwoPlayerName):
    ExplanationSuggestion("4C")
    AllColors = [Red+"RED"+reset,green+"GREEN"+reset,yellow+"YELLOW"+reset,Blue+"BLUE"+reset]
    YourLives = TwoPlrLives = MikeLives = JalenLives = MiguelLives = 2 # Default value of all lives is 2
    PlayersOut = 0
    while True:
        Mike = Jalen = Miguel = random.randrange(0,4) # All 3 characters will choose a random number
        FourColors = random.randrange(0,4) 
        try:
            clearScreen()
            print(f"{OnePlayerName}! Choose your color.")
            sleep(0.5)
            for x in range(1,5):
                print(f'''\n {x} - {AllColors[x]}''')
                sleep(0.25)
            
            You = NumChoiceWithQuit(range(1,5))
            if You == "Quit":
                return
            elif You == "Redo":
                continue
        except:
            InvalidInput()
            continue
        while True:
            try:
                clearScreen()
                print(f"{OnePlayerName} chose {AllColors[You]}.\n")
                sleep(1)
                print(f"{TwoPlayerName}! Choose your color.")
                sleep(0.5)
                for x in range(1,5):
                    print(f'''\n {x} - {AllColors[x]}''')
                    sleep(0.25)

                TwoPlr = NumChoiceWithQuit(range(1,5))
                if TwoPlr == "Quit":
                    return
                elif TwoPlr == "Redo":
                    continue
            except:
                InvalidInput()
                continue
            AllPlayers = [[TwoPlr,TwoPlrLives,"Raphael"],[Mike,MikeLives,"Mike"],[Jalen,JalenLives,"Jalen"],[Miguel,MiguelLives,"Miguel"],[You,YourLives,"You"]]
            print("The color chosen is......")
            sleep(0.5)
            print(f"{AllColors[FourColors - 1]}!!!")
            sleep(0.5)
            for Character in AllPlayers:
                if Character[1] > 0:
                    if Character[0] != FourColors:
                        print(Blue+f"{Character[2]} chose {AllColors[Character]}, so {Character[2]} is safe"+reset)
                    elif Character[0] == FourColors:
                        Character[1] -= 1
                        print(f"{Red}{Character[2]} chose {AllColors[Character]}, so Miguel has {Character[1]} live(s) left. {f"\n {Red+f"{Character[2]} IS OUT"+reset}" if Character[1] == 0 else ""} {reset}")
                        if Character[1] == 0:
                            PlayersOut += 1
                MessageStop()
                if YourLives > 0 and TwoPlrLives == 0:
                    MessageStop(f"{OnePlayerName} has lasted longer than {TwoPlayerName} in Four Corners!")
                    return "W"
                elif YourLives == 0 and TwoPlrLives > 0:
                    MessageStop(f"{TwoPlayerName} has lasted longer than {OnePlayerName} in Four Corners!")
                    return "L"
                elif YourLives == 0 and TwoPlrLives == 0:
                    MessageStop(f"{TwoPlayerName} and {OnePlayerName} has both been eliminated, so the game will now reset.") 
                    YourLives = TwoPlrLives = MikeLives = JalenLives = MiguelLives = 2 # Default value of all lives is 2
                    PlayersOut = 0