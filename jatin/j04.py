class Python : 
    population = 1
    victims = 0 
    def __init__(self) :
        self.length_ft = 3 
        self.__venomous = False

myObj = Python()
print("myObj.population = ",myObj.population)
print("myObj.population = ",myObj.victims)
print("myObj.population = ",myObj.length_ft)
print("myObj.population = ",myObj._Python__venomous)  # dont throw error because of name of class is used to access the private variable
# print("myObj.population = ",myObj.__venomous)  # AttributeError: 'Python' object has no attribute 'venomous'


print(hasattr(Python, 'constriction'))  # True
