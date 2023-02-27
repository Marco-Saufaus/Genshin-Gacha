import pygame as pg
from sys import exit
import random

from settings import *

pg.init()
screen = pg.display.set_mode(RES)
pg.display.set_caption("PAY2WIN SIMULATOR")
clock = pg.time.Clock()

background = pg.image.load("resources/Background/Eswgy9JUcAM4gte.jpg")
background = pg.transform.scale(background, RES)
card_test = pg.image.load("resources/Cards/barbara_gacha_card.webp")
card_test = pg.transform.scale(card_test, (240, 764))
card_test2 = pg.image.load("resources/Cards/barbara_gacha_card.webp")
card_test2 = pg.transform.scale(card_test2, (240, 764))
card_test3 = pg.image.load("resources/Cards/barbara_gacha_card.webp")
card_test3 = pg.transform.scale(card_test3, (240, 764))
card_test4 = pg.image.load("resources/Cards/barbara_gacha_card.webp")
card_test4 = pg.transform.scale(card_test4, (240, 764))
card_test5 = pg.image.load("resources/Cards/barbara_gacha_card.webp")
card_test5 = pg.transform.scale(card_test5, (240, 764))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    screen.blit(background, (0, 0))
    screen.blit(card_test, (100, 68))
    screen.blit(card_test2, (390, 68))
    screen.blit(card_test3, (680, 68))
    screen.blit(card_test4, (970, 68))
    screen.blit(card_test5, (1260, 68))
    pg.display.update()
    clock.tick(FPS)

