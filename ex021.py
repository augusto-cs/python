import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('teste.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    time.sleep(1)
