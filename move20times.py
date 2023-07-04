from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)


def move_ten_spaces():
    turtle.forward(20)


screen.listen()
screen.onkey(key="space", fun=move_ten_spaces)
screen.exitonclick()
