#
# Kristofer Hughes
#

#
# Question 1
#

import sys

from tkinter import *

class Buttons:
    root=Tk()
    frame=Frame(root)
    frame.pack()
    EButton=Button(frame, text='Emergency!',fg='red',width=100,padx=3,command=lambda:print('EMERGENCY!'))
    EButton.pack(side=TOP)
    quitButton=Button(frame, text="QUIT!",fg='black',command=frame.quit)
    quitButton.pack(side=BOTTOM)
    root.mainloop()
    root.destroy()

        


#
# Question 2
#


class Card(object):
    def __init__(self, rank, suit):
        FACE_CARD = {11: 'J', 12: 'Q', 13: 'K'}
        self.suit = suit
        self.rank = rank if rank <=10 else FACE_CARD[rank]
    def __str__(self):
        return "%s%s " % (self.rank, self.suit)
    
class Deck(object):
    def __init__(self,numCards=10):
        self.cards = []
        for s in ['S', 'D', 'C', 'H']:
            for r in range(1, numCards):
                c=Card(r, s)
                self.cards.append(c)
import random 
class Hand(object):
# This sets up a deck prior to a deal
# You do not need to add anything to this
# unless you want to
    def __init__(self):
        self.d=Deck()
        self.deckCards=self.d.cards

# This code takes cards from the deck
# randomly and saves them to a "hand"
# It removes from the deck any cards
# it uses
# It prints out the cards as they
# are being dealt
    def getHand(self,numInHand=5):
        random.shuffle(self.deckCards)
        self.existinghand=self.deckCards[0:numInHand]
        print("Dealing Cards...")
        for i in self.existinghand:
            print(i)
            self=i
            
            
            
            

# This code shows the cards beginning
# with the last dealt (the top) and
# ending with the first dealt (the bottom)
    def sneakPeek(self):
        for i in self:
            print (i)
            
    def __iter__(self):
        self.index=-1
        return self

    def __next__(self):
        try:
            endres=self.existinghand[self.index]
            self.index=self.index-1
            return endres
        except IndexError:
            raise StopIteration
    
# Hand1 and Hand2 are instances of Hand    
# This code compares each card in hand1
# with each card in hand2 in order from
# last dealt to first dealt
# The cards are compared based only on
# rank (not suit)
# If the ranks are equal, no one wins.
# Otherwise, either hand1 or hand2 wins
# with a print as shown in the sample
# based on which rank is larger
# A count is kept for each hand's wins
# At the end a winner is declared and
# the respective number of wins is
# shown. See the sample output

def playWar(hand1,hand2):
    warhand_1=[]
    warhand_2=[]
    h1wincount = 0
    h2wincount = 0
    for i in hand1:
        warhand_1.append(i)
    for i in hand2:
        warhand_2.append(i)
    for i in range(len(warhand_1)):
        card1=(str(warhand_1[i])[0])
        card1=int(card1)
        card2=(str(warhand_2[i])[0])
        card2=int(card2)
        if card1>card2:
            print("{} beats {} . Hand 1 wins".format(warhand_1[i], warhand_2[i]))
            h1wincount+=1
        elif card1<card2:
            print("{} beats {} . Hand 2 wins".format(warhand_2[i], warhand_1[i]))
            h2wincount+=1
        elif card1==card2:
            print("It's a tie. Nobody wins.")
    if h1wincount>h2wincount:
        print("Hand 1 wins this game {} to {}".format(h1wincount, h2wincount))
    elif h2wincount>h1wincount:
        print("Hand 2 wins this game {} to {}".format(h2wincount, h1wincount))
    elif h1wincount==h2wincount:
        print("Tied. {} to {}".format(h1wincount,h2wincount))



