import random, time
from UsefulStuff import yellow, Red, green, Blue, reset, clearScreen
from guide import InvalidInput, YesOrNo, NumChoiceWithQuit, NumChoice

def level6_function():
    Youlives = Raphaellives = Mikelives = Jalenlives = Miguellives = 2 # Live
    You = Miguel = Jalen = Mike = Raphael = 0 # Choices ( will take off later)
    PlayersOut = 0
    Colorselection = [Red+"RED"+reset,green+"GREEN"+reset,yellow+"YELLOW"+reset,Blue+"BLUE"+reset]
    Colors = ["","RED","GREEN","YELLOW","BLUE"]
    while True:
        print('''\n Choose your difficulty for Four Corners:''')
        time.sleep(0.5)
        Difficulties = [f"{Blue}Easy (3+ winners){reset}",f"{yellow}Medium (2+ winners){reset}", f"{Red}Hard (1+ winners){reset}"]
        for difficulty in Difficulties:
            print(f"\n {Difficulties.index(difficulty) + 1} - {difficulty}")
            time.sleep(0.25)
        try:
            DifficultyChoice = NumChoice()
        except:
            InvalidInput()
            continue
        if DifficultyChoice == 1:
          print("Alright! Easy difficulty of Four Corners loading!")
          time.sleep(1.5)
          clearScreen()
          break
        elif DifficultyChoice == 2:
          print("Alright! Medium difficulty Four Corners loading!")
          time.sleep(1.5)
          clearScreen()
          break
        elif DifficultyChoice == 3:
          print("Alright! Hard difficulty Four Corners loading!")
          time.sleep(1.5)
          clearScreen()
          break
        else:
          clearScreen()
          InvalidInput()
          continue
        ExplanationSuggestion("4C")
    while True:
      FourColors = random.randrange(1,5)
      Raphael = random.randrange(1,5)
      Mike = random.randrange(1,5)
      Jalen = random.randrange(1,5)
      Miguel = random.randrange(1,5)
      try:
      print('''Pick your color.''')
      time.sleep(0.5)
      for x in range(1,5):
        print('''\n{0} - {1}'''.format(x,Colorselection[x]))
        time.sleep(0.25)
      
      You = NumChoiceWithQuit()
      if You == "Quit":
        return
      elif You == "Redo":
        continue
      if You > 4 or You < 1:
        InvalidInput()
      continue
      print("The color chosen is......")
      time.sleep(0.5)
      print(f"{Colorselection[FourColors - 1]}!!!")
      time.sleep(0.5)
      if Raphaellives > 0:
      if Raphael != FourColors:
        Raphaellivesleft = Blue+"Raphael chose {}, so Raphael is safe"+reset
        print(Raphaellivesleft.format(Colors[Raphael],Raphaellives))
      elif Raphael == FourColors:
        Raphaellives = Raphaellives - 1
        Raphaellivesleft = Red+"Raphael chose {}, so Raphael has {} live(s) left"+reset  
        print(Raphaellivesleft.format(Colors[Raphael],Raphaellives))
      if Raphaellives == 0:
        print(Red+"RAPHAEL IS OUT"+reset)
        PlayersOut = PlayersOut + 1
      if Mikelives > 0:
      time.sleep(0.25)
      if Mike != FourColors:
        Mikelivesleft = Blue+"Mike chose {}, so Mike is safe"+reset
        print(Mikelivesleft.format(Colors[Mike],Mikelives))
      elif Mike == FourColors:
        Mikelives = Mikelives - 1
        Mikelivesleft = Red+"Mike chose {}, so Mike has {} live(s) left"+reset 
        print(Mikelivesleft.format(Colors[Mike],Mikelives))
        if Mikelives == 0:
          print(Red+"MIKE IS OUT"+reset)
          PlayersOut = PlayersOut + 1
      if Youlives > 0:
      time.sleep(0.25)
      if You != FourColors:
        Yourlivesleft = green+"You "+reset+Blue+"chose {}, so "+reset+green+"you "+reset+Blue+"are safe"+reset
        print(Yourlivesleft.format(Colors[You]))
      elif You == FourColors:
        Youlives = Youlives - 1
        Yourlivesleft = green+"You "+reset+Red+"chose {}, so "+reset+green+"You "+reset+Red+ "have {} live(s) left"+reset  
        print(Yourlivesleft.format(Colors[You],Youlives))
        if Youlives == 0:
          print(Red+"YOU ARE OUT"+reset)
      if Miguellives > 0:
      time.sleep(0.25)
      if Miguel != FourColors:
        Miguellivesleft = Blue+"Miguel chose {}, so Miguel is safe"+reset
        print(Miguellivesleft.format(Colors[Miguel]))
      elif Miguel == FourColors:
        Miguellives = Miguellives - 1
        Miguellivesleft = Red+"Miguel chose {}, so Miguel has {} live(s) left"+reset  
        print(Miguellivesleft.format(Colors[Miguel],Miguellives))
        if Miguellives == 0:
        print(Red+"MIGUEL IS OUT"+reset)
        PlayersOut = PlayersOut + 1
      time.sleep(0.25)
      if Jalenlives > 0:
      if Jalen != FourColors:
        Jalenlivesleft = Blue+"Jalen chose {}, so Jalen is safe"+reset
        print(Jalenlivesleft.format(Colors[Jalen]))
      elif Jalen == FourColors:
        Jalenlives -= 1
        Jalenlivesleft = Red+"Jalen chose {}, so Jalen has {} live(s) left"+reset  
        print(Jalenlivesleft.format(Colors[Jalen],Jalenlives))
        if Jalenlives == 0:
          print(Red+"JALEN IS OUT"+reset)
          PlayersOut += 1
      MessageStop()
      if PlayersOut >= 2 and DifficultyChoice == 1: 
        MessageStop(Blue+"YOU WON A GAME OF FOUR CORNERS ON EASY DIFFICULTY!"+reset)
        return "EW"
      elif Youlives == 0 and PlayersOut < 2 and DifficultyChoice == 1: 
        MessageStop(Red+"You lost a game of Four Corners on easy difficulty."+reset)
        return "EL"
      elif PlayersOut >= 3 and DifficultyChoice == 2: 
        MessageStop(Blue+"YOU WON A GAME OF FOUR CORNERS ON MEDIUM DIFFICULTY!"+reset)
        return "MW"
      elif Youlives == 0 and PlayersOut < 3 and DifficultyChoice == 2: 
        MessageStop(Red+"You lost a game of Four Corners on medium difficulty."+reset)
        return "ML"
      elif PlayersOut >=  4 and DifficultyChoice == 3: 
        MessageStop(Blue+"YOU WON A GAME OF FOUR CORNERS ON HARD DIFFICULTY!"+reset)
        return "HW"
      elif Youlives == 0 and PlayersOut < 4 and DifficultyChoice == 3: 
        MessageStop(Red+"You lost a game of Four Corners on hard difficulty."+reset)
        return "HL"

  #Level 6 - Four Corners

  def pvplevel6_function(OnePlayerName,TwoPlayerName):
  Youlives = TwoPlrlives = Mikelives = Jalenlives = Miguellives = 2 # Default value of all lives is 2
  Colorselection = [Red+"RED"+reset,green+"GREEN"+reset,yellow+"YELLOW"+reset,Blue+"BLUE"+reset]
  Colors = ["","RED","GREEN","YELLOW","BLUE"]
  ExplanationSuggestion("4C")
  while True:
    FourColors = random.randrange(1,5)
    Mike = random.randrange(1,5)
    Jalen = random.randrange(1,5)
    Miguel = random.randrange(1,5)
    try:
    clearScreen()
    print('''{}! Choose your color.'''.format(OnePlayerName))
    time.sleep(0.5)
    for x in range(1,5):
      print('''
  {0} - {1}'''.format(x,Colorselection[x]))
      time.sleep(0.25)
    
    You = NumChoiceWithQuit()
    if You == "Quit":
      return
    elif You == "Redo":
      continue
    
    if You > 4 or You < 1:
    InvalidInput()
    continue
    while True:
    try:
      clearScreen()
      print('''{0} chose {1}.\n'''.format(OnePlayerName,Colors[You]))
      time.sleep(1)
      print('''{}! Choose your color.'''.format(TwoPlayerName))
      time.sleep(0.5)
      for x in range(1,5):
      print('''\n {0} - {1}'''.format(x,Colorselection[x]))
      time.sleep(0.25)
      try:
        TwoPlr = NumChoiceWithQuit()
        if TwoPlr == "Quit":
          return
        elif TwoPlr == "Redo":
          continue
      except:
    
    if TwoPlr > 4 or TwoPlr < 1:
      InvalidInput()
      continue
    elif TwoPlr != 0:
      break
    print("The color chosen is......")
    time.sleep(0.5)
    print(f"{Colorselection[FourColors - 1]}!!!")
    time.sleep(0.5)
    if Youlives > 0:
    time.sleep(0.25)
    if You != FourColors:
      Yourlivesleft = "{1} "+reset+Blue+"chose {0}, so "+reset+"{1} "+reset+Blue+"is safe"+reset
      print(Yourlivesleft.format(Colors[You],OnePlayerName))
    elif You == FourColors:
      Youlives = Youlives - 1
      Yourlivesleft = "{1} "+Red+"chose {0}, so "+reset+"{1} "+Red+"has {2} live(s) left"+reset   
      print(Yourlivesleft.format(Colors[You],OnePlayerName,Youlives))
      if Youlives == 0:
      Yourlivesleft = "{} "+Red+"IS OUT"+reset
      print(Yourlivesleft.format(OnePlayerName))
    if Mikelives > 0:
    time.sleep(0.25)
    if Mike != FourColors:
      Mikelivesleft = Blue+"Mike chose {}, so Mike is safe"+reset
      print(Mikelivesleft.format(Colors[Mike],Mikelives))
    elif Mike == FourColors:
      Mikelives = Mikelives - 1
      Mikelivesleft = Red+"Mike chose {}, so Mike has {} live(s) left"+reset 
      print(Mikelivesleft.format(Colors[Mike],Mikelives))
      if Mikelives == 0:
      print(Red+"MIKE IS OUT"+reset)
    if TwoPlrlives > 0:
    time.sleep(0.25)
    if TwoPlr != FourColors:
      TwoPlrlivesleft = "{1} "+Blue+"chose {0}, so "+reset+"{1} "+Blue+"is safe"+reset
      print(TwoPlrlivesleft.format(Colors[TwoPlr],TwoPlayerName))
    elif TwoPlr == FourColors:
      TwoPlrlives = TwoPlrlives - 1
      TwoPlrlivesleft = "{1} "+Red+"chose {0}, so "+reset+"{1} "+Red+"has {2} live(s) left"+reset  
      print(TwoPlrlivesleft.format(Colors[TwoPlr],TwoPlayerName,TwoPlrlives))
      if TwoPlrlives == 0:
      TwoPlrlivesleft = "{} "+Red+"IS OUT"+reset
      print(TwoPlrlivesleft.format(TwoPlayerName))
    if Miguellives > 0:
    time.sleep(0.25)
    if Miguel != FourColors:
      Miguellivesleft = Blue+"Miguel chose {}, so Miguel is safe"+reset
      print(Miguellivesleft.format(Colors[Miguel]))
    elif Miguel == FourColors:
      Miguellives = Miguellives - 1
      Miguellivesleft = Red+"Miguel chose {}, so Miguel has {} live(s) left"+reset  
      print(Miguellivesleft.format(Colors[Miguel],Miguellives))
      if Miguellives == 0:
      print(Red+"MIGUEL IS OUT"+reset)
    time.sleep(0.25)
    if Jalenlives > 0:
    if Jalen != FourColors:
      Jalenlivesleft = Blue+"Jalen chose {}, so Jalen is safe"+reset
      print(Jalenlivesleft.format(Colors[Jalen]))
    elif Jalen == FourColors:
      Jalenlives = Jalenlives - 1
      Jalenlivesleft = Red+"Jalen chose {}, so Jalen has {} live(s) left"+reset  
      print(Jalenlivesleft.format(Colors[Jalen],Jalenlives))
      if Jalenlives == 0:
      print(Red+"JALEN IS OUT"+reset)
    MessageStop()
    if Youlives > 0 and TwoPlrlives == 0:
      MessageStop("{0} has lasted longer than {1} in Four Corners!".format(OnePlayerName,TwoPlayerName))
      return "W"
    elif Youlives == 0 and TwoPlrlives > 0:
    MessageStop("{0} has lasted longer than {1} in Four Corners!".format(TwoPlayerName,OnePlayerName))
    return "L"
    elif Youlives == 0 and TwoPlrlives == 0:
        MessageStop("{0} and {1} has both been eliminated, so the game will now reset.".format(TwoPlayerName,OnePlayerName)) 
        Youlives = TwoPlrlives = Mikelives = Jalenlives = Miguellives = 2
  #Level 6 - Four Corners