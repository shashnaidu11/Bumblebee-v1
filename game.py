import random
import pgzrun

TITLE="Bumble bee game"

HEIGHT=500
WIDTH=600
score=0

bee=Actor("bee")
bee.pos=(100,100)

flower=Actor("flower")
flower.pos=(200,250)

def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score: "+ str(score), color="red", topleft=(10,10) )






pgzrun.go()