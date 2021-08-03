import turtle
turtle.pensize(2)
turtle.speed(12)
turtle.bgcolor("Black")

for i in range(10):
    for colours in ["Yellow","Blue","White","Green","Red","Pink"]:
        turtle.color(colours)
        turtle.circle(200)
        turtle.left(10)
turtle.hideturtle()
