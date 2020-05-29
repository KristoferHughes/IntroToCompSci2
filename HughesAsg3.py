#Comp sci assignment 3

# Kristofer Hughes

# I collaborated with Joseph Kovacevic. We worked on getting started on the first two classes, and then helped eachother with errors and debugging.

import random

class Die(object):

    def __init__(self, sides=6):
        self.sides = sides
        self.current = random.randrange(1,self.sides)

    #This function returns current
    def get(self):
        '''returns current'''
        return self.current

    #This function rerolls, then returns current
    def roll(self):
        '''rerolls, then returns current'''
        self.current=random.randrange(1,sides)
        return self.current

    #This function returns sides
    def numSides(self):
        '''returns sides'''
        return self.sides

    #This function returns current
    def __repr__(self):
        '''returns current'''
        return "[{}]".format(self.current)

    #This function returns current
    def __str__(self):
        '''returns current'''
        return "[{}]".format(self.current)


class Craps(Die):

    #This function sets variables and rolls the first round of craps. if the player rolls 7 or 11, the player wins. if the player rolls a 2, 3, or 12, they lose. otherwise, they are told to play again
    def __init__(self):
        '''sets variables and rolls the first round of craps. if the player rolls 7 or 11, the player wins. if the player rolls a 2, 3, or 12, they lose. otherwise, they are told to play again'''
        self.die1 = 6
        self.die2 = 6
        self.total = random.randrange(1,self.die1) + random.randrange(1,self.die2)
        if self.total == 7 or self.total == 11:
            #if the total equals 7 or 11, the user wins
            print("Throw total: {}. You win!".format(self.total))
        elif self.total == 2 or self.total == 3 or self.total == 12:
            #if the total is 2, 3, or 12, the user loses
            print("Throw total: {}. You lose!".format(self.total))
        else:
            #if it's neither of the above, the user is advised to play again
            print("Throw total: {}. Throw for a point!".format(self.total))

    #This function rolls the next round of the craps game. If the player rolls a 7, the player loses. If the player rolls the same value as the initial roll, the player wins. Otherwise, they are told to play again
    def forPoint(self):
        '''rolls the next round of the craps game. If the player rolls a 7, the player loses. If the player rolls the same value as the initial roll, the player wins. Otherwise, they are told to play again'''
        self.total2 = random.randrange(1,self.die1) + random.randrange(1,self.die2)
        if self.total2 == 7:
            #if the total equals 7, the user loses
            print("Throw total: {}. You lose!".format(self.total2))
        elif self.total2==self.total:
            #if total2 is the same as total, the user wins
            print("Throw total: {}. You win!".format(self.total2))
        else:
            #if it's neither of the above, the user is advised to play again
            print("Throw total: {}. Throw for a point!".format(self.total2))

            



class Collection(list):

    def __init__(self, mxSize=10, value=[]):
        self.maxSize = mxSize
        self.value = value


    #This function checks to see if newItem is already in the list
    def __contains__(self,newItem):
        '''checks to see if newItem is already in the list'''
        falsehood=0
        if newItem in self.value:
            #checks if item is in list
            falsehood=True
        else:
            falsehood=False
        return falsehood

    #This function hecks to see if the max size of the list has been reached and if newItem is already in the list, if neither of these have occurred, the newItem is added to the list
    def add(self, newItem):
        '''checks to see if the max size of the list has been reached and if newItem is already in the list, if neither of these have occurred, the newItem is added to the list'''
        truth=0
        if len(self.value) == self.mxSize:
            truth=False
        elif self.__contains__(newItem) ==True:
            #calls __contains__ function to check if newItem is already in value
            truth=False
        else:
            self.value.append(newItem)
            truth=True
        return truth

    #This function returns length of the list
    def size(self):
        '''returns length of the list'''
        return len(self.value)

    #This function returns the list
    def __repr__(self):
        '''returns list'''
        return "{}".format(self.value)

    #This function returns the list
    def __str__(self):
        '''returns list'''
        return "{}".format(self.value)
    

    
        

    

                 
                 
