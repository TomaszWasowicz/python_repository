import turtle

def rectangle(step = 100):
    t = turtle.Pen()
    angle = 90
    i = 0
    j = 0
    while j < 3:
        while i < 4:
            t.forward(step)
            t.right(angle)
            i += 1
        step += 100
        j += 1
        i = 0
    turtle.Screen().exitonlick()

rectangle()

