# Simple window whic will show current time like digital watch and a quote by my favourite Rumi

import time
import datetime as dt
import turtle

# create a turtle to distplay time
t = turtle.Turtle()

# create screen
s = turtle.Screen()

# Screen interface
s.bgcolor("grey")
s.title("Can I have time by Mohammad Nehal Sayib")
s.setup(width=800, height=450)

# obtain current hour, minute and second from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour

# Quotes
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -200)
pen.write("The day is conscious of itself. - Rumi",
          align="center", font=("Courier", 24, "normal"))

while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2) + ":"+str(min).zfill(2)+":" +
            str(sec).zfill(2), align="center", font=("Arial Narrow", 35, "bold"))
    time.sleep(1)
    sec += 1

    if sec == 60:
        sec = 0
        min += 1

    if min == 60:
        min = 0
        hr += 1

    if hr == 13:
        hr = 1
