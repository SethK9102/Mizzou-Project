import pygame
import os

class Turtle_object(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # asked Copilot how to load a png in pygame
        # load image reliably using a path relative to this file
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'turtle.png')
        try:
            img = pygame.image.load(image_path)
        except Exception as e:
            print(f"Failed to load image '{image_path}': {e}")
            # create a visible placeholder surface (transparent)
            img = pygame.Surface((64, 64), pygame.SRCALPHA)
            img.fill((0, 0, 0, 0))
            pygame.draw.circle(img, (255, 0, 0), (32, 32), 28)

        # Convert to display format if display is initialized
        try:
            if img.get_alpha() is not None:
                self.image = img.convert_alpha()
            else:
                self.image = img.convert()
        except Exception:
            # If conversion fails (e.g., no display yet), keep raw surface
            self.image = img

        # set a rect so Group.draw() can blit this sprite
        self.rect = self.image.get_rect()
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