class Sample:
    def __init__(self, val):
        self.val = val

obj1 = Sample(0)
obj2 = Sample(2)
obj3 = obj1
obj3.val += 1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj3 is obj1)
print(obj1.val, obj2.val, obj3.val)

string1 = "Mary had a little "
string2 = "Mary had a little lamb"
string1 += "lamb"

# print(string1)
# print(string2)
print(string1 == string2, string1 is string2)