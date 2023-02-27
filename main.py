import pygame as pg
from sys import exit
import random
from data import *
from settings import *

pg.init()
screen = pg.display.set_mode(RES)
pg.display.set_caption("PAY2WIN SIMULATOR")
clock = pg.time.Clock()

background = pg.image.load("resources/Background/Eswgy9JUcAM4gte.jpg")
background = pg.transform.scale(background, RES)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.blit(background, (0, 0))
    screen.blit(Messenger, (100, 68))
    screen.blit(Sharpshooters_Oath, (390, 68))
    screen.blit(Recurve_Bow, (680, 68))
    screen.blit(Slingshot, (970, 68))
    screen.blit(Ebony_Bow, (1260, 68))
    pg.display.update()
    clock.tick(FPS)

