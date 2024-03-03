import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Константи для вікна
screen_width = 800
screen_height = 600

# Створення вікна гри
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Super Mario')

# Кольори
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)

# Початкові координати Маріо
mario_x = 50
mario_y = 500
mario_width = 40
mario_height = 60
mario_speed = 1

# Гравець на землі або в повітрі
is_jump = False
jump_count = 10

# Функція для відображення Маріо
def draw_mario(x, y):
    pygame.draw.rect(screen, blue, (x, y, mario_width, mario_height))

# Основний цикл гри
while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mario_x > mario_speed:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT] and mario_x < screen_width - mario_width - mario_speed:
        mario_x += mario_speed
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            mario_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    draw_mario(mario_x, mario_y)
    pygame.display.update()