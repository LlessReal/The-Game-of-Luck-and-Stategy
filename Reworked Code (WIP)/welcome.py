import time, sys
from UsefulStuff import Blue, reset, yellow, clearScreen

def Title():
    clearScreen()
    print(f"{Blue}WELCOME{reset}\n")
    WelcomeText = "TO THE GAME OF LUCK AND STRATEGY!"
    time.sleep(1)
    for WelcomeLetter in WelcomeText:
        sys.stdout.write(WelcomeLetter)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    input(yellow + "\n(Press Enter to Play)\n" + reset)
    clearScreen()