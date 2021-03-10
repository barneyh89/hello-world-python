import random

repeat = True
while repeat:
    no = random.randint(1, 6)
    print("You rolled", no)
    if no == 1:
        print("You feel somewhat disappointed")
    if no == 2:
        print("You look at the two dots and begin to mourn a lover lost at sea")
    if no == 3:
        print("Three is the magic number, you turn into a frog")
    if no == 4:
        print("4! You win...not really, you're just rolling a dice. Get some mates!")
    if no == 5:
        print("You bleed a little")
    if no == 6:
        print("You begin to wonder what this point of this is")
    if no == 7:
        print("err...what? This is literally impossible")

    print("Do you want to roll again Y/N (please roll again, it...it pleases me?)")
    repeat = "Y" in input()
