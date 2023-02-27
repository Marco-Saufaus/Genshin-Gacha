import random

rarity = ["five star", "four star", "three star"]
five_star = [100, 200, 300, 400, 500]
four_star = [10, 20, 30, 40, 50]
three_star = [1, 2, 3, 4, 5]

category = random.choice(rarity)
print(category)
# character = random.choice(list(category))
# print(character)

# category = random.choices(rarity, weights=(1, 89, 10), k=1)
# print(category)

if category == "five star":
    print(random.choice(five_star))
elif category == "four star":
    print(random.choice(four_star))
else:
    print(random.choice(three_star))


