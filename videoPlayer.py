from time import sleep
import pygame,os,sys
from pygame.locals import *

dir_path = '/media/usb0'
os.system("clear")
pygame.font.init()
pygame.mixer.init()

display_width = 1680
display_height = 1050
screen = pygame.display.set_mode()
screen.fill((255, 80, 80))

font_path = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
screenImg = pygame.image.load('screensaver.jpeg')

font_size = 70
myfont = pygame.font.Font(font_path, font_size)
myText = pygame.font.Font(font_path, font_size)
videoLabel = []
filePath = []
fileCount = 0

# Text labels
txt_noUSB = myfont.render("No usb storage device found", 1, (0,0,0))
txt_insertUSB = myfont.render("Insert usb device", 1, (0,0,0))
txt_filesFound = myfont.render("Found the following video files", 1, (0,0,0))
txt_playLoop = myfont.render("Playing all content in loop", 1, (0,0,0))

screen.blit(screenImg, (0, 0))
pygame.display.flip()

def centerText(myText):
    return myText.get_rect(center=(display_width/2, display_height/2))

def centerFileText(myText, increment):
    return myText.get_rect(center=(display_width/2, font_size*(increment+1)))

def checkUSBforFiles():
    count = 0
    screen.blit(screenImg, (0, 0))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.mp4'):
                #filePath.append(root+'/'+str(file))
                videoLabel.append(str(file))
                filePath.append(os.path.join(root, file).replace(" ", "\ "))
                count += 1

        screen.blit(txt_filesFound,centerFileText(txt_filesFound, 0))
        for x in range(count):
            fileName = myfont.render(videoLabel[x], 1, (200,0,100))
            screen.blit(fileName,centerFileText(fileName, x+1))
            pygame.display.flip()

        return count
if os.path.ismount(dir_path):
    fileCount = checkUSBforFiles()

else:
    screen.blit(txt_noUSB, centerText(txt_noUSB))
    pygame.display.flip()
    sleep(3)
    while os.path.ismount(dir_path) == False:
        screen.blit(screenImg, (0, 0))
        pygame.display.flip()
        sleep(1)
        screen.blit(txt_insertUSB, centerText(txt_insertUSB))
        pygame.display.flip()
        sleep(1)

    fileCount = checkUSBforFiles()

sleep(5)
screen.blit(screenImg, (0, 0))
screen.blit(txt_playLoop, centerText(txt_playLoop))
pygame.display.flip()
sleep(3)
pygame.quit()

while True:
    for x in range(fileCount):
        os.system("omxplayer " + filePath[x])

