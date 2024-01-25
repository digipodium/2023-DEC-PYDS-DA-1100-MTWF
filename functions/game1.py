# pip install pgzero 
import pgzrun
import random
WIDTH = 600
HEIGHT = 600
box1 = Rect((10, 10), (50, 50))
box2 = Rect((300, 300), (100, 100))
def draw():
    screen.clear()
    screen.draw.filled_rect(box1, 'red')
    screen.draw.filled_rect(box2, 'blue')
    screen.draw.text("game", (250,10), color='white', fontsize=50)

def move(box, axis, speed=1):
    if axis == 'x':
        if box.x > WIDTH:
            box.x = 0
        box.x += speed # speed left to right
    if axis == 'y':
        if box.y > HEIGHT:
            box.y = 0
        box.y += speed

def update():
    move(box1, 'x', 6)
    move(box2, 'y', 2)
    print('running')
pgzrun.go()