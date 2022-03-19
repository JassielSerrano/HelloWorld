class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def grow_older(self):
        return self.age + 1

p1 = Person("Rain", 19)
print(p1.grow_older())
print(type(p1))
p2= Person("jay", 39)
print(p2.grow_older())
print(type(p2))
#hi