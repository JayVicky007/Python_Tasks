def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

user_input = input("Enter a list of numbers (space-separated): ")
numbers = [int(num) for num in user_input.split()]
result = find_largest_number(numbers)
print(result)