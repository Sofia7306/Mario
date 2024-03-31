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
    
    def fire(self):
        bullet = Bullet('fire.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets.add(bullet)  

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - 100:
            self.rect.x += self.speed

bullets = sprite.Group()
class Bullet(GameSprite):
    def update(self): #функція пострілу праворуч
        self.rect.x += 10
        if self.rect.x > 1000:
            self.kill()
#ігрова сцена:
window =display.set_mode((800,600))
picture =transform.scale(image.load("image.jpg"),(800,600))
picture2 =transform.scale(image.load("image2.jpg"),(800,600))
win_width = 600
win_height = 500


player1 = Player('Mario.png',50,430,10,70,70)
player2 = Player("mushroom.png",250,430,10,50,50)
player3 = Player("mushroom.png",450,430,10,50,50)
player4 = Player("mushroom.png",650,430,10,50,50)
player5 = Player("star.png",370,300,10,50,50)
player6 = Player("star.png",570,300,10,50,50)
player7 = Player("bear.png",250,430,10,50,50)
player8 = Player("fox.png",450,430,10,50,50)


# змінні для стрибка
is_jump = False
jump_count = 10

#прапорці, що відповідають за стан гри
game = True
clock = time.Clock()

lvl1 = True
lvl2 = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    player1.fire()    


    
    keys = key.get_pressed()
    if not is_jump:
        if keys[K_UP]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player1.rect.y -= (jump_count ** 2) * 0.4 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    if lvl1:
        window.blit(picture,(0,0))
        player1.reset()
        player2.reset()
        player3.reset()
        player4.reset()
        player5.reset()
        player6.reset()
        bullets.draw(window)
        bullets.update()

        if sprite.collide_rect(player1,player2) :
            game = False
        if sprite.collide_rect(player1,player3) :
            game = False
        if sprite.collide_rect(player1,player4) :
            game = False
        player1.move()

        if player1.rect.x >= 800:
            lvl1 = False
            lvl2 = True
            player1.rect.x = 50
            player1.rect.y = 430



        
    if lvl2:
        window.blit(picture2,(0,0))
    
        player1.reset()
        player1.move()
        player8.reset()
        player7.reset()


   
    display.update()
    clock.tick(60)


