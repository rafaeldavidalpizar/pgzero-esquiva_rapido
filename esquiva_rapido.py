import pgzrun
import time

WIDTH = 600
HEIGHT = 300

personaje = Actor("sonic", (50, 220))
box = Actor("box", (550, 265))
go = Actor("go")
gameover = 0

bk = Actor("background")

def draw():
    bk.draw()
    personaje.draw()
    box.draw()
    if gameover == 1:
        go.draw()
    
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        personaje.y = 100
        animate(personaje, tween='bounce_end', duration=2, y=240)
    
    
def update(dt):
    if keyboard.a and personaje.x > 20:
        personaje.x -= 15
    elif keyboard.d and personaje.x < WIDTH-20:
        personaje.x += 15
    elif keyboard.space:
        personaje.pos = (50, 220)    

    if box.x > -20:
        box.x = box.x - 5
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
    
    if personaje.colliderect(box):
         gameover = 1
         
        
pgzrun.go()