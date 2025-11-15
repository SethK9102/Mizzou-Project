import pygame
from turtle_object import Turtle_object
from plastic_object import Plastic

pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pygame.sprite.Group()
trtl = Turtle_object(SCREEN_WIDTH//4 * 3, SCREEN_HEIGHT//2)
all_sprites.add(trtl)

clock = pygame.time.Clock()

plastic_straws = pygame.sprite.Group()
plastic_straw = Plastic()
plastic_straws.add(plastic_straw)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # trtl.update()

    all_sprites.draw(screen)
    all_sprites.update()
    
    
    screen.fill((14, 135, 204))
    plastic_straws.update()
    plastic_straws.draw(screen)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
