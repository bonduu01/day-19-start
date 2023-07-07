import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple"]
players = ["Peter", "Tim", "Azuka", "Tope", "Jindu", "Olivia", "Tolu", "Segun"]
is_race_on = False
all_turtles = []
turtle_names = []

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet fool!",
    prompt=f"Which turtle color would win the race? Enter a color: {colors}"
)


def move():
    forward = random.randint(3, 5)
    return forward


num_of_players = 8
x_cor = -240
y_cor = -160
for counter in range(num_of_players):
    color = colors[counter]

    players[counter] = Turtle(shape="turtle")
    players[counter].penup()
    players[counter].color(color)
    players[counter].goto(x=x_cor, y=y_cor)
    y_cor += 45
    all_turtles.append(players[counter])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"Yay! you have won, turtle with color {winning_color} is the winner!")
            else:
                print(f"Oops! Sorry you lost, "
                      f"color {winning_color} is the winner, you placed your bet on {user_bet} turtle")
        random_distance = move()
        turtle.forward(random_distance)

screen.exitonclick()
