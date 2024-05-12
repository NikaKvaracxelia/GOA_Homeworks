# def print_name(name, amount):
#     for i in range(amount):
#         print(name)


# print_name("luka", 5)

# print_name("Nika", 10)

# print_name("Gio", 2)



# def print_range(start, end):
#     for num in range(start, end + 1):
#         print(num)

# print_range(3, 9)



# def calculate_sum(start, end):
#     return sum(range(start, end + 1))

# result = calculate_sum(3, 9)
# print("result:", result)



# def calculate_average(start, end):
#     numbers = []
    
#     for num in range(start, end + 1):
#         numbers.append(num)
    
#     return sum(numbers) / len(numbers)

# result = calculate_average(3, 9)
# print("Arithmetic average of the numbers added to the list:", result)



# def print_char_at_index(name, index):
#     if index < len(name):
#         print("The letter at the index of the string:", name[index])
#     else:
#         print("Incorrect: Wrong index")

# print_char_at_index("Python", 3)



# def print_final_value():
#     x = 10  
#     print("Final value:", x)

# print_final_value()
# print(print_final_value)


def sum_of_two_numbers(a, b):
    return a + b

def print_sum_result(a, b):
    result = sum_of_two_numbers(a, b)
    print("The sum of", a, "and", b, "is:", result)

a = 5
b = 7
print_sum_result(a, b)



def sum_of_list(numbers):
    total = sum(numbers)  
    return total

def print_list_sum(numbers):
    result = sum_of_list(numbers)  
    print("The sum of the numbers in the list is:", result)

numbers = [1, 2, 3, 4, 5]
print_list_sum(numbers)



def add_even_indices(name):
    new_name = ""
    for i in range(len(name)):
        if i % 2 == 0: 
            new_name += name[i]
    return new_name

def print_modified_name(name):
    modified_name = add_even_indices(name)
    print("Modified name:", modified_name)

name = "Nika"
print_modified_name(name)


print("join goa")
print("join goa")
print("join goa")