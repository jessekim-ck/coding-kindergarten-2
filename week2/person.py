
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def greeting(self):
        print(f"My name is {self.name}!")
        print(f"My weight is {self.weight}!")
        print(f"My height is {self.height}!")
        print()
    
    def diet(self):
        self.weight -= 1

    def eat(self):
        self.weight += 1


me = Person("Chankyu Kim", 185, 65)
me.greeting()

me.eat()
me.greeting()

me.diet()
me.greeting()