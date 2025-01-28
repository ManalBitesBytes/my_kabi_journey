class Body_Measures():
    def __init__(self, height, weight):
        # one under score indicates that the attribute or method should not be accessed directly from outside the class
        #protected
        self._height = height
        # two underscores means hat the attribute cannot be accessed from outside the class
        # private
        self.__weight = weight

    def IncrementHeight(self):
        self._height += 1

    def IncrementWeight(self):
        self.__weight += 1

    #use property decorator as a getter for private attributes
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def weight(self):
        return self.__weight

    #you can make read only attribute by defining a getter only
    @weight.setter
    def weight(self, value):
        if value >= 0: #we can use property to add some validation
            self.__weight = value
        else:
            print("Weight must be positive")