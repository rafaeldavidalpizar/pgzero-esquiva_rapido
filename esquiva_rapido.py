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
enemy_list = ["enemigo1", "enemigo2", "enemigo3"]
bullets = []
indice_correr = 0


bk = Actor("background1")

def draw_enemies():
    for enemie in enemies:
        enemie.draw()


def create_enemies():
    if len(enemies) < 3:
        random_image_enemy = random.randint(0,2)
        random_pos_x = random.randint(WIDTH + 10, WIDTH + 1000)
        new_enemy = Actor(enemy_list[random_image_enemy], (random_pos_x, HEIGHT - 30))
        enemies.append(new_enemy)

def move_enemies():
    for enemy in enemies:
        if enemy.x > -20:
            enemy.x -= 9
        else:
            enemies.remove(enemy)

def game_over_verify():
    global gameover
    for enemy in enemies:
        if personaje.colliderect(enemy):
            gameover = 1


def draw_bullets():
    for bullet in bullets:
        bullet.draw()

def create_bullets():
    new_bullet = Actor("ataque", personaje.pos)
    bullets.append(new_bullet)

def move_bullets():
    for bullet in bullets:
        if bullet.x < WIDTH:
            bullet.x += 8
        else:
            bullets.remove(bullet)
def colisiones():
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
            




def draw():
    if gameover == 0:
        bk.draw()
        personaje.draw()
        draw_enemies()
        draw_bullets()
    else:
        go.draw()
    
def on_key_down(key):
    global gameover
    if keyboard.up or keyboard.w:
        personaje.y = 50
        animate(personaje, duration=0.8, y=altura_sonic)
        personaje.image = "sonic_de_salto"
    elif keyboard.K_RETURN and gameover == 1:
        gameover = 0
        personaje.pos = (50, altura_sonic)
        enemies.clear()


    elif keyboard.space:
        create_bullets()

    
    
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
    move_bullets()
    colisiones()
    game_over_verify()
        
pgzrun.go()