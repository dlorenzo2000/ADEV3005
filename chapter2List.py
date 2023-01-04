# Date: Tue Jan03/23
# Created by: Dean Lorenzo
# Purpose: Putting lists to work

# literal list
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = "Milliways"
# for letter in word:
#     if letter in vowels:
#         print(letter)

# undeclared list
# found = []
# print(len(found))

# append to undeclared list
# found.append('a')
# print(len(found))

# found.append('e')
# found.append('i')
# found.append('o')

# if 'u' not in found:
#     found.append('u')

# print(found)

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
 

