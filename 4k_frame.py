import turtle
a=turtle.Turtle()
screen=turtle.Screen()
screen.setup(500,500)
screen.bgcolor('black')
a.speed(11)
a.width(5)
col=('cyan','yellow','pink','orange','green','red')
def four ():
    for i in range (2):  
        a.penup()  
        a.goto(-200,-250)
        a.pendown()
        a.pencolor(col[i+1])
        a.goto(-200,250)
        a.pencolor(col[i+3])
        a.goto(-370,0)
        a.pencolor(col[i+2])
        a.goto(-75,0)
def K ():
    for b in range (2):
       
        a.penup()
        a.goto(100,-250)
        a.pendown()
        a.pencolor(col[b+1])
        a.goto(100,250)
        a.penup()
        a.goto(250,250)
        a.pendown()
        a.pencolor(col[b+2])
        a.goto(100,0)
        a.pencolor(col[b+3])
        a.goto(250,-250)
def star ():
    a.speed(27)
    a.width(1)
    a.penup ()
    a.goto(350,350)
    a.pendown()
 
    for s in range (80):
        a.forward(s*4)
        a.left(144)
        a.pencolor(col[s%6])
    a.penup ()
    a.goto(-350,-350)
    a.pendown()
    for d in range (100):
        a.forward(d*4)
        a.left(144)
        a.pencolor(col[d%6])
   
four()
K()
star()