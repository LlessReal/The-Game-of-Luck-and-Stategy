
import time, random
from guide import NumChoiceWithQuit, InvalidInput, PETC_function, PNTC_function, YesOrNo
from UsefulStuff import Red, reset, yellow, Blue, blue_back, red, clearScreen
import level4, level6, level7, level8, level9, level10

def GameSelected(TheGame,Points):
    if Points == "UC":
        print(f"{red}{TheGame} is under construction at the moment.{reset}")
        PETC_function()
        return "Redecide"
    
    while True:
        clearScreen()
        print(f"Game selected: {yellow}{TheGame}{reset}")
        time.sleep(0.5)
        print("\nContinue?")
        try:
            GameChoice = YesOrNo()
            break
        except:
            InvalidInput()
            continue
    if GameChoice == 1:
        print(f"Alright! {TheGame} loading!")
        time.sleep(1.5)
        clearScreen()
        return TheGame
    elif GameChoice == 2:
        print("Understood.")
        time.sleep(1)
        clearScreen()
        return "Redecide"

def WinStatementFunc(GameStatus,TheGame,ThePoints,PointsNow,Difficulty="N/A"):
    if "W" in GameStatus and Difficulty == "N/A":
        print(f'''{Blue}Congratulations on your win in {TheGame}. \n  
You gained {ThePoints} points so you have {PointsNow} points in total now.'''+reset)
    elif "L" in GameStatus and Difficulty == "N/A":
        print(f'''{Red}It looks like you lost a game of {TheGame}. \n
You lost {ThePoints / 2} points so you have {PointsNow} points in total now.'''+reset)
        
    elif "W" in GameStatus and Difficulty != "N/A":   
        print(Blue+f'''Congratulations on your win in {TheGame} ({Difficulty} Difficulty) \n 
You gained {ThePoints} points so you have {PointsNow} points in total now.'''+reset)
    elif "L" in GameStatus and Difficulty != "N/A":  
        print(Red+f'''It looks like you lost a game of {TheGame} ({Difficulty} Difficulty) \n  
You lost {ThePoints} points so you have {PointsNow} points in total now.'''+reset)
                             
def PVC():
    GamePoints = 0
    print("Gain as many points as you can in 5 games! \n You can win some and you can lose some.")
    PETC_function()
    GamesLeft = 5
    while GamesLeft != 0:
        print("\nChoose your game.")
        gamelist = [["Rock Paper Scissors","300"],["Gold Fish","UC"],["Four Corners","100 - 500"],
        ["Guess the number","300"],["Board Game","100 - 500"],["Tic-Tac-Toe","100 - 300"],["Connect FOUR","100 - 400"]]
        
        for gameinlist in gamelist:
            PointReward = f"{Blue}[{gameinlist[1]} points]{reset}" if gameinlist[1] != "UC" else f"{yellow}UNDER CONSTRUCTION{reset}"
            print(f"\n{gamelist.index(gameinlist) + 1} - {gameinlist[0]} {PointReward}")
            # Put UC in the list if you want it to show Under Construction
            """
            First game example:
            1 - Rock Paper Scissors [300 Points] (in blue)
            """
            time.sleep(0.1)
        try:
            GameChoice = NumChoiceWithQuit()
            if GameChoice == "Redo":
                continue
            elif GameChoice == "Quit":
                return
            GameChosen = gamelist[GameChoice - 1][0] # If this is not in the list, an error will return
            PointWorth = gamelist[GameChoice - 1][1]
        except:
            InvalidInput()
            continue  
        while True:
            GameDecision = GameSelected(GameChosen,PointWorth)
            # Checks to see what game we're doing, and calls that script based on it
            # RPS 
            if GameDecision == "Rock Paper Scissors":
                GamePointChange = 300
                GameInSession = level4.level4_function()
                clearScreen()
                if GameInSession == "Quit":
                    return # Back to the main screen
                GamePoints += GamePointChange if GameInSession == "W" else -(GamePointChange / 2)
                WinStatementFunc(GameInSession,GameDecision,GamePointChange,GamePoints)
            
            # Four Corners    
            elif GameDecision == "Four Corners":
                GameInSession = level6.level6_function()
                clearScreen()
                if GameInSession == "Quit":
                    return 
                Meanings = [["EW",100],["MW",300],["EW",500],["EL",-50],["ML",-150],["HL",-250]]
                Difficulties = ["Easy","Medium","Hard"]
                for Difficulty in Difficulties:
                    if GameInSession[0] in Difficulty:    
                        ChosenDifficulty = Difficulty
                        for meaning in Meanings:
                            if GameInSession in meaning:
                                GamePoints += meaning[1]
                                GamePointChange = abs(meaning[1])
                WinStatementFunc(GameInSession,GameDecision,GamePointChange,GamePoints,ChosenDifficulty)
                                    
            # Guess the number
            elif GameDecision == "Guess the number":
                GameInSession = level7.level7_function()
                GamePointChange = 300
                clearScreen()
                if GameInSession == "Quit":
                    return
                GamePoints += GamePointChange if GameInSession == "W" else -(GamePointChange / 2)
                WinStatementFunc(GameInSession,GameDecision,GamePointChange,GamePoints)

            elif GameDecision == "Board Game":
                GameInSession = level8.level8_function()
                clearScreen()
                if GameInSession == "Quit":
                    return
                Meanings = [["EW",100],["MW",300],["EW",500],["EL",-50],["ML",-150],["HL",-250]]
                Difficulties = ["Easy","Medium","Hard"]
                for Difficulty in Difficulties:
                    if GameInSession[0] in Difficulty:  
                        ChosenDifficulty = Difficulty    
                        for meaning in Meanings:
                            if GameInSession in meaning:
                                GamePoints += meaning[1]
                                GamePointChange = abs(meaning[1])
                WinStatementFunc(GameInSession,GameDecision,GamePointChange,GamePoints,ChosenDifficulty)

            # Tic-Taco-Toe
            elif GameDecision == "Tic-Tac-Toe":
                GameInSession = level9.level9_function()
                clearScreen()
                if GameInSession == "Quit":
                    return 
                Meanings = [["EW",100],["MW",300],["EW",500],["EL",-50],["ML",-150],["HL",-250]]
                Difficulties = ["Easy","Medium","Hard"]
                for Difficulty in Difficulties:
                    if GameInSession[0] in Difficulty:
                        ChosenDifficulty = Difficulty      
                        for meaning in Meanings:
                            if GameInSession in meaning:
                                GamePoints += meaning[1]
                                GamePointChange = abs(meaning[1])
                WinStatementFunc(GameInSession,GameDecision,GamePointChange,GamePoints,ChosenDifficulty)

            # Connect Four
            elif GameDecision == "Connect Four":
                GameInSession = level10.level10_function()
                clearScreen()
                if GameInSession == "Quit":
                    return 
                clearScreen()
                Meanings = [["EW",100],["MW",300],["EW",500],["EL",-50],["ML",-150],["HL",-250]]
                Difficulties = ["Easy","Medium","Hard"]
                for Difficulty in Difficulties:
                    if GameInSession[0] in Difficulty:      
                        ChosenDifficulty = Difficulty
                        for meaning in Meanings:
                            if GameInSession in meaning:
                                GamePoints += meaning[1]
                                GamePointChange = abs(meaning[1])
                WinStatementFunc(GameInSession,GameDecision,GamePointChange,GamePoints,ChosenDifficulty)
            # If no game, redecide
            elif GameDecision == "Redecide":
                pass

            break # Breaks out of decision loop

        if GameDecision == "Redecide": # If we chose to redecide
            continue    

        else: # If we just finishe a game
            PETC_function()
            clearScreen()
            GamesLeft -= 1
            print(f"\nYou and your opponent get to play {GamesLeft} more game(s)")
            PETC_function()
    # Once we break out of the big loop
    print(Blue+'''You have finished your trial of 7 games!''' + reset)
    PETC_function()
    for resultcount in range(5):
        print(f"Your final score is{"." * resultcount}")
        time.sleep(0.25)
        if resultcount != 4:
            clearScreen()
    if GamePoints <= 0:
        RoastingPhrases = ["Well, that's dissappointing.","I guess you're pretty unlucky huh.",
        "Oof, maybe you'll be luckier next time.","Well, that wasn't impressive.",
        "WOW! That was Sh!%.","Gosh you made me so mad it's unreal."]
        print(f"{Red} {GamePoints} {reset}.")
        print(f"{Red} {random.choice(RoastingPhrases)} {reset}")

    elif GamePoints > 0 and GamePoints < 500:
        print(f"{GamePoints} {reset}.")

    if GamePoints >= 500 and GamePoints < 1000:
        print(f"{Blue} {GamePoints} {reset}!\n Not bad challenger!")

    elif GamePoints >= 1000 and GamePoints < 2000:
        print(f"{Blue} {GamePoints} {reset}!\nYou did great challenger!!")

    elif GamePoints >= 2000 and GamePoints < 3000:
        print(f"{Blue} {GamePoints} {reset}!\n You're crazy challenger! Well done!!")

    elif GamePoints >= 3000:
            print(f"{Blue} {GamePoints} {reset}.")
            glazelines = ["Woah! That's a very big score!","You're not a challenger anymore...","You're a "+blue_back+"GOD!"+reset]
            for glazing in glazelines:
                print(glazing)
                if glazelines.index(glazing) != len(glazelines) - 1:
                    time.sleep(1)
    time.sleep(1)
    print('''\nFeel free to share your score with your friends!''')
    PETC_function()