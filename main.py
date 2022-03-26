import random

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

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

    def roll_dice(self, dice):
        print(f"Player named {self.name} rolled the dice and got {dice.roll()}")

d1 = Dice(6)
p1 = Player("Rain", 19)
print("Player 1 :", p1.get_name())
p1.grow_older()
p1.grow_older()
print(p1.get_age(), "years old")
p1.roll_dice(d1)
p2 = Player("Jay", 39)
print("Player 2:", p2.get_name())
print(p2.get_age(), "years old")
p2.roll_dice(d1)