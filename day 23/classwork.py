from turtle import *
# chad way
width(7)
speed(20)
for i in range(4):
    forward(200)
    left(90)

penup()
goto(-400,0)
pendown()

for i in range(4):
    forward(200)
    left(90)
         
penup()
goto(0,-300)
pendown()

for i in range(4):
    forward(200)
    left(90)


penup()
goto(-400,-300)
pendown()

for i in range(4):
    forward(200)
    left(90)


exitonclick()

# def greet():
#     print("hello nika")

# greet()
# greet()
# greet()
# greet()


# def add(number1,number2):
#     print(number1 + number2)

# add(145,24)


#gigachad way

width(7)
speed(20)

def draw_square():
    for i in range(4):
        forward(200)
        left(9)
draw_square()

def change_cordinates(x,y):
    penup()
    goto(x,y)
    pendown()
change_cordinates(-300,0)

draw_square()

change_cordinates(-300,-300)

draw_square()
         
change_cordinates(0,-300)

draw_square()

change_cordinates(-400,-300)

draw_square()


exitonclick()
print("join goa")
print("join goa")