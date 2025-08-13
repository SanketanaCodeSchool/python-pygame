class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.walk()
d.bark()