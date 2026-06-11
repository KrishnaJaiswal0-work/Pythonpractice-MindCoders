string = "Hello, How are you doing today?"
# Count vowels in the string
# Print you from the string
# Print the string in reverse order/
non_palin , palin = "abcdef", "axttxa"
# Check if the string is palindrome or not



Vowel = {'a', 'e', 'i', 'o', 'u'}

count = 0
for i in string.lower():
    if i in Vowel:
        count += 1
print(count)

print(string[15:19])
print(string[::-1])

