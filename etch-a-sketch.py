from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.colormode(225)
turtle.setheading(0)


def forward():
    turtle.forward(20)


def backward():
    turtle.backward(20)


def clockwise():
    new_header = turtle.heading() + 10
    turtle.setheading(new_header)


def anti_clock():
    new_header = turtle.heading() - 10
    turtle.setheading(new_header)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(anti_clock, "a")
screen.onkey(clear, "c")

screen.exitonclick()
