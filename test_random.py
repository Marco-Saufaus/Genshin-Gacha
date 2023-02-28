import pygame as pg
import random
from settings import *

# Rarity Backgrounds
rarity_5_bg = pg.image.load("resources/Background/orange.png")
rarity_4_bg = pg.image.load("resources/Background/purple.png")
rarity_3_bg = pg.image.load("resources/Background/blue.png")

# Characters

# 4-Star
Barbara = pg.image.load("resources/Cards/Characters/4_Star/barbara_gacha_card.webp")
Barbara = pg.transform.scale(Barbara, (240, 764))

# 5-Star


# Weapons

# 3-Star
Ebony_Bow = pg.image.load("resources/Cards/Weapons/3_Star/Bow/Ebony_Bow.webp")
Ebony_Bow = pg.transform.scale(Ebony_Bow, (240, 764))
Messenger = pg.image.load("resources/Cards/Weapons/3_Star/Bow/Messenger.webp")
Messenger = pg.transform.scale(Messenger, (240, 764))
Raven_Bow = pg.image.load("resources/Cards/Weapons/3_Star/Bow/Raven_Bow.webp")
Raven_Bow = pg.transform.scale(Raven_Bow, (240, 764))
Recurve_Bow = pg.image.load("resources/Cards/Weapons/3_Star/Bow/Recurve_Bow.webp")
Recurve_Bow = pg.transform.scale(Recurve_Bow, (240, 764))
Sharpshooters_Oath = pg.image.load("resources/Cards/Weapons/3_Star/Bow/Sharpshooters_Oath.webp")
Sharpshooters_Oath = pg.transform.scale(Sharpshooters_Oath, (240, 764))
Slingshot = pg.image.load("resources/Cards/Weapons/3_Star/Bow/Slingshot.webp")
Slingshot = pg.transform.scale(Slingshot, (240, 764))

# 4-Star


# 5-Star

rarity = ["five star", "four star", "three star"]
five_star = [100, 200, 300, 400, 500]
four_star = [Barbara]
three_star = [Ebony_Bow, Messenger, Raven_Bow, Recurve_Bow, Sharpshooters_Oath, Slingshot]


# pulls items from the itempool depending on rarity


pg.init()
screen = pg.display.set_mode(RES)
pg.display.set_caption("PAY2WIN SIMULATOR")
clock = pg.time.Clock()

background = pg.image.load("resources/Background/Eswgy9JUcAM4gte.jpg")
background = pg.transform.scale(background, RES)

# creates list of 5 random rarity-options from the rarity list
pulls = random.choices(rarity, weights=(0, 10, 90), k=5)

screen.blit(background, (0, 0))

# list of card coordinates
coordinates = [(100, 68), (390, 68), (680, 68), (970, 68), (1260, 68)]

# pulls items from the itempool depending on rarity
for index, pull in enumerate(pulls):
   # for i in coordinates:
    if pull == "five star":
        screen.blit(rarity_5_bg, coordinates[index])
        screen.blit(random.choice(five_star), coordinates[index])
    elif pull == "four star":
        screen.blit(rarity_4_bg, coordinates[index])
        screen.blit(random.choice(four_star), coordinates[index])
    elif pull == "three star":
        screen.blit(rarity_3_bg, coordinates[index])
        screen.blit(random.choice(three_star), coordinates[index])
    else:
        print(f"{pull} is not valid.")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.update()
    clock.tick(FPS)

