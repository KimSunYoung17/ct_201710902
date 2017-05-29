import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


width=wn.window_width()


x1=0.0-(width-40)/3
x2=0.0
x3=0.0+(width-40)/3

w3=(width-40)/3
x1=0.0-w3
x2=0.0
x3=0.0+w3




def drawSquare(size):
    for i in range(0, 4):
        t1.forward(size)
        t1.right(90)

def drawSquareAt(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    drawSquare(size)





    
def drawTriangle(size):
    for i in range(0, 3):
        t1.forward(size)
        t1.right(120)

def drawTriangleAt(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    drawTriangle(size)






def drawStar(size):
    for i in range(0, 5):
        t1.forward(size)
        t1.right(144)

def drawStarAt(x, y, size):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    drawStar(size)



        
drawSquareAt(x1,0,100)
drawTriangleAt(x2,0,100)
drawStarAt(x3,0,100)
