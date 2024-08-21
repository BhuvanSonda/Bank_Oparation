import turtle as t
T=t.Turtle()
t.shape("turtle")
t.pencolor("pale green")
t.pensize(5)
t.speed(1)
t.hideturtle()

def square(length):
    t.color("red")
    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    t.color("light green")
    t.end_fill()

def triangle(length):
    t.color("red")
    t.begin_fill()
    for i in range(3):
        t.fd(length)
        t.lt(120)
    t.color("pale green")
    t.end_fill()
t.penup()
t.goto(150,150)
t.pendown()
square(100)
t.penup()
t.goto(0,0)
t.penup()
t.goto(-150,150)
t.pendown()
triangle(100)


t.done()