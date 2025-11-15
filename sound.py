import pygame
pygame.mixer.init()

class Sound():
    # Initialize the Sound object with a sound file and volume
    def __init__(self, sound_file:str="Sounds/Plastic.mp3", volume:float=1.0):
        self.sound  = pygame.mixer.Sound(sound_file)
        self.sound.set_volume(volume)

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def loop_sound(self):
        self.sound.play(-1)