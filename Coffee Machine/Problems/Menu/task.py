menu = {
    "pizza": "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy",
    "salad": "Caesar salad, Green salad, Tuna salad, Fruit salad",
    "soup": "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
}

kind_of_food = input()
if kind_of_food not in menu:
    print("Sorry, we don't have it in the menu")
else:
    print(menu[kind_of_food])
