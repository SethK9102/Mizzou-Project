import pygame

class GamePhysics:
    
    def __init__(self, screen_width, screen_height, turtle_size=20):
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.turtle_size = turtle_size
        self.move_speed = 5
    
    def turtle_movement(self, turtle_x, turtle_y, keys):
        
        new_x = turtle_x
        new_y = turtle_y
        
        if keys[pygame.K_UP]:
            new_y = max(0, turtle_y - self.move_speed)
        if keys[pygame.K_DOWN]:
            new_y = min(self.screen_height - self.turtle_size, turtle_y + self.move_speed)
        if keys[pygame.K_LEFT]:
            new_x = max(0, turtle_x - self.move_speed)
        if keys[pygame.K_RIGHT]:
            new_x = min(self.screen_width - self.turtle_size, turtle_x + self.move_speed)
        
        if keys[pygame.K_w]:
            new_y = max(0, turtle_y - self.move_speed)
        if keys[pygame.K_s]:
            new_y = min(self.screen_height - self.turtle_size, turtle_y + self.move_speed)
        if keys[pygame.K_a]:
            new_x = max(0, turtle_x - self.move_speed)
        if keys[pygame.K_d]:
            new_x = min(self.screen_width - self.turtle_size, turtle_x + self.move_speed)
        
        return new_x, new_y
    
    def check_collision_rectangle(self, rect1, rect2):
        return rect1.colliderect(rect2)
    
    def check_food_collision(self, turtle_rect, food_items):

        collided_food_indices = []
        for index, food_rect in enumerate(food_items):
            if self.check_collision_rectangle(turtle_rect, food_rect):
                collided_food_indices.append(index)
        return collided_food_indices
    
    def check_obstacle_collision(self, turtle_rect, obstacle_items):
        for obstacle_rect in obstacle_items:
            if self.check_collision_rectangle(turtle_rect, obstacle_rect):
                return True
        return False
    
    def update_obstacle_position(self, obstacle_x, obstacle_y, move_direction_x, move_direction_y, move_speed):
        new_x = obstacle_x + (move_direction_x * move_speed)
        new_y = obstacle_y + (move_direction_y * move_speed)
        
        new_x = max(0, min(self.screen_width, new_x))
        new_y = max(0, min(self.screen_height, new_y))
        
        return new_x, new_y

    def is_position_on_screen(self, x, y):
        return (0 <= x <= self.screen_width and
                0 <= y <= self.screen_height)
