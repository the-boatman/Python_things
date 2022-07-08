import turtle
import time
import math


def mvback():
    turtle.back(75)
    print(turtle.position())
def mvfwrd():
    turtle.forward(75)
    print(turtle.position())
def left():
    turtle.left(45)

def right():
    turtle.right(45)
def nodraw():
    turtle.penup()
def yesdraw():
    turtle.pendown

# turtle.onkeypress(mvback,'Down')
# turtle.onkeypress(mvfwrd,'Up')
# turtle.onkeypress(left,'Left')
# turtle.onkeypress(right,'Right')
# turtle.onkeypress(nodraw,'KP_0')
# turtle.onkeypress(yesdraw,'KP_1')
# turtle.listen()

# (-1600.00,600.00) coordinates for top left


# #box size for letters
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
# turtle.right(90)
# turtle.forward(200)
tall = (175/3)/3
def drawA():
    # turtle.color(color)
    turtle.penup()
    turtle.right(90)    
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75) #puts the turtle in the bottom right square
    turtle.left(180)
    turtle.forward(25)
    turtle.pendown()
    turtle.left(135)
    turtle.forward(25*math.sqrt(2))
    turtle.right(45)
    turtle.forward(175)
    turtle.right(135)            
    turtle.forward(25*math.sqrt(2))   
    turtle.right(45)    
    turtle.forward(175)    
    turtle.left(90)    
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(175*(2/3))
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(175*(2/3))
    turtle.right(135)
    turtle.forward(25*math.sqrt(2))
    turtle.back(25*math.sqrt(2))
    turtle.right(135)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(75)
    turtle.right(45)
    turtle.forward(25*math.sqrt(2))
    turtle.right(135)
    turtle.forward(75)
    turtle.right(45)
    turtle.forward(25*math.sqrt(2))
    turtle.penup()
    turtle.right(135)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(tall)
    turtle.pendown()
    turtle.forward(tall)
    turtle.right(135)
    turtle.forward(25*math.sqrt(2))
    turtle.back(25*math.sqrt(2))
    turtle.left(45)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)


turtle.hideturtle()
turtle.colormode(255) 



turtle.bgcolor('black')
r,g,b = 255,0,0
for i in range(255*2):
    turtle.color(r,g,b)
    if i<255//3:
        g += 5
    elif i < 255*2//3:
        r -= 5
    elif i <255:
        b += 5
    elif i < 255*4//3:
        g -= 5
    elif i < 255*5//3:
        r += 5
    else:
        b -= 5
    turtle.color(r,g,b)
    drawA()
    turtle.penup()
    turtle.forward(100)
    turtle.right(15)
    
    # turtle.forward()
    turtle.pendown()



   
ex = input("Push any button to continue")



