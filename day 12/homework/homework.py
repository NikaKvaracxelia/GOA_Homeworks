budget = int(input("What is your budget :"))
cost = int(input("enter price for this item :"))
if budget >= cost:
    print("you have bought this item")
else:
    print("Sorry,you do not have enough money to buy this item")


real_password = "Nika420"

password = input("Please enter your password: ")

while password != real_password:
    password = input("Please enter your password again: ")
    if password == real_password:
        print("You have logged in")
    else:
        print("the passord is incorrect, please try again :")

start = int(input("Please enter starting value: "))
end = int(input("Please enter ending value: "))
step = int(input("Please enter step value: "))

for i in range(start,end,step):
    print(i)

s1 = int(input("Please enter first side: "))
s2 = int(input("Please enter second side: "))
s3 = int(input("Please enter third side: "))


valid = (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2)

while valid != True:
    s1 = int(input("Please enter first side: "))
    s2 = int(input("Please enter second side: "))
    s3 = int(input("Please enter third side: "))

    valid = s1 + s2 > s3

num1 = int(input("Please enter first number: "))
operation = input("Please enter operation (+,-,*,/): ")
num2 = int(input("Please enter second number: "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("operation is not valid")