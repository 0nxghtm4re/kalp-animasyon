import turtle
import math
import time

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Kalp Animasyonu")

def kalp(n):
    x = 16 * math.sin(n)**3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

t.color("red")
t.pensize(2)

for i in range(15):
    t.clear()
    t.penup()
    scale = 15 + i*0.8  # büyüyüp küçülme efekti
    t.goto(0, -50)
    t.pendown()
    t.begin_fill()
    for j in range(100):
        x, y = kalp(j * math.pi / 50)
        t.goto(x * scale, y * scale - 50)
    t.end_fill()
    time.sleep(0.1)

t.hideturtle()
turtle.done()
