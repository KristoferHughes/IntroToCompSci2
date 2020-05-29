from tkinter import Tk, Label, Entry, Button, END
from random import *

# Kristofer Hughes

class Craps(Tk):
        

    #set up the main window
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Play Craps')
        self.new_game()
        self.make_widgets()



 

    #when a new game is started, the firstRoll will start at 0
    def new_game(self):
        self.firstRoll = 0
        
    #create and place the widgets in the window
    def make_widgets(self):
        Label(self, text="Die 1").grid(row=0, column=0, columnspan=1)
        Label(self, text="Die 2").grid(row=0, column=1, columnspan=1)

        self.die1Ent = Entry(self) #entry field for die 1
        self.die2Ent = Entry(self) #entry field for die 2
        self.die1Ent.grid(row=1, column=0, columnspan=1)
        self.die2Ent.grid(row=1, column=1, columnspan=1)

        Label(self, text="First roll").grid(row=2, column=0, columnspan=1)
        Label(self, text="Result").grid(row=2, column=1, columnspan=1)

        self.firstRollEnt = Entry(self) #entry field for the first roll
        self.resultEnt = Entry(self) #entry field the result of the current roll
        self.firstRollEnt.grid(row=3, column=0, columnspan=1)
        self.resultEnt.grid(row=3, column=1, columnspan=1)

        Button(self, text="Roll the dice!", command=self.play).grid(row=4, column=0)

    #complete the implementation of play()
    def play(self):
        self.die1Ent.delete(0, END)
        self.die2Ent.delete(0, END)
        self.firstRollEnt.delete(0, END)
        self.resultEnt.delete(0, END)
        playdie1=randrange(0,6)
        playdie2=randrange(0,6)
        firstRollres=playdie1+playdie2
        self.die1Ent.insert(0,str(playdie1))
        self.die2Ent.insert(0,str(playdie2))
        self.firstRollEnt.insert(0,str(firstRollres))
        if self.firstRollEnt == 7 or 11:
            self.resultEnt.insert(0,"You won! Play again?")
        elif self.firstRollEnt == 2 or 3 or 12:
            self.resultEnt.insert(0,"You lost. Play again?")
        else:
            self.resultEnt.insert(0,"You need to roll again.")
        
       
                
       
Craps().mainloop()
