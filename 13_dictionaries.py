dictionary = {
"cat": "chat",
"dog": "chien",
"horse": "cheval"
}
phone_number = {'boss': 5551234567, 'Suzy': 2265783407}
empty_dictionay = {}

print(dictionary)
print(type(dictionary))
print(phone_number)
print(type(phone_number))
print(empty_dictionay)
print(type(empty_dictionay))

print(dictionary['cat'])
print(phone_number['Suzy'])
# print(phone_number['president'])

words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print("-----",word, "is not in dictionary", "-----")