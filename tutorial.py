import random
import os
import math
import pygame
from os import listdir
from os.path import isfile,join






pygame.init()


pygame.display.set_caption("Platformer")



Bg_image_var = "Gray.png"
WIDTH,HEIGHT = 1000,800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))


class PLAYER(pygame.sprite.Sprite):
    COLOUR = (255,0,0)
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self,dx,dy):
        self.rect.x +=dx
        self.react.y +=dy

    def move_left(self,vel):
        self.x_vel = -vel
        if self.direction!="left":
            self.direction= "left"
            self.animation_count = 0


    def move_right(self,vel):
        self.x_vel = -vel
        if self.direction!="right":
            self.direction= "right"
            self.animation_count = 0

    def loop(self,fps):
        self.move(self.x_vel,self.y_vel)
    
    def draw(self,win):
        pygame.draw.rect(win,self.COLOUR,self.rect)


def get_background(name):
    image = pygame.image.load(join("assets","Background",name))
    _,_,width,height = image.get_rect()
    tiles = []
    for i in range( WIDTH//width+1):
        for j in range(HEIGHT   //height +1):
            pos = (i*width,j*height)
            tiles.append(pos)

    return tiles,image

def draw(window,background,bg_image,player):
    for tile in background:
        window.blit(bg_image,tuple(tile))

    player.draw(window)
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    background,bg_image = get_background(Bg_image_var)

    player = PLAYER(100,100,50,50)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window,background,bg_image,player)                
    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)