# Name: G Adityan
# ID: 2016B1A70929P

import turtle
import pickle

def graphics_function():
    SIZE = 600
    size=4
    TURTLE_SIZE = 20

    colors = ["blue", "green"]

    fp = open("moves_list.pkl", "rb")
    moves = pickle.load(fp)
    #print(type(movesp), movesp)
    screen = turtle.Screen()

    tom = turtle.Turtle(visible=False)
    tom.penup()
    tom.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
    tom.pendown()
    tom.forward(SIZE)
    tom.penup()
    tom.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2-10)
    tom.pendown()
    tom.showturtle()

    #screen.mainloop()
    tom.speed(7)

    tom.forward(SIZE)
    tom.right(90)
    tom.forward(SIZE)
    tom.right(90)
    tom.forward(SIZE)
    tom.right(90)
    tom.forward(SIZE)

    if size%2!=0:
        for i in range(size):
          if i%2==0:
            tom.right(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.right(90)
            tom.pendown()
            tom.forward(SIZE)
          else:
            tom.left(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.left(90)
            tom.pendown()
            tom.forward(SIZE)

        tom.left(90)

        for i in range(size):
          if i%2==0:
            tom.left(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.left(90)
            tom.pendown()
            tom.forward(SIZE)
          else:
            tom.right(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.right(90)
            tom.pendown()
            tom.forward(SIZE)
    else:
        for i in range(size):
          if i%2==0:
            tom.right(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.right(90)
            tom.pendown()
            tom.forward(SIZE)
          else:
            tom.left(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.left(90)
            tom.pendown()
            tom.forward(SIZE)

        tom.right(90)

        for i in range(size):
          if i%2==0:
            tom.right(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.right(90)
            tom.pendown()
            tom.forward(SIZE)
          else:
            tom.left(90)
            tom.penup()
            tom.forward(SIZE/size)
            tom.left(90)
            tom.pendown()
            tom.forward(SIZE)

    TURTLE_SIZE = 20

    screen = turtle.Screen()

    tom = turtle.Turtle(visible=False)
    tom.penup()
    tom.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
    tom.pendown()
    tom.showturtle()

    k=0
    for p in moves:
        print("k is ", k)
        tom.pencolor(colors[k])
        x = int(p[0])
        y = int(p[1])
        tom.penup()
        tom.right(90)
        tom.forward(SIZE/size * (x+0.5))
        tom.penup()
        tom.left(90)
        tom.forward(SIZE/size * (y+0.5))
        tom.pendown()
        
        if k==0:
            tom.begin_fill()
            tom.color("blue")
            tom.circle(20)
            tom.end_fill()
            k=1
        else:
            tom.begin_fill()
            tom.color("green")
            tom.circle(20)
            tom.end_fill()
            k=0
        tom.penup()
        tom.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
