import pygame
import random
from turtle_object import Turtle_object
from plastic_object import Plastic
from food import Food

pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pygame.sprite.Group()
trtl = Turtle_object(SCREEN_WIDTH//4 * 3, SCREEN_HEIGHT//2)
all_sprites.add(trtl)

food_items = pygame.sprite.Group()

clock = pygame.time.Clock()

plastic_straws = pygame.sprite.Group()



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # trtl.update()
    screen.fill((14, 135, 204))
    all_sprites.draw(screen)
    all_sprites.update()
    
    if len(food_items) < 5 and random.random() < 0.01:
        food_item = Food(700, random.randint(0, SCREEN_HEIGHT))
        food_items.add(food_item)

    if len(plastic_straws) < 10 and random.random() < 0.015:
        plastic_straw = Plastic(700, random.randint(0, SCREEN_HEIGHT))
        plastic_straws.add(plastic_straw)
    
        all_sprites.draw(screen)
        all_sprites.update()
    
    food_items.update()
    food_items.draw(screen)
    
    plastic_straws.update()
    plastic_straws.draw(screen)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
