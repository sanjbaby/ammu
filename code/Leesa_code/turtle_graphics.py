import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed (0)
colors = ("red","yellow","blue","green","grey","white","pink","purple")
sides = int(turtle.numinput("number of sides","how many sides (1-8)"))
your_name = turtle.textinput("enter your name","what is your name")
for x in range(200):
    t.pencolor(colors[x%sides])
    t.penup()
    t.forward(2*x)
    t.pendown()
    t.write(your_name)
    t.left(92)
