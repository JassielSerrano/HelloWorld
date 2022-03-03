import random

def rolldice(min,max):
    while True:
        print("Rolling dice...")
        print(f"Your number : {random.randint(min,max)}")
        choice = input("Do you want to roll the dice again? (y/n)")
        if choice.lower() == 'n':
            break


rolldice(1,6)