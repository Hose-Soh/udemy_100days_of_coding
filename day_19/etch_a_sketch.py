from turtle import Turtle, Screen

mini = Turtle()
new_screen = Screen()

def forward():
    mini.forward(10)

def backward():
    mini.backward(10)

def left():
    mini.left(10)

def right():
    mini.right(10)

def clear():
    mini.clear()
    mini.penup()
    mini.home()

new_screen.listen()

new_screen.onkey(key="w", fun=forward)
new_screen.onkey(key="s", fun=backward)
new_screen.onkey(key="d", fun=right)
new_screen.onkey(key="a", fun=left)
new_screen.onkey(key="c", fun=clear)

new_screen.exitonclick()