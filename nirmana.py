import turtle
turtle.bgcolor("black")

t = turtle.Turtle()
t.pencolor("light blue")

a = 0
b = 0

t.speed(20)
t.penup()
t.goto(0, 200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()
    
turtle.done()