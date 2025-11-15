import pygame
pygame.init()

info = pygame.display.Info()
info = pygame.display.Info()



SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85


class Plastic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Plastic_Bag.png")