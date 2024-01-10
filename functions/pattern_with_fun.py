from turtle import *
def polygon(sides,length,color):
    fillcolor(color)
    begin_fill()
    for i in range(sides):
        fd(length)
        rt(360/sides)
    end_fill()
polygon(4,100,"red")
goto(150,150)
polygon(3,100,"blue")
goto(150,-150)
polygon(5,100,"green")
goto(-150,-150)
polygon(6,100,"yellow")
hideturtle()
mainloop()