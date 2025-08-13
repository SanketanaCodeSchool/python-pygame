class Animal:
    def speak(self):
        print("Animal speaks")

class cat(Animal):
    def meow(self):
        print("cat meows")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

c=cat()
c.speak()
c.meow()