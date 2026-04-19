from pygame import *

#создание окна игры
window = display.set_mode((900, 700))
display.set_caption('PingPongGame')

#создание сцены
win_width = 900
win_height = 500
background = display.set_mode((win_width, win_height))
background.fill((84, 143, 171)) # Заливка цветом (R, G, B)
display.flip()

#наименование картинок
img_ball = "Ball--Streamline-Plump.png"

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
     
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

#класс мяча
class Ball(GameSprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)


#класс платформы
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

#настройка элементов
ball = Ball(img_ball, 415, 215, 35, 35, 15)
left_platform = Wall(195, 116, 60, 80, 200, 20, 100)
right_platform = Wall(195, 116, 60, 820, 200, 20, 100)

#условия работы игры (игровой цикл)
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    ball.reset()
    left_platform.draw_wall()
    right_platform.draw_wall()
    display.update()