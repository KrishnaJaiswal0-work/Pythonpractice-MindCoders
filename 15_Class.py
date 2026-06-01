class ThisIsMyFirstClass:
    name = "jatin"
    age = 24

    def getname(self):
        print(self.name)
        

firstObject = ThisIsMyFirstClass()    #CONSTRUCTOR
print(firstObject)

firstObject.getname()
print(firstObject.name)

# class Student:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.gender