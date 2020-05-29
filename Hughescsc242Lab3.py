# Kristofer Hughes
#I collaborated with Joseph Kovacevic. We worked together on all 3 problems, and helped eachother debug the other's code.

#1
#Subclass of list tat iterates over odd indices
class OddList(list):
    
    def __init__(self, labLst=[]):
        self.labLst = labLst
        ListIterator.__init__(self, labLst)
        

    def __iter__(self):
        newLst=iter(self.labLst[1::2])
        
        

class ListIterator(OddList):
    def __init__(self,labLst):
        labLst2 = self.labLst[1::2]
        

    def __next__(self):
        done = True
        while done:
            for idx, elem in enumerate(labLst):
                thiselem = elem
                nextelem = self.labLst[(idx + 1) % len(self.labLst)]
                done = False
        
#2
#Modified Animal class with InvalidAge exception for negative ages
class InvalidAge(Exception):
    
    def __init__(self):
        Exception.__init__(self, "Negative number detected")
    

class Animal(object):

    #modify __init__
    def __init__(self, newSpecies="default", newLanguage="default", newAge=0):
        self.species = newSpecies
        self.language = newLanguage
        self.age = newAge
        if self.age < 0:
            raise InvalidAge

    def __repr__(self):
        return "Animal('{}','{}',{})".format(self.species, self.language, self.age)

    def __eq__(self, otherAnimal):
        return self.species == otherAnimal.species and self.language == otherAnimal.language and self.age == otherAnimal.age

    def setSpecies(self, newSpecies):
        self.species = newSpecies

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    #modify setAge()
    def setAge(self, newAge):
        if self.age < 0:
            raise InvalidAge
        else:
            self.age = newAge

    def speak(self):
        if self.age < 0:
            raise InvalidAge
        else:
            print("I am a {} year-old {} and I{}.".format(self.age, self.species, self.language))

#3
#Modified processAnimals function with InvalidAge exception
def processAnimals(file):
    animalList = []

    inFile = open(file)
    lineList = inFile.readlines()
    inFile.close()

    #modify the code in loop to handle Animals being made with negative ages (refer to lab for output examples)
    for line in lineList:
        try:
            data = line.strip('\n').split(',')
            newAnimal = Animal(data[0], data[1], eval(data[2]))
            animalList.append(newAnimal)
            newAnimal.speak()
        except:
            if line in lineList < 0:
                raise InvalidAge
            
            
    return animalList
