import pygame


pygame.init()


display_width = 1680
display_height = 1050

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('dome-screensaver.jpeg')

def car(x,y):
    gameDisplay.blit(carImg, (0,0))

x =  (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
