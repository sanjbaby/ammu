import turtle
t = turtle.Pen()
t.speed(0)
t.width(3)
t.penup()
turtle.bgcolor("black")
colors = ("red","orange","yellow","green","blue","violet","indigo","pink")
number = int(turtle.numinput("number of sides","how many sides(1-8)"))
for x in range(100):
    t.forward(x*5)
    position= t.position()
    heading= t.heading()
    for n in range (int(x/3)):
        t.pendown()
        t.pencolor(colors[n % number])
        t.forward(3*n)
        t.right(360/number-3)
        t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.left(360/number+2)


