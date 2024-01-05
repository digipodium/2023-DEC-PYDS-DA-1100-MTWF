from turtle import *
speed(0)
def pentagon(size, color):
    fillcolor(color)
    begin_fill()
    for i in range(5):
        fd(size)
        lt(360/5)
    end_fill()
# use
for i in range(6):
    pentagon(100, 'red')
    pentagon(90, 'green')
    pentagon(80, 'blue')
    bk(150)
    rt(360/6)
hideturtle()
mainloop()
