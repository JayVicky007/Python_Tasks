print("Enter the integers to be added: ")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
num4 = int(input("Enter the fourth integer: "))
num5 = int(input("Enter the fifth integer: "))

def calc_sum(*args):
    for num in args:
        total_num = sum(num)
    return total_num
total = calc_sum([num1, num2, num3, num4, num5])
print(total)





# def add_nums(*args):
#     total_sum = 0
#     for num in args:
#         total_sum = total_sum + num
#     return total_sum
# total = add_nums(5,6,7,9)
# print(total)
