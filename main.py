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
screen.blit(background, (0, 0))


# pulls items from the itempool depending on rarity
for index, pull in enumerate(pulls):
    if pull == "five star":
        screen.blit(rarity_5_bg, card_coordinates[index])
        screen.blit(random.choice(five_star), card_coordinates[index])
    elif pull == "four star":
        screen.blit(rarity_4_bg, card_coordinates[index])
        screen.blit(random.choice(four_star), card_coordinates[index])
    elif pull == "three star":
        screen.blit(rarity_3_bg, card_coordinates[index])
        screen.blit(random.choice(three_star), card_coordinates[index])
    else:
        print(f"{pull} is not valid.")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    clock.tick(FPS)

