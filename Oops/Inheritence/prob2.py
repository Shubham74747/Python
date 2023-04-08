class Animal:
    animaltype = "Mammal"

class Pets:
    colour = "White"

class Dog:
    @staticmethod
    def bark():
        print("bow bow")

D = Dog
D.bark()