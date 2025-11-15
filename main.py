import pygame
pygame.init()

#used Chat GPT to ask a question on how to get your screen width based on your screen
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           
    screen.fill((14, 135, 204))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()