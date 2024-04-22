#створи гру "Лабіринт"!
from pygame import *
from typing import Any

init()
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
        all_sprite.add(self)



class Player(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.hp = 100
        self.speed = 4

    def update(self):
        key_pressed = key.get_pressed()
        if (key_pressed[K_w] or key_pressed[K_UP])  and self.rect.y > 0:
            self.rect.y -= self.speed
        if (key_pressed[K_s] or key_pressed[K_DOWN]) and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if (key_pressed[K_a] or key_pressed[K_LEFT])  and self.rect.x > 0:
            self.rect.x -= self.speed
        if (key_pressed[K_d] or key_pressed[K_RIGHT]) and self.rect.right < WIDTH:
            self.rect.x += self.speed




player1 = Player(player_img, TILESIZE,TILESIZE,300,300)
player2 = Player(player2_img, TILESIZE,TILESIZE,470,300)
walls = sprite.Group()


with open("map.txt", 'r') as f:
    map = f.readlines()
    x = 0
    y = 0
    print(map)
    for line in map:
        for symbol in line:
            if symbol == "W":
                walls.add(Sprite(wall_img, TILESIZE, TILESIZE, x,y))
            if symbol == "P":
                player1.rect.x = x
                player1.rect.x = x
            x += TILESIZE
        y += TILESIZE
        x = 0
       


run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg, (0,0))
    
    all_sprite.draw(window)
    all_sprite.update()

    display.update()
    clock.tick(FPS)
    
# W - Стіна
# P - Гравець