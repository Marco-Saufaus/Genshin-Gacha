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

card_rarity = []

# pulls items from the itempool depending on rarity
for index, pull in enumerate(pulls):
    if pull == "five star":
        card_back = (255, 127, 39)
        screen.blit(rarity_5_bg, card_coordinates[index])
        screen.blit(random.choice(five_star), card_coordinates[index])
        pg.draw.rect(screen, card_back, [card_coordinates[index][0], card_coordinates[index][1], 240, 764], 0, 0)
        card_rarity.append(five_star)
    elif pull == "four star":
        card_back = (163, 73, 164)
        screen.blit(rarity_4_bg, card_coordinates[index])
        screen.blit(random.choice(four_star), card_coordinates[index])
        pg.draw.rect(screen, card_back, [card_coordinates[index][0], card_coordinates[index][1], 240, 764], 0, 0)
        card_rarity.append(four_star)
    elif pull == "three star":
        card_back = (153, 217, 234)
        screen.blit(rarity_3_bg, card_coordinates[index])
        screen.blit(random.choice(three_star), card_coordinates[index])
        pg.draw.rect(screen, card_back, [card_coordinates[index][0], card_coordinates[index][1], 240, 764], 0, 0)
        card_rarity.append(three_star)
    else:
        print(f"{pull} is not valid.")

print(card_rarity)

rect1 = pg.Rect(100, 68, 240, 764)
rect2 = pg.Rect(390, 68, 240, 764)
rect3 = pg.Rect(680, 68, 240, 764)
rect4 = pg.Rect(970, 68, 240, 764)
rect5 = pg.Rect(1260, 68, 240, 764)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONUP:
            mouse_position = pg.mouse.get_pos()
            if rect1.collidepoint(mouse_position):
                rect1 = pg.Rect(0, 0, 0, 0)
                screen.blit(random.choice(card_rarity[0]), (100, 68))
            elif rect2.collidepoint(mouse_position):
                rect2 = pg.Rect(0, 0, 0, 0)
                screen.blit(random.choice(card_rarity[1]), (390, 68))
            elif rect3.collidepoint(mouse_position):
                rect3 = pg.Rect(0, 0, 0, 0)
                screen.blit(random.choice(card_rarity[2]), (680, 68))
            elif rect4.collidepoint(mouse_position):
                rect4 = pg.Rect(0, 0, 0, 0)
                screen.blit(random.choice(card_rarity[3]), (970, 68))
            elif rect5.collidepoint(mouse_position):
                rect5 = pg.Rect(0, 0, 0, 0)
                screen.blit(random.choice(card_rarity[4]), (1260, 68))
    pg.display.update()
    clock.tick(FPS)
    pg.display.flip()

