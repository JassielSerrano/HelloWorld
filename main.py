class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def grow_older(self):
        self.age = self.age + 1

    def roll_dice(self):
        import random

        def rolldice(min, max, limit):
            for e in range(5):
                print("Rolling dice...")
                print(f"Your number : {random.randint(min, max)}")
                choice = input("Do you want to roll the dice again? (y/n)")
                if choice.lower() == 'n':
                    quit()
                if choice.lower() != 'y':
                    print("Not(y/n)")
                    quit()
                    # raise Exception

        rolldice(1, 6, 5)
        print('finsihed successfully')


p1 = Player("Rain", 19)
print("Player 1 :", p1.get_name())
p1.grow_older()
p1.grow_older()
print(p1.get_age(), "years old")
p1.roll_dice()
p2 = Player("Jay", 39)
print("Player 2:", p2.get_name())
print(p2.get_age(), "years old")
p2.roll_dice()
