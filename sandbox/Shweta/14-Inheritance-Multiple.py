class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print('Can swim')

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack, Quack")


d=  Duck()
d.fly()
d.swim()
d.quack()
