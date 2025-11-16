import pgzrun
import random

WIDTH = 600
HEIGHT = 300

altura_sonic = HEIGHT - 40
mode = 'menu'



sonic_normal = Actor("sonic_de_ido", (50, altura_sonic))
sonic_super = Actor("super_de_ido", (120, 200))
go = Actor("go")
play = Actor("play", (300, 50))
shop = Actor("tienda", (300, 135))
collection = Actor("coleccion", (300, 210))
cross = Actor("cross", (580, 20))
list_sonic = []
count = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
bullet_count = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
bala_tienda = Actor("bala_tienda", (400, 200))


gameover = 0

enemies = []

sonic_de_correr = ["sonic_de_correr1", "sonic_de_correr2"]
sonic_iz_correr = ["sonic_iz_correr1", "sonic_iz_correr2"]
enemy_list = ["enemigo1", "enemigo2", "enemigo3", "la_grande_cbn"]
bullets = []
indice_correr = 0
personaje_seleccionado = sonic_super
personajes_comprados = [sonic_super]

bk = Actor("background1")

def draw_enemies():
    for enemie in enemies:
        enemie.draw()


def create_enemies():
    if len(enemies) < 3:
        random_image_enemy = random.randint(0,2)
        random_brainrot = random.randint(0,40)
        if random_brainrot == 1 and mode == "game":
            random_image_enemy = 3
            sounds.la_grande_cbn.play()
        random_pos_x = random.randint(WIDTH + 10, WIDTH + 1000)
        new_enemy = Actor(enemy_list[random_image_enemy], (random_pos_x, HEIGHT - 30))
        enemies.append(new_enemy)
        

def move_enemies():
    global count
    for enemy in enemies:
        if enemy.x > -20:
            enemy.x -= 10.5
        else:
            enemies.remove(enemy)
            count += 3

def game_over_verify():
    global gameover
    if personaje_seleccionado == sonic_normal:
        for enemy in enemies:
            if sonic_normal.colliderect(enemy):
                gameover = 1
    elif personaje_seleccionado == sonic_super:
        for enemy in enemies:
            if sonic_super.colliderect(enemy):
                gameover = 1


def draw_bullets():
    for bullet in bullets:
        bullet.draw()

def create_bullets():
    global bullet_count
    if bullet_count > 0:
        bullet_count -= 1
        if personaje_seleccionado == sonic_normal:
            new_bullet = Actor("ataque", sonic_normal.pos)
            bullets.append(new_bullet)
        elif personaje_seleccionado == sonic_super:
            new_bullet = Actor("ataque", sonic_super.pos)
            bullets.append(new_bullet)

def move_bullets():
    for bullet in bullets:
        if bullet.x < WIDTH:
            bullet.x += 7.3
        else:
            bullets.remove(bullet)
def colisiones():
    global count
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                count += 1
            




def draw(): 
    if gameover == 0 and mode == "game":
        bk.draw()
        screen.draw.text(str(count), center = (30, 50), fontsize = 30)
        screen.draw.text(str(bullet_count), center = (WIDTH - 30, 50), fontsize = 30)
        if personaje_seleccionado == sonic_normal:
            sonic_normal.draw()
        elif personaje_seleccionado == sonic_super:
            sonic_super.draw()
        draw_enemies()
        draw_bullets()
        cross.draw()
    if gameover == 1:
        go.draw()
    elif mode == 'menu':
        bk.draw()
        screen.draw.text(str(count), center = (30, 50), fontsize = 30)
        screen.draw.text(str(bullet_count), center = (WIDTH - 30, 50), fontsize = 30)
        play.draw()
        shop.draw()
        collection.draw()
    elif mode == 'shop':
        bk.draw()
        screen.draw.text(str(count), center = (30, 50), fontsize = 30)
        screen.draw.text(str(bullet_count), center = (WIDTH - 30, 50), fontsize = 30)
        cross.draw()
        sonic_super.pos = (120, 200)
        sonic_super.draw()
        bala_tienda.draw()
        screen.draw.text("$300", center = (120, 245), fontsize = 30)
        screen.draw.text("$15", center = (400, 245), fontsize = 30)
    elif mode == "collection":
        bk.draw()
        screen.draw.text(str(count), center = (30, 50), fontsize = 30)
        screen.draw.text(str(bullet_count), center = (WIDTH - 30, 50), fontsize = 30)
        cross.draw()
        sonic_normal.pos = (120, altura_sonic)
        sonic_super.pos = (400, altura_sonic)
        if sonic_normal in personajes_comprados:
            sonic_normal.draw()
        if sonic_super in personajes_comprados:
            sonic_super.draw()
    
def on_key_down(key):
    global gameover
    if personaje_seleccionado == sonic_normal:
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
    elif personaje_seleccionado == sonic_super:
        if keyboard.up or keyboard.w:
            sonic_super.y = 50
            animate(sonic_super, duration=0.8, y=altura_sonic)
            sonic_super.image = "super_de_salto"
        elif keyboard.K_RETURN and gameover == 1:
            gameover = 0
            sonic_super.pos = (50, altura_sonic)
            enemies.clear()
        elif keyboard.space:
            create_bullets()
def on_mouse_down(pos, button):
    global mode, personaje_seleccionado, count, bullet_count
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
    if mode == "collection" and sonic_normal.collidepoint(pos):
        personaje_seleccionado = sonic_normal
    elif mode == "collection" and sonic_super.collidepoint(pos):
        personaje_seleccionado = sonic_super
    if mode == "shop" and sonic_super.collidepoint(pos) and count >= 300 and sonic_super not in personajes_comprados:
        personaje_seleccionado = sonic_super
        personajes_comprados.append(sonic_super)
        count -= 300
    elif mode == "shop" and bala_tienda.collidepoint(pos) and count >= 15:
        bullet_count += 20
        count -= 15

def update(dt):
    global gameover, indice_correr
    if personaje_seleccionado == sonic_normal:
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
    elif personaje_seleccionado == sonic_super:
        if keyboard.a and sonic_super.x > 20:
            sonic_super.x -= 10
            indice_correr += 1
            if indice_correr > 1:
                indice_correr = 0
            sonic_super.image = "super_iz_correr"
        elif keyboard.d and sonic_super.x < WIDTH-20:
            sonic_super.x += 10  
            indice_correr += 1
            if indice_correr > 1:
                indice_correr = 0
            sonic_super.image = "super_de_correr"   
        elif sonic_super.y == altura_sonic:
            sonic_super.image = "super_de_ido"
        if mode != "game":
            enemies.clear()

    create_enemies()
    move_enemies()
    move_bullets()
    colisiones()
    game_over_verify()
        
pgzrun.go()