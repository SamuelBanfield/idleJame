import random

class GameState:
    def __init__(self):
        # Just populating with some random fields for now
        self.fields = [CropField(), CropField(), LivestockField()]
        
    def update(self):
        # Handles the by tick updates, could only call once per second?
        pass

class Field:
    ''' Dont use this class directly, only use its children '''
    def __init__(self):
        pass

    def update(self):
        # You can overwrite this so that different fields update differently
        pass

    def __str__(self):
        # This method gets called when you try to print() a field
        return "Field: Should never be used directly"

class CropField(Field):
    def __init__(self):
        # Because these inherit from Field, we call the __init__ function on field
        Field.__init__(self)
        self.animalNumber = 0
        self.animalType = "sheep"

    def __str__(self):
        return "A crop field"

class LivestockField(Field):
    def __init__(self):
        Field.__init__(self)
        self.cropLevel = 0
        self.cropType = "wheat"

    def __str__(self):
        return "A livestock field"