import random


def rolldice(min, max, limit):
    for e in range(5):
        print("Rolling dice...")
        print(f"Your number : {random.randint(min,max)}")
        choice = input("Do you want to roll the dice again? (y/n)")
        if choice.lower() == 'n':
            quit()
        if choice.lower() != 'y':
            print("Not(y/n)")
            quit()
            #raise Exception

rolldice(1, 6, 5)
print('finsihed successfully')