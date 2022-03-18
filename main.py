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

p = Person("Rain", 19)
print(p.grow_older())
print(type(p))