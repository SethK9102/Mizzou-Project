<<<<<<< Updated upstream
<<<<<<< Updated upstream:turtle.py
class Turtle_object:
=======
import pygame
>>>>>>> Stashed changes:turtle_object.py
=======
import pygame
>>>>>>> Stashed changes

class Turtle_object(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.lives = 3
        self.score = 0
    
    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1
        elif self.lives == 0:
            return True
        return False
    
    def gain_score(self, points):
        self.score += points