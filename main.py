import pygame as pg
from sys import exit
import random

from settings import *

pg.init()
screen = pg.display.set_mode(RES)
pg.display.set_caption("PAY2WIN SIMULATOR")
clock = pg.time.Clock()

test_surface = pg.Surface((200, 300))
test_surface.fill("Red")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    for i in range(5):
        for j in range(2):
            pg.draw.rect(screen, "Red", [i * 300 + 50, j * 400 + 50, 250, 350], 0, 5)

    pg.display.update()
    clock.tick(FPS)

