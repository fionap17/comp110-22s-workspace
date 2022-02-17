
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# leo.left(90)
# leo.forward(50)
# done()

leo.speed(50)
leo.hideturtle()
leo.fillcolor(150, 50, 0)
leo.pencolor("green")
leo.begin_fill()
i: int = 0
while (i < 4):
    leo.forward(100)
    leo.left(90)
    i = i + 1
leo.end_fill()

leo.penup()
leo.goto(100, 100)
leo.pendown()

leo.color("blue", "pink")
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(100)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
side_length: float = 300.0

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.5

done()