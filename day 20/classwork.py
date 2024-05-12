# ამოცანა 1
#შექმენით პროგრამა, რომელსაც გადასცემთ სიას, სადაც გექნებათ მთელი რიცხვები. თქვენი დავალებაა, რომ ამ სიის ორი მინიმალური რიცხვის ჯამი დააბრუნოთ: ([5, 8, 12, 18, 22]), 13), ([7, 15, 12, 18, 22]), 19), ([25, 42, 12, 18, 22]), 30)

numbers = [203, 43, 3253, 15, 84]

smallest_numbers = sorted(numbers)[:2]
sum_of_smallest = sum(smallest_numbers)

print(sum_of_smallest)


#ამოცანა 2
#შექმენით პროგრამა რომელსაც გადასცემთ მთელი რიცხვების სიას. შემდეგ უნდა მოახდინოთ გაფილტვრა: ახალ სიაში გადაიტანოთ მარტო ლუწი რიცხვები. ბოლოს კი დააბრუნოთ ახალი სია. test cases: [1, 2, 3, 4] -> [2, 4]

number_list = [1, 2, 3, 4]
even_numbers = []

for number in number_list:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


#ამოცანა 3
def index(numbers):
    even_num = 0
    odd_num = 0
    
    for i in range(len(numbers)):
        if i % 2 == 0:
            even_num += numbers[i]
        else:
            odd_num += numbers[i]
    

    new_list = [even_num, odd_num]
    
    return new_list

tests = [
    [80],
    [100, 50],
    [50, 60, 70, 80],
    [13, 27, 49],
    [70, 58, 75, 34, 91]
]

for test in tests:
    result = index(test)
    print(result)



print("join goa")
print("join goa")