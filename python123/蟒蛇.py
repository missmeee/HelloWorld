import turtle
turtle.setup(850,350)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(10)
turtle.colormode(255)
turtle.pencolor(167,126,236)
turtle.seth(-40)
for i in range(5):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
