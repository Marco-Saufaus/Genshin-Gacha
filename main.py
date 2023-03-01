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

new_game = True

# pulls items from the itempool depending on rarity

rect1 = pg.Rect(100, 68, 240, 764)
rect2 = pg.Rect(390, 68, 240, 764)
rect3 = pg.Rect(680, 68, 240, 764)
rect4 = pg.Rect(970, 68, 240, 764)
rect5 = pg.Rect(1260, 68, 240, 764)

counter = 0

while True:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            exit()

        elif event.type == pg.MOUSEBUTTONUP:
            mouse_position = pg.mouse.get_pos()
            if rect1.collidepoint(mouse_position):
                # rect1 = pg.Rect(0, 0, 0, 0)
                fifty_fifty = random.choice(card_rarity[0])
                screen.blit(random.choice(fifty_fifty), (100, 68))
            elif rect2.collidepoint(mouse_position):
                # rect2 = pg.Rect(0, 0, 0, 0)
                fifty_fifty = random.choice(card_rarity[1])
                screen.blit(random.choice(fifty_fifty), (390, 68))
            elif rect3.collidepoint(mouse_position):
                # rect3 = pg.Rect(0, 0, 0, 0)
                fifty_fifty = random.choice(card_rarity[2])
                screen.blit(random.choice(fifty_fifty), (680, 68))
            elif rect4.collidepoint(mouse_position):
                # rect4 = pg.Rect(0, 0, 0, 0)
                fifty_fifty = random.choice(card_rarity[3])
                screen.blit(random.choice(fifty_fifty), (970, 68))
            elif rect5.collidepoint(mouse_position):
                # rect5 = pg.Rect(0, 0, 0, 0)
                fifty_fifty = random.choice(card_rarity[4])
                screen.blit(random.choice(fifty_fifty), (1260, 68))

        while new_game:
            card_rarity = []
            pulls = random.choices(rarity, weights=(2, 10, 88), k=5)
            for index, pull in enumerate(pulls):
                if pull == "five star":
                    card_back = (255, 127, 39)
                    screen.blit(rarity_5_bg, card_coordinates[index])
                    pg.draw.rect(screen, card_back, [card_coordinates[index][0], card_coordinates[index][1], 240, 764],
                                 0, 0)
                    card_rarity.append(five_star)
                elif pull == "four star":
                    card_back = (163, 73, 164)
                    screen.blit(rarity_4_bg, card_coordinates[index])
                    pg.draw.rect(screen, card_back, [card_coordinates[index][0], card_coordinates[index][1], 240, 764],
                                 0, 0)
                    card_rarity.append(four_star)
                elif pull == "three star":
                    card_back = (153, 217, 234)
                    screen.blit(rarity_3_bg, card_coordinates[index])
                    pg.draw.rect(screen, card_back, [card_coordinates[index][0], card_coordinates[index][1], 240, 764],
                                 0, 0)
                    card_rarity.append(three_star)
                else:
                    print(f"{pull} is not valid.")
            new_game = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                new_game = True

    pg.display.update()
    clock.tick(FPS)
    pg.display.flip()

