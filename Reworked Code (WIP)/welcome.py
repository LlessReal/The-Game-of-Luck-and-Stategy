import sys
from UsefulStuff import Blue, reset, yellow, clearScreen
from time import sleep
def Title():
    clearScreen()
    print(f"{Blue}WELCOME{reset}\n")
    WelcomeText = "TO THE GAME OF LUCK AND STRATEGY!"
    sleep(1)
    for Letter in WelcomeText:
        sys.stdout.write(Letter); sys.stdout.flush(); sleep(0.05)
    sleep(1)
    input(yellow + "\n(Press Enter to Play)\n" + reset)
    clearScreen()