import pgzrun
import time

WIDTH = 600
HEIGHT = 300

altura_sonic = HEIGHT - 40

personaje = Actor("sonic_de_ido", (50, altura_sonic))
enemigo1 = Actor("enemigo1", (550, 265))
go = Actor("go")

gameover = 0


sonic_de_correr = ["sonic_de_correr1", "sonic_de_correr2"]
sonic_iz_correr = ["sonic_iz_correr1", "sonic_iz_correr2"]
indice_correr = 0


bk = Actor("background1")

def draw():
    bk.draw()
    personaje.draw()
    enemigo1.draw()
    if gameover == 1:
        go.draw()
    
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        personaje.y = 50
        animate(personaje, duration=0.6, y=altura_sonic)
        personaje.image = "sonic_de_salto"
    
    
def update(dt):
    global gameover, indice_correr
    if keyboard.a and personaje.x > 20:
        personaje.x -= 15
        indice_correr += 1
        if indice_correr > 1:
            indice_correr = 0
        personaje.image = sonic_iz_correr[indice_correr]
    elif keyboard.d and personaje.x < WIDTH-20:
        personaje.x += 15   
        indice_correr += 1
        if indice_correr > 1:
            indice_correr = 0
        personaje.image = sonic_de_correr[indice_correr]        
    elif personaje.y == altura_sonic:
        personaje.image = "sonic_de_ido"

    if enemigo1.x > -20:
        enemigo1.x = enemigo1.x - 10
    else:
        enemigo1.x = WIDTH + 20
    
    if personaje.colliderect(enemigo1):
         gameover = 1
         
        
pgzrun.go()