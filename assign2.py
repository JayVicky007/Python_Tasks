def isVowel(word):
    letter = ""
    
    for char in word:
        if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
            letter += char
    return letter

user_input = input("Enter a word: ")
vowels = isVowel(user_input)
print(vowels)



# def isVowel(word):
#     letter = ""
    
#     for char in word:
#         if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
#             letter += char
#     return letter

# vowels = isVowel("Ballerina")
# print(vowels)



