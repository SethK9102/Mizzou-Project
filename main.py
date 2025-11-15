from turtle_object import Turtle_object
import pygame

trtl = Turtle_object()


pygame.init()
from plastic_object import Plastic

#used Chat GPT to ask a question on how to get your screen width based on your screen
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

plastic_straws = pygame.sprite.Group()
plastic_straw = Plastic()
plastic_straws.add(plastic_straw)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill((14, 135, 204))
    plastic_straws.update()
    plastic_straws.draw(screen)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
