import pgzrun
import random

WIDTH = 600
HEIGHT = 300

altura_sonic = HEIGHT - 40
mode = 'menu'

sonic_normal = Actor("sonic_de_ido", (50, altura_sonic))
sonic_super = Actor("super_de_ido", (120, 200))
go = Actor("go")
play = Actor("play", (300, 100))
shop = Actor("tienda", (300, 200))
collection = Actor("coleccion", (300, 300))
cross = Actor("cross", (580, 20))
list_sonic = []


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
        if sonic_normal.colliderect(enemy):
            gameover = 1


def draw_bullets():
    for bullet in bullets:
        bullet.draw()

def create_bullets():
    new_bullet = Actor("ataque", sonic_normal.pos)
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
    if gameover == 0 and mode == "game":
        bk.draw()
        sonic_normal.draw()
        draw_enemies()
        draw_bullets()
        cross.draw()
    elif mode == 'menu':
        bk.draw()
        play.draw()
        shop.draw()
        collection.draw()
    elif gameover == 1:
        go.draw()
    elif mode == 'shop':
        bk.draw()
        cross.draw()
        sonic_super.draw()
    elif mode == "collection":
        cross.draw()
    
def on_key_down(key):
    global gameover
    if keyboard.up or keyboard.w:
        sonic_normal.y = 50
        animate(sonic_normal, duration=0.8, y=altura_sonic)
        sonic_normal.image = "sonic_de_salto"
    elif keyboard.K_RETURN and gameover == 1:
        gameover = 0
        sonic_normal.pos = (50, altura_sonic)
        enemies.clear()
    elif keyboard.space:
        create_bullets()

def on_mouse_down(pos, button):
    global mode
    if mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'
        elif shop.collidepoint(pos):
            mode = 'shop'
        elif collection.collidepoint(pos):
            mode = "collection"
    elif cross.collidepoint(pos):
        mode = 'menu'
    elif cross.collidepoint(pos):
        mode = 'menu'
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'
        elif shop.collidepoint(pos):
            mode = 'shop'
        elif collection.collidepoint(pos):
            mode = "collection"

    
def update(dt):
    global gameover, indice_correr
    if keyboard.a and sonic_normal.x > 20:
        sonic_normal.x -= 10
        indice_correr += 1
        if indice_correr > 1:
            indice_correr = 0
        sonic_normal.image = sonic_iz_correr[indice_correr]
    elif keyboard.d and sonic_normal.x < WIDTH-20:
        sonic_normal.x += 10  
        indice_correr += 1
        if indice_correr > 1:
            indice_correr = 0
        sonic_normal.image = sonic_de_correr[indice_correr]        
    elif sonic_normal.y == altura_sonic:
        sonic_normal.image = "sonic_de_ido"
    if mode != "game":
        enemies.clear()

    create_enemies()
    move_enemies()
    move_bullets()
    colisiones()
    game_over_verify()
        
pgzrun.go()