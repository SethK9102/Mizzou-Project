import pygame
pygame.mixer.init()

class Sound():
    def __init__(self, sound_file:str="", volume:float=0.5):
        self.sound  = pygame.mixer.Sound(sound_file)
        self.sound.set_volume(volume)
    def play(self):
        self.sound.play()
    def stop(self):
        self.sound.stop()