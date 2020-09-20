import pygame
pygame.init()

while 1:
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print('ciao')