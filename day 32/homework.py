def manual_index(numbers_list, search_value):
    for index, value in enumerate(numbers_list):
        if value == search_value:
            return index
    return -1

numbers = [1, 3, 5, 7, 9]
search_value = 5
print("important index:", manual_index(numbers, search_value))


def manual_max(numbers_list):
    max_value = numbers_list[0]
    for number in numbers_list:
        if number > max_value:
            max_value = number
    return max_value

def manual_min(numbers_list):
    min_value = numbers_list[0]
    for number in numbers_list:
        if number < min_value:
            min_value = number
    return min_value

numbers = [3, 7, 2, 9, 1, 5]
print("maximum value:", manual_max(numbers))  
print("minimum value:", manual_min(numbers))




def manual_pop(input_list, index):
    if index < 0 or index >= len(input_list):
        print("incorrect: put the right index.")
        return input_list

    new_list = input_list[:index] + input_list[index+1:]
    return new_list

my_list = [1, 2, 3, 4, 5]
index_to_remove = 2
new_list = manual_pop(my_list, index_to_remove)
print("new list:", new_list)