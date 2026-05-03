#создай игру "Лабиринт"!
from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Лабирик')

#задай фон сцены
background = transform.scale(
    image.load("background.jpg"), (700, 500)
    )
#Значение ФПС
clock = time.Clock()
FPS = 70

#мьюзика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

#спрайты
x_h = 70
y_h = 350

x_v = 550
y_v = 300


#класс спрайт
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = "left"
    def update(self):
        if self.rect.x <= 450:
            self.direction = "right"
        if self.rect.x > 700 - 50:
            self.direction = "left" 
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
violet = (93, 20, 145)
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
hero = Player('hero.png', x_h, y_h, 15)
cyborg = Enemy('cyborg.png', x_v, y_v, 15)
final = GameSprite('treasure.png', 600, 400, 0)
wall1 = Wall(93, 20, 145, 200, 200, 10, 250)
wall2 = Wall(93, 20, 145, 200, 30, 10, 50)
wall3 = Wall(93, 20, 145, 200, 30, 500, 10)
wall4 = Wall(93, 20, 145, 200, 450, 450, 10)
wall5 = Wall(93, 20, 145, 400, 40, 10, 100)
wall6 = Wall(93, 20, 145, 300, 350, 10, 100)
wall7 = Wall(93, 20, 145, 300, 350, 100, 10)
wall8 = Wall(93, 20, 145, 300, 130, 100, 10)
game = True
finish = False
while game:
    
    for e in event.get(): # ОБЯЗАТЕЛЬНО
        if e.type == QUIT:
            game = False
    if finish != True:
        clock.tick(FPS)
        window.blit(background, (0,0))
        hero.update()
        hero.reset()
        cyborg.update()
        cyborg.reset()
        final.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]
        display.update()
    if sprite.collide_rect(hero, final):
        finish = True
    if sprite.collide_rect(hero, cyborg):
        finish = True
    for wall in walls:
        if sprite.collide_rect(hero, wall):
            finish = True
