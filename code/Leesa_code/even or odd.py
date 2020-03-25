import turtle
t = turtle.Pen()
t.speed (0)
sides = int(turtle.numinput("number of sides","how many sides do you want in your spiral"))
turtle.bgcolor("light blue")

for x in range(5,75):
    t.left(360/sides+2)

    t.width(x/25 + 1)
    t.penup()
    t.forward(3*x)
    t.pendown()
    if (x % 2 == 0):
        for n in range(sides):
            t.circle(n/3)
            t.left(360/sides)
    else:
        for n in range(sides):
            t.forward(x)
            t.left(360/sides+4)