class RiceCakeSoup:
    def __init__(self, age):
        self.age = age

    def drink(self):
        self. age += 1


bob = RiceCakeSoup(2)

while bob.age < 100:
    bob.drink()
    print(f"Bob's age is {bob.age}")

print("Bob is dead...")