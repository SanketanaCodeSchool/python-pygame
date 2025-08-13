#poly = many
#morph = forms
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat Meow")  



a=Animal()
d=Dog()
c=Cat()
a.speak()
d.speak()
c.speak()

