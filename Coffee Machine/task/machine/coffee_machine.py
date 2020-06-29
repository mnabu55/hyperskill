# Write your code here
# machine = {"water": 0, "milk": 0, "bean": 0, "cup": 0, "money": 0}
machine = [400, 540, 120, 9, 550]
coffee_menu = {}
method = ["buy", "fill", "take", "remaining", "exit"]

first_message = """
The coffee machine has:
{w} of water
{m} of milk
{b} of coffee beans
{c} of disposable cups
{mo} of money
"""


def show_status():
    print(first_message.format(w=machine[0], m=machine[1], b=machine[2], c=machine[3], mo=machine[4]))


def init():
    coffee_menu[1] = [250, 0, 16, 1, 4]
    coffee_menu[2] = [350, 75, 20, 1, 7]
    coffee_menu[3] = [200, 100, 12, 1, 6]


def buy():
    having_elements = [machine[0], machine[1], machine[2], machine[3]]

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    number = input("> ")
    if number not in ["1", "2", "3"]:
        print("no such coffee")
        return
    number = int(number)
    needed_coffee_elements = coffee_menu[number][:4]
    price = coffee_menu[number][4]
    how_can_coffee_list = []
    for has, need in zip(having_elements, needed_coffee_elements):
        if has == 0 or need == 0:
            how_can_coffee_list.append(has)
        else:
            how_can_coffee_list.append(has // need)
    max_coffee = min(how_can_coffee_list)

    if max_coffee < 1:
        print("No, I can make only {} cups of coffee".format(max_coffee))
    else:
        print("I have enough resources, making you a coffee!")
        for i in range(4):
            machine[i] -= needed_coffee_elements[i]
        machine[4] += price


def fill():
    print("Write how many ml of water the coffee machine add:")
    water = int(input("> "))

    print("Write how many ml of milk the coffee machine add:")
    milk = int(input("> "))

    print("Write how many grams of coffee beans the coffee machine add:")
    bean = int(input("> "))

    print("Write how many disposable cups of coffee do you want to add:")
    cup = int(input("> "))

    machine[0] += water
    machine[1] += milk
    machine[2] += bean
    machine[3] += cup


def take():
    print("I gave you ${mo}".format(mo=machine[4]))
    machine[4] = 0


def remaining():
    show_status()


def exit():
    exit()


def do_action():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input("> ")
    while action != "exit":
        eval(action)()
        print("Write action (buy, fill, take, remaining, exit):")
        action = input("> ")


def main():
    init()
    do_action()


if __name__ == '__main__':
    main()
