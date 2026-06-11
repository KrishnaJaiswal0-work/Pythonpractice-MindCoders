text = '    Hello Python Programmer     '
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.strip())

print()
print('Python' in text)
print('python' in text)
print(text.find("Hello"))
print(text.find("programmer"))
print(text.count('o'))


# Replace
print(text.replace('Python', 'Anacoda'))

# Split and Join
csv = 'Rahul,22,Indore,Engineer'
text1 = csv.split(',')
print(text1)
print(text1[2])
text2 = '  |  '.join(text1)
print(text2)

# Check content
print('1234'.isalnum())
print('12345'.isdigit())
print('Python'.isalpha())
print('      '.isspace())

#  Start/End check
print(text.startswith('   '))
print(text.startswith('Hello'))
print(text.endswith('   '))