import random
import pygame


class Wave:
    # Represents a game wave with intensity that affects object movement speeds
    
    def __init__(self, screen_width, screen_height):
        # Initialize a wave with random intensity from 1 to 5
        self.intensity = random.randint(1, 5)
        self.speed_multiplier = 1 + self.intensity / 3.0  # Scale intensity to multiplier (1.33 to 2.67)
        self.screen_width = screen_width
        self.screen_height = screen_height
        # Make waves taller to cover more vertical space
        self.rect = pygame.Rect(0, 0, 50, screen_height)
        # Spawn wave on left side
        self.rect.x = random.randint(-100, 0)
        self.rect.y = 0
        self.wave_speed = 3
        self.active = True
    
    def update(self):
        # Move wave from left to right
        self.rect.x += self.wave_speed
        # Wave disappears when it reaches the right side
        if self.rect.left > self.screen_width:
            self.active = False
    
    def get_modified_speed(self, base_speed):
        # Calculate modified speed based on wave intensity
        return base_speed * self.speed_multiplier
    
    def check_collision_with_obstacles(self, obstacles):
        # Check which obstacles collide with wave
        colliding_obstacles = []
        for i, ob in enumerate(obstacles):
            if self.rect.colliderect(ob["rect"]):
                colliding_obstacles.append(i)
        return colliding_obstacles
    
    def check_collision_with_food(self, food_rects):
        # Check which food items collide with wave
        colliding_food = []
        for i, f in enumerate(food_rects):
            if self.rect.colliderect(f["rect"]):
                colliding_food.append(i)
        return colliding_food
    
    def check_collision_with_turtle(self, turtle_rect):
        # Check if wave collides with turtle
        return self.rect.colliderect(turtle_rect)
    
    def apply_to_obstacles(self, obstacles):
        # Apply wave intensity only to colliding obstacles
        colliding = self.check_collision_with_obstacles(obstacles)
        for i in colliding:
            if "base_speed" not in obstacles[i]:
                obstacles[i]["base_speed"] = obstacles[i]["speed"]
            obstacles[i]["speed"] = self.get_modified_speed(obstacles[i]["base_speed"])
    
    def apply_to_food(self, food_rects):
        # Apply wave intensity only to colliding food
        colliding = self.check_collision_with_food(food_rects)
        for i in colliding:
            if "base_speed" not in food_rects[i]:
                food_rects[i]["base_speed"] = food_rects[i]["speed"]
            food_rects[i]["speed"] = self.get_modified_speed(food_rects[i]["base_speed"])
    
    def __str__(self):
        # Return a string representation of the wave
        return f"Wave(intensity={self.intensity}, multiplier={self.speed_multiplier:.2f})"
