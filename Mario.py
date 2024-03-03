from pygame import *
'''Необхідні класи'''
 
# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - 100:
            self.rect.x += self.speed


#ігрова сцена:
window =display.set_mode((800,600))
picture =transform.scale(image.load("image.jpg"),(800,600))

win_width = 600
win_height = 500


player1 = Player('Mario.png',50,295,10,200,220)
player2 = Player("mushroom.png",100,295,10,150,100)


# змінні для стрибка
is_jump = False
jump_count = 10

#прапорці, що відповідають за стан гри
game = True
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    


    
    keys = key.get_pressed()
    if not is_jump:
        if keys[K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player1.rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    window.blit(picture,(0,0))
    player1.reset()
    player2.reset()

    player1.move()

   
   
    display.update()
    clock.tick(60)


