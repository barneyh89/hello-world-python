"""
A script to roll nDm where n is the number of die and m is how many faces each die has. The value of each die as well as
the total is printed each time the script is run. 4k ultra HD graphics of the dice are also displayed.

Current limitations:
* Each die needs to have the same number of sides
* The graphics only display if ALL dice have a value less than or equal to 6
* The number of dice and how many faces they have is currently hardcoded under configurables
* The return_dice_as_text function returns "a 11" instead of "an 11". I really CBA to fix that
"""

import random

"""Configurables"""
number_of_dice = 3
faces = 6


def main():
    repeat = True
    while repeat:
        display(roll(number_of_dice, faces))
        print("Do you want to roll again Y/N (please roll again, it...it pleases me?)")
        repeat = "Y" in input().upper()


def roll(number_of_dice, faces):
    return [random.randint(1, faces) for n in range(number_of_dice)]


def display(dice):
    if all(number <= 6 for number in dice):
        for number in dice:
            if number == 1:
                print(" -------")
                print("｜     ｜")
                print("｜  o  ｜")
                print("｜     ｜")
                print(" -------")
            elif number == 2:
                print(" -------")
                print("｜o    ｜")
                print("｜     ｜")
                print("｜    o｜")
                print(" -------")
            elif number == 3:
                print(" -------")
                print("｜o    ｜")
                print("｜  o  ｜")
                print("｜    o｜")
                print(" -------")
            elif number == 4:
                print(" -------")
                print("｜o   o｜")
                print("｜     ｜")
                print("｜o   o｜")
                print(" -------")
            elif number == 5:
                print(" -------")
                print("｜o   o｜")
                print("｜  o  ｜")
                print("｜o   o｜")
                print(" -------")
            elif number == 6:
                print(" -------")
                print("｜o   o｜")
                print("｜o   o｜")
                print("｜o   o｜")
                print(" -------")
    print("You rolled " + return_dice_as_text(dice))


def return_dice_as_text(dice):
    output = ""
    for i in range(len(dice)):
        if i == 0:
            output += f"a {dice[i]}"
            if len(dice) == 1:
                break
        elif i == len(dice) - 1:
            output += f" and a {dice[i]}; totaling {sum(dice)}"
        else:
            output += f", a {dice[i]}"
    return output


if __name__ == "__main__":
    main()
