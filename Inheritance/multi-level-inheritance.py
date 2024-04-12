class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = 'Tonewood'

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print('This guitar contains of {} strings. It is made of {} and it can play {} keys.'
              .format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))
        
guitar = Guitar()