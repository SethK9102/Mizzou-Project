import pygame
import os

class Turtle_object(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/turtle.png").convert_alpha()

        # set a rect so Group.draw() can blit this sprite
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.lives = 3
        self.score = 0
    
    def lose_life(self, running):
        if self.lives > 0:
            self.lives -= 1
        elif self.lives == 0:
            running = False

    def gain_score(self, points):
        self.score += points
        return self.score
    
    # def update(self):
    #     # get the current mouse position
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #     # center the turtle on the mouse position
    #     self.rect.centerx = mouse_x
    #     self.rect.centery = mouse_y