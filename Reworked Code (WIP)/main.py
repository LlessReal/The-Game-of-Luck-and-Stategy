from welcome import Title
from MenuScreen import MenuScreen
from PVC import PVC
from PVP import PVP

def main():
    Title() # Welcome !!!!!
    while True:
        MenuResults = MenuScreen()
        if MenuResults == "Quit":
            exit("Alr cya lol")
        if MenuResults == "Vs. Computer":
            PVC()
        elif MenuResults == "PVP":
            PVP()
        # More modes in the future !!!!

if __name__ == "__main__":
    main()