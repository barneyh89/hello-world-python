import random

repeat = True
while repeat:
    print("You rolled", random.randint(1, 6))
    print("Do you want to roll again Y/N (please roll again, it...it pleases me?)")
    repeat = "Y" in input()