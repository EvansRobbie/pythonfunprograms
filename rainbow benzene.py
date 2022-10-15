import turtle
screen =  turtle.Screen()
screen.setup(500,600, startx=0, starty=100)
colors= ['red','purple','green', 'violet', 'blue', 'orange', 'yellow']
t= turtle.pen()
turtle.bgcolor('black')
for x in range (280):
    turtle.pencolor(colors[x%6])
    turtle.width(x//100+1)
    turtle.forward(x)
    turtle.left(59)