import pygame
pygame.init()

info = pygame.display.Info()
info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85

class Heart(pygame.sprite.Sprite):
    def __init__(self, x_pos=500, y_pos=500):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Heart.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)
        
    """def update(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0"""
            
pygame.quit()