
import pgzrun
import random

WIDTH = 400
HEIGHT = 400

def draw():
    circleR = 20
    screen.clear()
    for i in range(40):
        circlex = random.randint(10,390)
        circley = random.randint(10,390)
        Rcircle = random.randint(0,255)
        Gcircle = random.randint(0,255)
        Bcircle = random.randint(0,255)
        screen.draw.circle((circlex,circley),circleR,(Rcircle,Gcircle,Bcircle))


    

pgzrun.go()
