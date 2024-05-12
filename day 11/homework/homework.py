for i in range(1,51):
    if i % 5 == 0:
        print(i)

for i in range(2,21):
    if i % 2 ==0:
        print(i)

result = 1
for i in range (5,11):
    result *= result * i
    print(i)

num = int(input("Please enter your number :"))
result = 1
for i in range(1, result + 1):
    result *= i
print(num,result)


num = int(input("Please enter your number: "))
if num % 2 == 0:
    num /= 2
print(num)


num = 10
while num > 0:
    print(num)
    num -= 1


user = int(input("enter your name or quit: "))
while user != "quit":
    user = int(input("enter your name or quit: "))


num1 = 10
num2 = 21
while num1 < num2:
    if num1 % 2 == 0:
        print(num1)
        num1 += 1


user = int(input("enter your number: "))
while user < 0:
    user = int(input("enter your number: "))
    
num = 1
while num < 10:
    print(i*i)
    num += 1
    