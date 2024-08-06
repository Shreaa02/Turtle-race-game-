from turtle import Turtle, Screen
from random import randint


def start(j):
    t.penup()
    t.goto(x=-230, y=j)
    t.pendown()


colours = ["red", "orange", "yellow", "green", "blue", "purple"]

players = []

s = Screen()
s.setup(width=500, height=400)
k = Turtle()
k.hideturtle()
k.penup()
game_is_on = False
user_bet = s.textinput(title="Make your bet", prompt="Who will win the race?\n [red, orange, yellow, green, blue, purple]\n Enter a colour:")
print(user_bet)
k = -60
for i in range(len(colours)):
    t = Turtle(shape="turtle")
    t.color(colours[i])
    players.append(t)
    start(k)
    k += 30

if user_bet:
    game_is_on = True

msg = "lost"
col = ""
while game_is_on:
    for p in players:
        if p.xcor() > 230:
            game_is_on = False
            if col == user_bet:
                msg = "won"
            col += p.pencolor()
        p.penup()
        p.fd(randint(1, 10))
    p.pendown()

print(f"You {msg} !!, the {col} turtle is the winner.")
s.exitonclick()
