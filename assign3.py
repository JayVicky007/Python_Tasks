user_input = input("Enter a string: ")

def count_characters(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

output = count_characters(user_input)
print(output)
