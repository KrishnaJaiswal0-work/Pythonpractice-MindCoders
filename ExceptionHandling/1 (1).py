# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__frist = val
#         ExampleClass.counter += 1

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_3 = ExampleClass(4)


# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)


class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        ExampleClass.counter += 1
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

obj = ExampleClass(2)
# print(obj.a)
# print(obj.b)

try:
    print("a = ",obj.a)
except AttributeError:
    try:
        print("b = ",obj.b)
    except AttributeError:
        print("The exception is successfully handled")
        