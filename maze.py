#створи гру "Лабіринт"!
from pygame import *
from typing import Any
from random import choice

init()
font.init()
font1 = font.SysFont("Impact", 85)
finish_text = font1.render("GAME OVER", True, (235, 64, 52))
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
mixer.music.set_volume(0.25)

kick = mixer.Sound

MAP_WIDTH, MAP_HEIGHT = 25, 20#
TILESIZE = 40 #розмір квадратика карти



WIDTH, HEIGHT = MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE
window = display.set_mode((WIDTH,HEIGHT))
FPS = 60
clock = time.Clock()

bg = image.load("background.jpg")
bg = transform.scale(bg, (WIDTH,HEIGHT))
player_img = image.load("hero.png")
player2_img = image.load("cyborg.png")
wall_img = image.load("wall.png")
gold_img = image.load("treasure.png")


all_sprite = sprite.Group()
class Sprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = mask.from_surface(self.image)
        all_sprite.add(self)



class Player(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.hp = 100
        self.speed = 2.6

    def update(self):
        key_pressed = key.get_pressed()
        old_pos = self.rect.x, self.rect.y
        if (key_pressed[K_w] or key_pressed[K_UP])  and self.rect.y > 0:
            self.rect.y -= self.speed
        if (key_pressed[K_s] or key_pressed[K_DOWN]) and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if (key_pressed[K_a] or key_pressed[K_LEFT])  and self.rect.x > 0:
            self.rect.x -= self.speed
        if (key_pressed[K_d] or key_pressed[K_RIGHT]) and self.rect.right < WIDTH:
            self.rect.x += self.speed
        
        collide_list = sprite.spritecollide(self, walls, False, sprite.collide_mask)
        if len(collide_list) > 0:
            self.rect.x , self.rect.y = old_pos

        enemy_collide = sprite.spritecollide(self, enemys, False, sprite.collide_mask)
        if len(enemy_collide) > 0:
            self.hp -= 100
            
class Enemy(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.damage = 20
        self.speed = 2
        self.dir_list = ["right", "left", "up", "down"]
        self.dir = choice(self.dir_list)


    def update(self):
        key_pressed = key.get_pressed()
        old_pos = self.rect.x, self.rect.y
        if self.dir == "up"  and self.rect.y > 0:
            self.rect.y -= self.speed
        if self.dir == "down" and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if self.dir == "left"  and self.rect.x > 0:
            self.rect.x -= self.speed
        if self.dir == "right" and self.rect.right < WIDTH:
            self.rect.x += self.speed
        
        collide_list = sprite.spritecollide(self, walls, False, sprite.collide_mask)
        if len(collide_list) > 0:
            self.rect.x , self.rect.y = old_pos
            self.dir = choice(self.dir_list)     


player1 = Player(player_img, TILESIZE-5,TILESIZE-5, 5, 40)
walls = sprite.Group()
enemys = sprite.Group()
gold = sprite.Group()

with open("map.txt", 'r') as f:
    map = f.readlines()
    x = 0
    y = 0
    for line in map:
        for symbol in line:
            if symbol == "W":
                walls.add(Sprite(wall_img, TILESIZE, TILESIZE, x,y))
            if symbol == "E":
                enemys.add(Enemy(player2_img, TILESIZE, TILESIZE, x,y))
            if symbol == "P":
                player1.rect.x = x
                player1.rect.x = x
            if symbol == "g":
                gold = Sprite(gold_img, TILESIZE, TILESIZE,x,y)
            x += TILESIZE
        y += TILESIZE
        x = 0
       


run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg, (0,0))
    if player1.hp <= 0:
        finish = True
    if sprite.collide_mask(player1, gold):
        finish = True
        finish_text = font1.render("YOU WIN", True, (235, 64, 52))

    all_sprite.draw(window)
    if not finish:
        all_sprite.update()
    if finish:
        window.blit(finish_text, (280, 300) )
    display.update()
    clock.tick(FPS)
    
# W - Стіна
# P - Гравець