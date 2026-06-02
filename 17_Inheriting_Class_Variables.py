class Super:
    supVar = 1

class Sub(Super):
    subVar = 3 

obj = Sub()
print(obj.supVar)  
print(obj.subVar)     