class Turtle_object:

    def __init__(self):
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