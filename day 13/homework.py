for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


number = int(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    print("ეს რიცხვი დადებითია")
elif number < 0:
    print("ეს რიცხვი უარყოფითია")
else:
    print("ეს რიცხვი ნულოვანია")


for i in range(2, 101, 2):
    print(i)


total = 0
number = 1

while number <= 100:
    total += number
    number += 1

print("ყველა რიცხვის ჯამი 1-დან 100-მდე არის:", total)


day_number = int(input("შეიყვანეთ რიცხვი 1-დან 7-ის ჩათვლით: "))

if day_number == 1:
    print("ორშაბათი")
elif day_number == 2:
    print("სამშაბათი")
elif day_number == 3:
    print("ოთხშაბათი")
elif day_number == 4:
    print("ხუთშაბათი")
elif day_number == 5:
    print("პარასკევი")
elif day_number == 6:
    print("შაბათი")
elif day_number == 7:
    print("კვირა")
else:
    print("ასეთი რიცხვი არ არსებობს")


number = int(input("შეიყვანეთ რიცხვი: "))

if number == 0:
    print("რიცხვი ნულია")
elif number % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")

