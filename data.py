import random
import pygame as pg
import os

rarity = ["five star", "four star", "three star"]
five_star = [100, 200, 300, 400, 500]
four_star = [10, 20, 30, 40, 50]
three_star = ["Ebony_Bow", "Messenger", "Raven_Bow", "Recurve_Bow", "Sharpshooters Oath", "Slingshot"]

# category = random.choice(rarity)
# print(category)
# character = random.choice(list(category))
# print(character)

# creates list of 5 random rarity-options from the rarity list
pulls = random.choices(rarity, weights=(4, 10, 86), k=5)

# pulls items from the itempool depending on rarity
for pull in pulls:
    if pull == "five star":
        print(random.choice(five_star))
    elif pull == "four star":
        print(random.choice(four_star))
    elif pull == "three star":
        print(random.choice(three_star))
    else:
        print(f"{pull} is not valid.")


# if category == "five star":
#     print(random.choice(five_star))
# elif category == "four star":
#     print(random.choice(four_star))
# else:
#     print(random.choice(three_star))

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


