school_dict = {}

while True:
    name = input("Enter Student's name : " )
    if name  == "": 
        break
    score = int(input(f"Enter {name}'s score:"))

    if score not in range(1, 11):
        break
    if name in school_dict:
        school_dict[name] += (score, )
    else:
        school_dict[name] = (score, )

print(school_dict)

for name, mark in school_dict.items():
    sum = 0
    for m in mark:
        sum += m
    print(name , "->" , sum / len(mark))