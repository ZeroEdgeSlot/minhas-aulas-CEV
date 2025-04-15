import pygame

# usando para iniciar o player
pygame.mixer.init()

# carrega um arquivo de musica 
pygame.mixer.music.load("Waitremix.mp3")

# inicia a musica com reprodutor
pygame.mixer.music.play()

input()
pygame.event.wait()