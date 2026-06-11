import csv

records = [

    ['Name', "Age", 'Math_marks', 'Sci_marks', 'Eng_marks'],
    ['Rampal', '35', '67', '53', '98'],
    ['Bahubali', '50', '45', '74', '10'],
    ['Raju', '86', '76', '20', '48'],
    
]

with open('FileHandling/students.csv1', 'w',  newline = '') as f:
    csv.writer(f).writerows(records)

name = input("Enter Student Name for Search :")    
found = False

with open('FileHandling/students.csv1', 'r') as f:
    for row in csv.DictReader(f):
        if row["Name"] == name:
            print(f'Found {name}')
            print(f'{row['Name']}: {row["Age"]}, Marks: Maths = ({row['Math_marks']}) Science = ({row['Sci_marks']}) Endlish = ({row['Eng_marks']})' )
            found = True
            break

if not found:
         print("Student not found")