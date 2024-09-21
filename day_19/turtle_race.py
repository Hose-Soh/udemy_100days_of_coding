from random import randrange
from turtle import Turtle, Screen

new_screen = Screen()
new_screen.setup(width=500, height=400)
race_on = False

user_select = new_screen.textinput(title="Turtle Bet", prompt="Select a turtle: ")

all_turtle = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_list = []
y_ax = -150

for i in range(len(all_turtle)):
    turtle = Turtle(shape="turtle")

    turtle.color(all_turtle[i])
    turtle.penup()
    turtle.goto(x=-220, y=y_ax)
    y_ax+=50
    turtle_list.append(turtle)

if user_select:
    race_on = True

while race_on:

    for t in turtle_list:
        if t.xcor() > 230:
            race_on = False
            t_won = t.pencolor()
            if t_won==user_select:
                print(f"Your bet was accurate. {t_won.title()} turtle won!")
            else:
                print(f"Your bet was inaccurate. {t_won.title()} turtle won!")


        steps = randrange(1, 10)
        t.speed("slowest")
        t.forward(steps)


new_screen.exitonclick()