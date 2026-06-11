class Example : 
    counter = 0 
    def __init__(self, val = 1) :
        Example.counter +=1    
        if val %2 == 0 :
            self.a = 1

        else :
            self.b = 2



# example_object_1 = Example()
# example_object_2 = Example(2)
# example_object_3 = Example(3)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)

# example_object = Example(8)
# try :
#     print(example_object.a)
# except AttributeError as e:

#     try :
#         print(example_object.b)
#     except AttributeError as e:
#         print("the error has occured! silently handling the error ")

example_object = Example(6)
if hasattr(example_object, 'a'):
    print("a = ",example_object.a)

if hasattr(example_object, 'b'):
    print("b = ",example_object.b)

print(hasattr(example_object, 'a'))  # True
print(hasattr(example_object, 'b'))  # False