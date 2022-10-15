import turtle
screen = turtle.Screen()
screen.setup(500,600, startx=0, starty=100)
colors= ['red','black', 'yellow', 'blue', 'green','violet','pink']
t = turtle.pen()
turtle.bgcolor('black')
for i in range (280):
    turtle.pencolor(colors [i%6])
    turtle.speed(10)
    turtle.forward(i)
    turtle.width(i//100+1)
    turtle.left(59)
