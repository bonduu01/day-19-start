import random
from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple"]
players = ["Peter", "Tim", "Azuka", "Tope", "Jindu", "Olivia", "Tolu", "Segun"]

num = print(colors.index("green"))

print(players[3])


def get_turtle_name(text_color):
    index = colors.index(text_color)
    player = players[index]
    return player

tur = get_turtle_name("red")
print(tur)
