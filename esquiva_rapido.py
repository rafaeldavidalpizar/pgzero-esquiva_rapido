import pgzrun
import random

WIDTH = 600
HEIGHT = 300

altura_sonic = HEIGHT - 40

personaje = Actor("sonic_de_ido", (50, altura_sonic))
go = Actor("go")

gameover = 0

enemies = []

sonic_de_correr = ["sonic_de_correr1", "sonic_de_correr2"]
sonic_iz_correr = ["sonic_iz_correr1", "sonic_iz_correr2"]
indice_correr = 0


bk = Actor("background1")

def draw_enemies():
    for enemie in enemies:
        enemie.draw()


def create_enemies():
    if len(enemies) < 3:
        random_pos_x = random.randint(WIDTH + 10, WIDTH + 1000)
        new_enemy = Actor("enemigo1", (random_pos_x, HEIGHT - 30))
        enemies.append(new_enemy)

def move_enemies():
    for enemy in enemies:
        if enemy.x > -20:
            enemy.x = enemy.x - 7.5
        else:
            enemies.remove(enemy)


def draw():
    bk.draw()
    personaje.draw()
    draw_enemies()
    if gameover == 1:
        go.draw()
    
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        personaje.y = 50
        animate(personaje, duration=0.8, y=altura_sonic)
        personaje.image = "sonic_de_salto"
    
    
def update(dt):
    global gameover, indice_correr
    if keyboard.a and personaje.x > 20:
        personaje.x -= 10
        indice_correr += 1
        if indice_correr > 1:
            indice_correr = 0
        personaje.image = sonic_iz_correr[indice_correr]
    elif keyboard.d and personaje.x < WIDTH-20:
        personaje.x += 10  
        indice_correr += 1
        if indice_correr > 1:
            indice_correr = 0
        personaje.image = sonic_de_correr[indice_correr]        
    elif personaje.y == altura_sonic:
        personaje.image = "sonic_de_ido"

    create_enemies()
    move_enemies()
    
    # if personaje.colliderect(enemigo1):
    #      gameover = 1
         
        
pgzrun.go()