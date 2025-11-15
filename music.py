import pygame
pygame.mixer.init()

class Music():
    def __init__(self, music_file:str="Sounds/Waves_Music.mp3", volume:float=0.25):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(volume)
    def play(self, loops:int=-1):
        pygame.mixer.music.play(loops)
    def stop(self):
        pygame.mixer.music.stop()
    
pygame.quit()