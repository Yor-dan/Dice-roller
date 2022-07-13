import random

def greet():
    print("\nWelcome to Dice Rolling Program!")

def restart():
    response = input("\nWant to roll some more dices? (yes/no): ").lower()
    if response == "yes":
        dice()
    else:
        print("\nSee You next time!")

def dice():
    try:
        roll = int(input("\nHow many dice(s) you want to roll? "))
        dices = []

        for i in range(0,roll):
            dices.append(random.randint(1,6))

        print("\nResult: " + ', '.join(map(str,dices)))

        restart()

    except ValueError:
        print('Invalid input!')

greet()
dice()