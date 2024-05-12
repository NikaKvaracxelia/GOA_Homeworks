names = ["Nika", "Gio", "Dato, Luka, milo"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])


names = ["Nika", "Gio", "Dato, Luka, milo"]

for i in names:
    print(i)


numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print(number)


numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0
multiple = 1

for num in numbers:
    sum = sum + num
    multiple = multiple * num

print(numbers,"sum of these numbers is",sum)
print(numbers, "multiple of these numbers is", multiple)


numbers = [1,2,3,4,5,6,7,8,9,10]

even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum = even_sum + num
        print(num)

print(even_sum)

numbers = [1,2,3,4,5,6,7,8,9,10]

odd_sum = 0
odd_multiple = 1

for num in numbers:
    if num % 2 != 0:
        odd_sum = odd_sum + num
        odd_multiple = odd_multiple * num

print("Odd numbers sum", odd_sum)
print("Odd numbers multiple", odd_multiple)


name = "Nika"

for char in name:
    print(char)




