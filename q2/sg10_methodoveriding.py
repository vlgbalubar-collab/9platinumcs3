class Animal

  def __init__(self, name):
    self.name = name

  def eat(self):
    return f"{self.name} eats"

  def make_sound(self):
    return f"{self.name} makes sound"

class Lion(Animal):
    def make_sound(self):
        return f"{self.name} roars loudly!"
    def eat(self):
        return f"{self.name} eats fresh meat."

class Elephant(Animal):
    def make_sound(self):
        return f"{self.name} trumpets!"

    def eat(self):
        return f"{self.name} eats grass and fruits."

class Monkey(Animal):
    def make_sound(self):
        return f"{self.name} chatters!"

    def eat(self):
        return f"{self.name} eats bananas."

animals = [
    Lion("Simba"),
    Elephant("Dumbo"),
    Monkey("George")
]

for animal in animals:
    print(animal.make_sound())
    print(animal.eat())
    print("-----")
