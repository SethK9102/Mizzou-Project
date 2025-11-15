import pygame
import random
pygame.init()

info = pygame.display.Info()
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85

class Food(pygame.sprite.Sprite):
    def __init__(self, x_pos=500, y_pos=random.randint(0, SCREEN_HEIGHT)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Bottle.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        
    def update(self):
        self.rect.x += 5
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

pygame.quit()