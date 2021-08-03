import turtle
t=turtle.Turtle()
turtle.bgcolor("white")
turtle.pensize(2)
turtle.speed(5)
while(True):

    for i in range(6):
        for colours in ["Yellow","Blue","Black","Green","Red","Pink"]:
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(30)
turtle.hideturtle()
turtle.mainloop()
