#!/usr/bin/env python
# Note the change in the shebang!

# 27th May 2016
# program name: display.py
# version 1.0
from datetime import datetime
from time import sleep # this lets us have a time delay (see line 12)

import pygame,os,sys
from pygame.locals import *
os.system("clear")
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error

pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 400))
screen.fill((255, 80, 80))

font_path = "/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf" # I don't have this!

font_size = 32
#fontObj = pygame.font.Font("font_path, font_size) LINE COMMENTED OUT!

myfont = pygame.font.SysFont("Rooto_Bold", 30) # Size increased from 15 to 30

# render text
label = myfont.render("Some text!", 1, (255,255,0))
screen.blit(label, (50, 50)) # Reduced the position from 500, 500, as this position is off the screen!

# I changed the shebang at the top, and added this:
pygame.display.flip() # Without this line, Pygame won't draw anything!

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
