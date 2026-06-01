pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
}

print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

del pol_eng_dictionary["zamek"]
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

pol_eng_dictionary.clear()
print(pol_eng_dictionary)
print(len(pol_eng_dictionary))

del pol_eng_dictionary
print(pol_eng_dictionary)