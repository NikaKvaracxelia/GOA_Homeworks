def even_indices_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        if i % 2 == 0:  
            total += numbers[i]
    return total

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(check_even_odd(7))  # odd
print(check_even_odd(10)) # even


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(11)) # True
print(is_prime(15)) # False


def capitalize_names(names):
    capitalized_names = [name.capitalize() for name in names]
    return capitalized_names

names = ["nika", "gio", "nini"]
print(capitalize_names(names))


