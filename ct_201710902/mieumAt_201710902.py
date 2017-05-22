
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def giyukAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.fd(size)
    t1.rt(90) 
    t1.fd(size)

giyukAt(-100,100,100)



t1.home()

t1.clear()


def nieunAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)



nieunAt(-100,100,100)



t1.home()

t1.clear()

def mieumAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    giyukAt(x,y,size)
    t1.penup()
    t1.goto(x,y)
    t1.lt(90)
    t1.pendown()
    nieunAt(x,y,size)


mieumAt(100,-100,100)






