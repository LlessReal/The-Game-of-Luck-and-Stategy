import time
from guide import NumChoiceWithQuit, InvalidInput, MessageStop, YesOrNo
from UsefulStuff import Red, reset, yellow, Blue, red, green, clearScreen
import RPS, GuessTheNumber, TicTacToe, Connect4
from PVC import GameSelected # Borrowing this function from PVC

def WinStatementFunc(GameStatus,TheGame,PONGiven,PTNGiven):
    if GameStatus == "W":
        return f"{green}{PONGiven} {Blue}has won the game of {TheGame}! {reset}"
    elif GameStatus == "L":
        return f"{red}{PTNGiven} {Blue}has won the game of {TheGame}! {reset}"

def PVP():
    PlrOnePts = PlrTwoPts = 0 # Point initialization
    PONSelection = True
    while PONSelection == True:
        PlayerOneName = str(input("Player 1! Type in your name. \n"+yellow+"\n (Name must contain atleast one letter and be no longer than 10 characters.)\n"+reset))
        if len(PlayerOneName) != 0 and len(PlayerOneName) <= 10 and PlayerOneName.isdigit() == False:
            while True:
                clearScreen()
                print(f"Player 1 name selected: {PlayerOneName}"); time.sleep(1)
                try: PONConfirmation = YesOrNo()
                except: InvalidInput(); continue
                if PONConfirmation == 1:
                    print("Great!"); time.sleep(1)
                    PONNoColor = PlayerOneName
                    PlayerOneName = green + PlayerOneName + reset
                    MessageStop(f"\n Player 1 Name: {PlayerOneName}")
                    time.sleep(1.5)
                    clearScreen()
                    PONSelection = False
                    break
                elif PONConfirmation == 2: print("Understood."); time.sleep(1); clearScreen(); break
                else: InvalidInput()
        else: 
            InvalidInput('''Name must contain atleast one letter and be no longer than 10 characters.)
(Your name also cannot be the same as Player 1's name''')
            continue

    PTNSelection = True
    while PTNSelection == True:
            PlayerTwoName = str(
                input('''Player 2! Type in your name.
''' + yellow + '''(Name must contain atleast one letter and be no longer than 10 characters.)
(Your name also cannot be the same as Player 1's name)\n ''' + reset))
            if len(PlayerTwoName) != 0 and len(PlayerTwoName) <= 10 and PlayerTwoName.isdigit() == False and PlayerTwoName != PONNoColor:
                while True:
                    clearScreen()
                    print(f"Player 2 name selected: {PlayerTwoName}"); time.sleep(1)
                    try: PTNSelection = YesOrNo()
                    except: InvalidInput(); continue
                    if PTNSelection == 1:
                        print("Great!"); time.sleep(1)
                        PlayerTwoName = red + PlayerTwoName + reset
                        print(f"\nPlayer 2 Name: {PlayerTwoName}"); time.sleep(1.5)
                        clearScreen()
                        PTNSelection = False
                        break
                    elif PTNSelection == 2:
                        print("Understood."); time.sleep(1)
                        clearScreen(); break
                    else: InvalidInput(); continue
            else:
                clearScreen()
                InvalidInput('''Name must contain atleast one letter and be no longer than 10 characters.)
(Your name also cannot be the same as Player 1's name''')

    MessageStop('''Win as many games as you can!
Whichever opponent reaches 3 wins in the games first will win the game of luck and stategy!''')
    GamesLeft = 5
    while GamesLeft != 0 and PlrOnePts != 3 and PlrTwoPts != 3:
        print("\nChoose your game.")
        gamelist = [["Gold Fish","UC"],["Four Corners",""],
        ["Guess the number",""],["Board Game","UC"],["Tic-Tac-Toe",""],["Connect FOUR",""]]
        for gameinlist in gamelist:
            print(f"\n{gamelist.index(gameinlist) + 1} - {gameinlist[0]} " + yellow if gameinlist[1] == "UC" else Blue + f"[{f"{gameinlist[1]} points" if gameinlist[1] != "UC" else "UNDER CONSTRUCTION"}]" + reset)
            time.sleep(0.1)
        time.sleep(0.5)
        try:
            GameChoice = NumChoiceWithQuit()
            if GameChoice == "Redo": continue
            elif GameChoice == "Quit": return
        except: InvalidInput(); continue
        
        GameChosen = gamelist[GameChoice - 1][0]
        PointWorth = gamelist[GameChoice - 1][1]
        while True:
            GameDecision = GameSelected(GameChosen,PointWorth)
            if GameDecision == "Rock Paper Scissors": GameInSession = RPS.RPS(PlayerOneName,PlayerTwoName)
            elif GameDecision == "Guess the number": GameInSession = GuessTheNumber.GuessTheNumber(PlayerOneName,PlayerTwoName)
            elif GameDecision == "Tic-Tac-Toe": GameInSession = TicTacToe.TicTacToe(PlayerOneName,PlayerTwoName)
            elif GameDecision == "Connect Four": GameInSession = Connect4.Connect4(PlayerOneName,PlayerTwoName)   
            clearScreen()
            if GameInSession == "Quit": return 
            elif GameInSession == "W": PlrOnePts += 1
            elif GameInSession == "L": PlrTwoPts += 1    
            break

        if GameDecision == "Redecide": continue
        else:
            MessageStop(WinStatementFunc(GameInSession,GameDecision,PlayerOneName,PlayerTwoName))
            MessageStop(f"Score Board:\n\n{PlayerOneName} - {PlrOnePts} win(s). \n\n{PlayerTwoName} - {PlrTwoPts} win(s).")
            clearScreen()
            GamesLeft -= 1
            if GamesLeft != 0: MessageStop(f"\n You and your opponent get to play {GamesLeft} more game(s)")
        # Loop
            
    print("The trial of games has ended!")
    time.sleep(1)
    MessageStop(Blue+'''We have a winner!''' + reset)
    for resultcount in range(5):
        print(f"The winner of the trial of games of luck and strategy is{"." * resultcount}")
        time.sleep(0.25)
    if resultcount != 4: clearScreen()

    print(f"{PlayerOneName if PlrOnePts > PlrTwoPts else PlayerTwoName}!")
    time.sleep(1)
    MessageStop(f" \nCongratulations {PlayerOneName if PlrOnePts > PlrTwoPts else PlayerTwoName}!")