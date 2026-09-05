import random
import turtle as t

mini = t.Turtle()
t.colormode(255)
colors = [ (233, 225, 99), (208, 160, 114), (120, 172, 205), (217, 134, 174), (194, 9, 67), (223, 61, 128), (184, 79, 29), (49, 101, 160), (122, 188, 158), (191, 167, 18), (12, 21, 58), (235, 164, 191), (39, 185, 116), (20, 27, 161), (195, 40, 116), (232, 225, 4), (18, 181, 211), (9, 42, 21), (48, 128, 78), (147, 219, 197), (129, 218, 233), (51, 18, 14), (104, 99, 201), (223, 77, 50), (187, 12, 8), (238, 167, 156)]
size = len(colors)
tub = random.choice(colors)
mini.shape("circle")
mini.color(tub)
build = True
for _ in range(5):
    while build:
        for _ in range (20):
            tub = random.choice(colors)
            mini.color(tub)
            mini.pensize(10)
            mini.shape("circle")
            mini.pendown()
            mini.forward(20)
            mini.penup()
            mini.forward(20)
        mini.right(90)
        mini.backward(20)
        mini.left(90)
        for _ in range (20):
            tub = random.choice(colors)
            mini.color(tub)
            mini.pensize(10)
            mini.shape("circle")
            mini.pendown()
            mini.backward(20)
            mini.penup()
            mini.backward(20)
        mini.left(90)
        mini.forward(20)
        mini.right(90)
    build = False


    
    






















screen = t.Screen()
screen.exitonclick()