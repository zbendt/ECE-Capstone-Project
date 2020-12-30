import picamera
from time import sleep
import pygame
import random

WIDTH=1280
HEIGHT=1024
FONTSIZE=25


# INIT CAMERA
camera = picamera.PiCamera()
camera.vflip = False
camera.hflip = False
camera.brightness = 60

# BUILD A SCREEN
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
black = pygame.Color(0, 0, 0)
textcol = pygame.Color(255, 255, 0)
screen.fill(black)

while True:
    # TAKE A PHOTO
    camera.start_preview()
    sleep(0.5)
    camera.capture('image.gif', format='gif', resize=(WIDTH,HEIGHT))
    screen.fill(black)
    pygame.display.update()    
    camera.stop_preview()

    #READ IMAGE AND PUT ON SCREEN
    img = pygame.image.load('image.gif')
    screen.blit(img, (0, 0))

    #OVERLAY CAPTIONS AS TEXT
    text = "Count: " colony_count
    font = pygame.font.Font('freesansbold.ttf', FONTSIZE)
    font_surf = font.render(text, True, textcol)
    font_rect = font_surf.get_rect()
    font_rect.left = 100
    font_rect.top = 100
    screen.blit(font_surf, font_rect)
    pygame.display.update()

    # WAIT A BIT
    sleep(3)

# CLOSE CLEANLY AND EXIT
pygame.quit()