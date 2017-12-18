import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.pencolor("yellow")
        turtle.circle(rad,angle)
        turtle.pencolor("red")
        rad+=10
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    
    turtle.seth(-30)
    drawSnake(20,60,5,pythonsize/2)
main()    
