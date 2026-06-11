class Python:
    popultion = 1 
    victims = 0
    def __init__(self):
        self.length = 3
        self.__venomous = False

myObj = Python()
print("myObj.population:", myObj.popultion)
print("myObj.victims:", myObj.victims)
print("myObj.length:", myObj.length)
print("myObj.venomus:", myObj.__venomous) #private variable
print("myObj.venomou: ", myObj._Python__venomous) #ACCESS PRIVATE VARIABLE