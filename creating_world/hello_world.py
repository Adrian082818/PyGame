# import pygame module
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Initialize pygame 
pygame.init()

screen_width = 1000
screen_height = 1000 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

# load images 
sun_img = pygame.image.load('img/sun.png')
background_img = pygame.image.load('img/sky.png')

run = True 
while run:

    screen.blit(background_img, (0, 0))
    screen.blit(sun_img, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.display.update()

pygame.quit() 