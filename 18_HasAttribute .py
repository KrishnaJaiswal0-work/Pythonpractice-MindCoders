
class ExampleClass:
    a = 1 
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
example_object = ExampleClass(1)
print(example_object.a)
 
if hasattr(example_object, 'b'):
    print(example_object.b)
class ExampleClass:
    attr = 1
print(hasattr(ExampleClass, 'a'))
print(hasattr(ExampleClass, 'b'))
