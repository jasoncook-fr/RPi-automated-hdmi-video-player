import os
from time import sleep
import pygame,os,sys
from pygame.locals import *

os.system("clear")
pygame.font.init()
pygame.mixer.init()

display_width = 1680
display_height = 1050
screen = pygame.display.set_mode((display_width, display_height))
screen.fill((255, 80, 80))

font_path = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
screenImg = pygame.image.load('dome-screensaver.jpeg')

font_size = 70
myfont = pygame.font.Font(font_path, font_size)

label = myfont.render("please introduce a usb storage device", 1, (0,0,0))
text_rect = label.get_rect(center=(display_width/2, display_height/2))
screen.blit(screenImg, (0, 0))
screen.blit(label, text_rect)
pygame.display.flip()

loop = True
while loop:
    # This loop runs until the user either presses the <ESC> key, or closes the Pygame window.
    # This allows the user to see the Pygame window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            loop = False

# Exit pygame cleanly
pygame.quit()
