import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500
score = 0
gameover = False

bee=Actor("bee")
bee.pos=(100,100)

flower=Actor("flower")
flower.pos=(200,200)

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score),color="blue",topleft=(10,10))

    if gameover:
        screen.fill("red")
        screen.draw.text("Time's Up! Your Final Score: "+str(score),midtop=(WIDTH/2,10),fontsize=40,color="black")

def place_flower():
    flower.x=randint(70,(WIDTH-70))
    flower.y=randint(70,(HEIGHT-70))

def timeup():
    global gameover
    gameover = True




pgzrun.go()