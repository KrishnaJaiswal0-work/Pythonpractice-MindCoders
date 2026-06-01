# class Student:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#         self.grade = ""

# shayampal = Student()
# print(shayampal)

# shayampal.name = "shayampal Kumar"
# shayampal.age = 54
# shayampal.gender = "Male"
# shayampal.grade = "12th"

# print(shayampal.name)
# print(shayampal.age)
# print(shayampal.gender)
# print(shayampal.grade)


class Student:
    def __init__(self, name, age, gender, grade):
        self.name = name 
        self.age = age
        self.gender = gender
        self.grade = grade

    def printDetails(self):
        print("Name:", self.name )
        print("Age:",self.age )
        print("Gender:",self.gender)
        print("Grade:",self.grade)


Ironman = Student("Lanka Adhipati" , 101, "Male", "PHD_in_Gyan")
print(Ironman)


Ironman.printDetails()