#створи гру "Лабіринт"!
from pygame import *

init()
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
mixer.music.set_volume(0.25)

kick = mixer.Sound

WIDTH, HEIGHT = 700,500
window = display.set_mode((WIDTH,HEIGHT))
FPS = 60
clock = time.Clock()

bg = image.load("background.jpg")
bg = transform.scale(bg, (WIDTH,HEIGHT))
player_img = image.load("hero.png")
player2_img = image.load("cyborg.png")



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
        if key_pressed[K_w] or key_pressed[K_UP]  and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]  and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed




player1 = Player(player_img, 70,70,160,300)
player2 = Player(player2_img, 70,70,470,300)



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
    